from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import JsonResponse
import json
from .models import Collection, Photo, SiteCopy

##
# Index - acts as home page
##
def index(request):
  collections = Collection.objects.filter(featured=False)
  featured_collections = Collection.objects.filter(featured=True)
  about_text = None
  try:
    about_text = SiteCopy.objects.get(html="fr").text
  except SiteCopy.DoesNotExist:
    about_text = None
    
  context = {'collections': collections, 'featured_collections': featured_collections, 'about_text': about_text}
  return render(request, 'gallery/index.html', context)
    
def collection(request, collection_id):
  collection = get_object_or_404(Collection, pk=collection_id)
  map_settings = {}
  if collection.lat and collection.lon and collection.zoom:
    map_settings =  { 'DEFAULT_CENTER': (collection.lat, collection.lon),'DEFAULT_ZOOM': collection.zoom }
    
  context = {'collection':collection, 'map_settings':map_settings}
  return render(request, 'gallery/collection.html', context)
  
def collection_geojson(request, collection_id):
  collection = get_object_or_404(Collection, pk=collection_id)
  photos = get_list_or_404(collection.photo_set.all())
  features = [f.get_geojson() for f in photos]
  d = {
      'type': 'FeatureCollection',
      'features': features
  }
  return JsonResponse(d)
  
  
def photo(request, photo_id):
  photo = get_object_or_404(Photo, pk=photo_id)
  memories = photo.memory_set.all()
  map_settings = {}
  if photo.location:
    map_settings =  { 'DEFAULT_CENTER': (photo.location["coordinates"][1], photo.location["coordinates"][0]),'DEFAULT_ZOOM': 16 }

  photo_json = json.dumps(photo.location)
  context = {'photo':photo, 'memories':memories, 'map_settings':map_settings, 'photo_json': photo_json}
  print context
  return render(request, 'gallery/photo.html', context)

def about(request):
  try:
    about_text = SiteCopy.objects.get(html="ab").text
  except SiteCopy.DoesNotExist:
    about_text = None
    
  context = {'about_text':about_text}
  return render(request, 'gallery/about.html', context)
