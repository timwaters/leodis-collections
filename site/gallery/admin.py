from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Photo, Collection, Memory, SiteCopy

class MemoryInline(admin.StackedInline):
    model = Memory
    extra = 1
    

class PhotoAdmin(LeafletGeoAdmin ):
  fields = ['image', 'image_tag','collection','title','description','creator','location', 'subject_id','featured','created_at', 'updated_at' ]
  readonly_fields = ('created_at', 'updated_at','image_tag')
  list_display = ('pk','title', 'subject_id', 'collection','image', 'image_admin_tag','featured','memories', 'geocoded', 'updated_at')
  list_filter = ['collection','updated_at']
  list_display_links = ('pk','title',)
  search_fields = ['title', 'description', 'creator']
  save_on_top = True
  inlines = [MemoryInline]
  

admin.site.register(Photo, PhotoAdmin)


class CollectionAdmin(LeafletGeoAdmin):
  fields = ['title','description','featured','centre','zoom','lat','lon','created_at','updated_at']
  readonly_fields = ('created_at', 'updated_at',)
  list_display = ('title','featured', 'updated_at')
  search_fields = ['title', 'description']
  save_on_top = True
  
  class Media:
    js = (
        '/static/gallery/admin/collectionadmin.js',
    )

admin.site.register(Collection, CollectionAdmin)

class SiteCopyAdmin(admin.ModelAdmin):
  fields = ['html', 'text']
  list_display = ('html', 'pk')
  save_on_top = True
  
admin.site.register(SiteCopy, SiteCopyAdmin)


