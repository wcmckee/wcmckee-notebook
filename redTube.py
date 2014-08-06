# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# RedTube json Python

# <codecell>


# <codecell>


# <codecell>

import requests
import json
import random

# <markdowncell>

# Requests and json are the two main modules used for this. Random can also be handy

# <codecell>

getPrn = requests.get('http://api.redtube.com/?output=json&data=redtube.Videos.searchVideos&page=1')

# <markdowncell>

# Simple requests command to get the json object. This could be any json object - not just RedTube

# <codecell>

loaPrn = json.loads(getPrn.text)
#print loaUrl

# <markdowncell>

# Convert it into readable text that you can work with

# <codecell>

naoPrn = loaPrn[u'videos'][0]
print naoPrn

# <markdowncell>

# Compress down - look at first element of json object. You could cycle through older elements
# by increasing the int

# <codecell>

ngePrn = naoPrn[u'video']
print ngePrn

# <markdowncell>

# Compress down again - this time video. It's always a bit of a trial and error to figure out
# navagating json objects, IPython is perfect for this. 

# <headingcell level=2>

# Individual Data!

# <markdowncell>

# This could be imporoved by turning the following unicode into a list and get the program
# to cycle though - saving off each element. Maybe save to a list?

# <codecell>

ratPrn = ngePrn[u'rating']

# <codecell>

thumPrn = ngePrn[u'thumb']

# <codecell>

print thumPrn

# <codecell>

ratPrn = ngePrn[u'ratings']
print ratPrn

# <codecell>

urlPrn = ngePrn[u'url']
print urlPrn

# <codecell>

viwPrn = ngePrn[u'views']
print viwPrn

# <codecell>

idPrn = ngePrn[u'video_id']
print idPrn

# <codecell>

pdaPrn = ngePrn[u'publish_date']
print pdaPrn

# <codecell>

timPrn = ngePrn[u'duration']
print timPrn

# <codecell>

titPrn = ngePrn[u'title']
print titPrn

# <codecell>

tagPrn = ngePrn[u'tags']
print tagPrn

# <codecell>

derbPrn = (tagPrn, 'tag_name')
print derbPrn

# <codecell>

thNum = 0
taTrn = tagPrn[thNum]
print taTrn
thNum + 1

# <markdowncell>

# TODO: Cycle the list and print all tags

# <codecell>

naTrn = taTrn['tag_name']
print naTrn

# <codecell>


# <headingcell level=2>

# Saving Data

# <markdowncell>


# <codecell>

import dominate

# <codecell>

savPrn = open('savPrn','w')
savPrn.write('<h3 style="text-align: center;"><a href="' + urlPrn + '">')
savPrn.write(titPrn + '</a></h3>')
savPrn.write('<p style="text-align: right;">' + pdaPrn)
savPrn.write('</a></h3><img class="aligncenter" alt="null" src="' + thumPrn)
savPrn.write('" />')
savPrn.close()

# <codecell>

opPrn = open('savPrn','r')
for op in opPrn:
    print op

# <codecell>


# <codecell>


# <codecell>


