from django.db import models
from djgeojson.fields import PointField
import urllib, urllib2
from django.http import HttpResponse
from bs4 import BeautifulSoup
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
import os

class Collection(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField(blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  featured = models.BooleanField(default=False)
  centre = PointField(null=True, blank=True, help_text="move map to set default view")
  lat = models.FloatField(null=True, blank=True, help_text="Gets updated when the map is moved")
  lon = models.FloatField(null=True, blank=True, help_text="Gets updated when the map is moved")
  zoom = models.IntegerField(null=True, blank=True, help_text="Gets updated when the map is moved")

  def __str__(self):
      return self.title
  
  @receiver(post_save)
  def cache_clear(sender, instance, **kwargs):
      cache.clear()
      
  def featured_photo(self):
    featured_photos = self.photo_set.all().filter(featured=True)
    featured_photo = None
    if len(featured_photos) == 0:
      featured_photo = self.photo_set.all().first()
    else:
      featured_photo = featured_photos[0]
      
    return featured_photo
    
  def related_photos(self):
    featured_photos = self.photo_set.all().filter(featured=True)
    related_photos = None
    if len(featured_photos) == 0:
      related_photos = self.photo_set.all().filter(featured=False).exclude(image__isnull=True)[1:4]
    else:
      related_photos = self.photo_set.all().filter(featured=False).exclude(image__isnull=True)[:3] 
      
    return related_photos

    
    

class Photo(models.Model):
  title = models.CharField(blank=True, max_length=255, help_text="Keep blank when adding to autofill from Leodis.net")
  description = models.TextField(blank=True, help_text="Keep blank when adding to autofill from Leodis.net")
  collection =  models.ForeignKey(Collection, null=True, blank=True, on_delete=models.SET_NULL)
  year = models.IntegerField(null=True)
  subject_id = models.CharField(blank=True, null=True, unique=True, max_length=128, help_text="Keep blank when adding to autofill from Leodis.net" )
  featured = models.BooleanField(default=False)
  location = PointField(null=True,blank=True)
  image = models.ImageField(upload_to="photos", null=True)
  creator = models.CharField(blank=True, max_length=255, help_text="Keep blank when adding to autofill from Leodis.net")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
  
  @receiver(post_save)
  def cache_clear(sender, instance, **kwargs):
      cache.clear()
    
  def image_tag(self):
      return u'<img src="%s" />' % self.image.url
      
  image_tag.short_description = 'Image'
  image_tag.allow_tags = True      
  
  def image_admin_tag(self):
      return '<img src="/media/%s" height="80" />' % get_thumbnailer(self.image)['admin_thumb']
  image_admin_tag.allow_tags = True
  image_admin_tag.short_description = 'Thumbnail'
  
  def memories(self):
    return self.memory_set.count()
    
  def geocoded(self):
    return self.location is not None
      
  
  def save(self, *args, **kwargs):
    within_autopop = False
    if "within_autopop" in kwargs:
      within_autopop = True

    if (not self.pk) and (within_autopop == False):
      self = self.auto_populate()
  
    if within_autopop == True:
      del kwargs["within_autopop"]
      
    super(Photo, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
      self.image.delete(save=False)
      super(Photo, self).delete(*args, **kwargs)
        
  def auto_populate(self):
    subject_id = self.subject_id
    if subject_id == '' or subject_id is None:
      subject_id = os.path.splitext(os.path.basename(self.image.url))[0]
  
    url = 'http://www.leodis.net/display.aspx?resourceIdentifier='+subject_id+'&DISPLAY=FULL'
    print "calling" + url
    try:
      soup = BeautifulSoup(urllib2.urlopen(url, timeout=2), "html.parser")
    except (urllib2.HTTPError, urllib2.URLError):
      print "Error calling url"
      return self

    title = self.title
    if title == '':
      title_content = soup.find("meta", attrs={'name': 'DC.Title', 'content': True}) 
      if title_content:
        title = title_content['content']
    
    description = self.description
    if description == '':
      desc_content = soup.find("meta", attrs={'name': 'DC.Description', 'content':True})
      if desc_content:
        description = desc_content['content']
        
    creator = self.creator
    if creator == '':
      creator_content = soup.find("meta", attrs={'name': 'DC.Creator', 'content':True})
      if creator_content:
        creator = creator_content['content']
        
    if self.memory_set.all().count() == 0:
      comment_name = None
      comment_text = None
      name_div = soup.find('div', attrs={'class':'commentHeader'}, text='Name:')
      if name_div:
        comment_name = name_div.next_sibling.text

      comment_div = soup.find('div', attrs={'class':'commentHeader'}, text='Comment:')
      if comment_div:
        comment_text = comment_div.next_sibling.text
        
      if comment_name and comment_text:
        self.save(within_autopop=True)
        print "saving new memory"
        self.memory_set.create(name=comment_name, text=comment_text)

    print "updating photo"
    self.title = title
    self.description = description
    self.creator = creator
    self.subject_id = subject_id
    return self
    
  def get_geojson(self):
      #if not self.location == None:
      geom = self.location
      feature_type = 'Point'
      
      properties = {
          'id': self.id,
          'title': self.title,
          'icon' : get_thumbnailer(self.image)['popup'].url
      }
      return {
          'type': 'Feature',
          'properties': properties,
          'geometry': geom
      }        
    
  
class Memory(models.Model):
    text = models.TextField(blank=True)
    name = models.CharField(max_length=255)
    photo = models.ForeignKey(Photo)
    
    @receiver(post_save)
    def cache_clear(sender, instance, **kwargs):
        cache.clear()


class SiteCopy(models.Model):
    text = models.TextField(blank=True)
    HTML_CHOICES = (
      ('ab', 'About Page'),
      ('fr', 'Front Page About Text'),
    )
    html = models.CharField(max_length=2, choices=HTML_CHOICES, default='about', unique=True)

    @receiver(post_save)
    def cache_clear(sender, instance, **kwargs):
        cache.clear()
