# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# RedTube json Python

# <markdowncell>

# This takes data from the website redtube and saves it as an index.html.
# When I first wrote this script I manually wrote the html tags. That was before I found dominate. 
# Since discovering dominate I have been using it everywhere. It allows me to visually see the output of the scripts I write. 
# The posibilities are endless...

# <codecell>

import os
import random
import requests
from bs4 import BeautifulSoup
import re
import json
import time
import dominate
from dominate.tags import *
from time import gmtime, strftime

# <markdowncell>

# Requests and json are the two main modules used for this. Random can also be handy

# <codecell>

getprn = requests.get('http://api.redtube.com/?output=json&data=redtube.Videos.searchVideos&page=1')

# <markdowncell>

# Simple requests command to get the json object. This could be any json object - not just RedTube

# <codecell>

loaprn = json.loads(getprn.text)
#print loaUrl

# <markdowncell>

# Convert it into readable text that you can work with

# <codecell>

naoprn = loaprn[u'videos'][0]
print naoprn

# <markdowncell>

# Compress down - look at first element of json object. You could cycle through older elements
# by increasing the int

# <codecell>

ngeprn = naoprn[u'video']
print ngeprn

# <markdowncell>

# Compress down again - this time video. It's always a bit of a trial and error to figure out
# navagating json objects, IPython is perfect for this. 

# <headingcell level=2>

# Individual Data!

# <markdowncell>

# This could be imporoved by turning the following unicode into a list and get the program
# to cycle though - saving off each element. Maybe save to a list?

# <codecell>

prnliz = []

# <codecell>

for nge in ngeprn:
    prnliz.append(ngeprn[nge])
    print nge
    print len(nge)

# <codecell>

prnliz

# <codecell>

for liz in prnliz:
    print liz

# <codecell>

tagprn = ngeprn[u'tags']
print tagprn

# <codecell>

tagval = []

# <codecell>

for ta in tagprn:
    print ta.values()
    tagval.append(ta.values())

# <codecell>

for tag in tagval:
    print tag

# <codecell>

derbprn = (tagprn, 'tag_name')
print derbprn

# <codecell>

for deb in derbprn:
    print deb

# <codecell>


# <headingcell level=2>

# Saving Data

# <codecell>

doc = dominate.document(title='nsfw')

# <codecell>

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(id=header):
        attr(cls='header')
        #<img src="smiley.gif" alt="Smiley face" height="42" width="42">
        h1('nsfw')
        img(scr='logo.gif')
        h2('warning: porn. get out now.')
        p(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        a('about', href='http://brobeur.com/nsfw/about')
        a('contact', href='http://brobeur.com/nsfw/contact') 
        a('blog', href='http://brobeur.com/wcmckee.com/wcmckee/output')
        
    with div(id='body'):
        h1(prnliz[9])
        #img(prnliz[1])
        (img(src= prnliz[1]))
        #for liz in prnliz:
        #    h1(liz)[7]
        for tag in tagval:
            p(tag)
    
    
    
    
    
    
    
    
    
    
                                                                                                                                                                                                                 #with div(id='pnr').add(p()):
        #for i in jplis:
            #(img(i.lower(), src='%s' % i))
            #(a(i.lower(), href='%s' % i))
            
    with div(id='footer'):
        p(a('nsfw: warning porn - is open source', href='https://github.com/wcmckee/wcmckee-notebook'))


            

print doc

# <codecell>

os.chdir('/home/wcmckee/nsfw/')

# <codecell>


# <codecell>

savPrn = open('index.html','w')
savPrn.write(str(doc))
savPrn.close()

# <codecell>

opPrn = open('index.html','r')
for op in opPrn:
    print op

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


