from django.core.management.base import BaseCommand, CommandError
from django.core.files import File
from gallery.models import Photo, Collection
import os

#
# python manage.py import_photos /path/to/photos --collection_id=2
#

class Command(BaseCommand):
    help = 'Adds photos to a collection'

    def add_arguments(self, parser):
        parser.add_argument('directory', help='directory of photos to import')
        parser.add_argument('--collection_id', help='collection id of photos to add to', type=int)

    def handle(self, *args, **options):
        collection = None
        print options["collection_id"]
        if options["collection_id"]:
          collection = Collection.objects.get(pk=options["collection_id"])

        photos = os.listdir(options['directory'])
        for photo_name in photos:
          print "photo name "+ photo_name
          photo_path = os.path.join(options['directory'], photo_name)
          if os.path.isfile(photo_path):
            print photo_path
            sub_id = os.path.splitext(os.path.basename(photo_path))[0]
            print sub_id
            if not Photo.objects.filter(subject_id=sub_id).exists():
      
              new_photo = Photo()
              if collection:
                new_photo.collection = collection
              filename = os.path.basename(photo_name)
              fobject  = open(photo_path)
              dfile = File(fobject)
              new_photo.image.save(filename, dfile)
              fobject.close()
              print str(new_photo)
            else:
              print "image already exists with subject_id of " + sub_id

        
