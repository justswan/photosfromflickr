#!/usr/bin/python
import urllib2
import json 
import sys
import os

api_key = u'key'
api_secret = u'secret'
user_id = u'44672786%40N00'

def getPhotoSets():
	photosets_getList='https://api.flickr.com/services/rest/?method=flickr.photosets.getList&user_id='+user_id+'&per_page=500&format=json&nojsoncallback=1&api_key='+api_key
	jresp=urllib2.urlopen(photosets_getList)
	jresp=json.loads(jresp.read())
	return jresp['photosets']['photoset']

def getPhotos(id):
	photosets_getPhotos='https://api.flickr.com/services/rest/?method=flickr.photosets.getPhotos&api_key='+api_key+'&photoset_id='+id+'&user_id='+user_id+'&per_page=500&privacy_filter=1&media=photos&format=json&nojsoncallback=1&extras=url_o'
	jresp=urllib2.urlopen(photosets_getPhotos)
	jresp=json.loads(jresp.read())
	return jresp


exclude_sets=set(['580232','652770','1038222','72157633450533676','72157594473086965'])

try:
	fpath=sys.argv[1]
	print "saving photos to"+fpath
except:
	print "usage:"
	print sys.argv[0]+" path_to_save_images"
	exit()

for Photo_set_id in getPhotoSets():
    if Photo_set_id['id'] not in exclude_sets:
	    for photo in getPhotos(Photo_set_id['id'])['photoset']['photo']:
			photo_url=photo['url_o']
			filename=photo_url.split('/')[-1]
			os.system("curl -C - -# -o "+fpath+"/"+filename+" \'"+photo_url+"\'")