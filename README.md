Leodis Collections
====

http://leodiscollections.net

What
=====

This is a django python web application for showing collections of historical photos on a map. It enables staff users to georeference photos using the django admin. The database is sqlite, but any SQL databse should be fine. The system has file based caching enabled to improve performance.

There are four main components to the site:

1) Front page showing all collections

![Alt text](docs/front-page.png?raw=true "Front Page")

2) Collection view showing a collection and all photos within that collection

![Alt text](docs/collections-page.png?raw=true "Collection Page")

3) Photo view showing an individual photo

![Alt text](docs/photo-page.png?raw=true "Photo Page")

4) Admin django admin pages

![Alt text](docs/admin-pages.png?raw=true "Admin Pages")

It is tightly integrated with the exising Leodis.net website. Photos have to have a filename which is same UUID as used in the Leodis.net site. Metadata about the photos is queried using BeautifulSoup. Additionally memories, comments about the photos are also retrieved from Leodis.net. 

Directories of photos can be imported into an existing collection at once using the following management command:

```python manage.py import_photos /path/to/photos --collection_id={id}```

About
====

A prototype interface of the Leodis website - The Leeds City Council Library's historical photo website.  Tim Waters worked closely with the libraries team to re-imagine how the Leodis archive, which has over 60,000 images, can be used to share stories about the city. These collections of images will grow and develop and can be used by people to share the stories which are important to them. 

The new interface has been created through the 6 month Innovation Pathway. It uses images from Leodis, managed by Leeds Library and Information Service, published on the Leeds Data Mill, the open data repository for the city.

The Innovation Pathway is a ground breaking collaboration between Leeds City Council and the Sustainable Development Lab http://sustainabledevelopmentlab.com/ 

Tim Waters, a Geo-spatial developer and member of the Lab has worked globally to help organisations digitise their collections and improve access.


