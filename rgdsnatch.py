# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# RedditGetsDrawn Snatch
# 
# This is a Python script that takes data from reddit and posts it to another subreddit. It also creates a html file with the images embed into. The images are the most recent 25 on r/redditgetsdrawn.
# 

# <markdowncell>

# TODO
# 
# submit art to users via website
# 
# fix image sizes (need to scale down to 550px)
# 
# Save to server rather than imgur
# 
# Archieve, snapshots of rgd
# 
# more artcontrol
# 
# itwillbemine comments to html
# 
# work on css, div up page, title, side, body, footer
# 

# <codecell>

import os
import random
import requests
import re
import json
import praw
import dominate
from dominate.tags import *

# <codecell>

os.chdir('/var/www/artcontroldrawsyou')

# <codecell>

r = praw.Reddit(user_agent='rgdsnatch')

# <codecell>

r.login('artcontrol', 'zipit123')

# <codecell>

usrd = r.get_my_subreddits()

# <codecell>

suls = []

# <codecell>

for subs in usrd:
    print subs
    suls.append(subs)

# <codecell>

suls

# <codecell>

lesuls = len(suls)

ransuz = random.randint(0, lesuls)

thesubraz = suls[ransuz]

# <codecell>

suls

# <codecell>

print thesubraz

# <codecell>

rd = r.get_subreddit('redditgetsdrawn')

# <codecell>

rdnewz = rd.get_new()

# <codecell>

rdnew = []

# <codecell>

rdnew

# <codecell>

for uz in rdnewz:
    #print uz
    rdnew.append(uz)

# <codecell>

urzlis = []
titlis = []

# <codecell>

#os.chdir('imgs')

# <codecell>

for rdn in rdnew:
    print rdn.url
    urzlis.append(rdn.url)
    titlis.append(rdn.author.name)
    

# <codecell>

titlis

# <codecell>

jplis = []

# <codecell>

for urz in urzlis:
    if '.jpg' in urz:
        jplis.append(urz)

# <codecell>

doc = dominate.document(title='artcontroldrawsyou')

# <codecell>

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div():
        attr(cls='header')
        #<img src="smiley.gif" alt="Smiley face" height="42" width="42">
        h1('artcontroldrawsyou!')
        p(img(scr='http://brobeur.com/artcontroldrawsyou/logo.gif'))
        h2('go away artcontrol')
        
    with div(id='author'):
        for tits in titlis:
            h3(tits)
            h2(a(tits, href='%s' % tits))
    
    with div(id='body').add(p()):
        for i in jplis:
            li(img(i.lower(), src='%s' % i))
            li(a(i.lower(), href='%s' % i))
            



print doc

# <codecell>


# <codecell>

ophtml = open('index.html', 'w')

# <codecell>

ophtml.write(str(doc))

# <codecell>

ophtml.close()

# <codecell>

import PIL

# <codecell>

jplis

# <codecell>

rdnew

# <codecell>

ransubz = random.randint(0,24)

# <codecell>

print ransubz

# <codecell>

ransev = rdnew[ransubz]

# <codecell>

rgdautoz = str(ransev.author)

# <codecell>

rgdsubred = str(ransev.subreddit)

# <codecell>

sutit = ('[' + rgdsubred + ']')

# <codecell>

sutit

# <codecell>

rgdaqwew = ('xpost[RGD]' + rgdautoz)

# <codecell>

rgdaturo = str(ransev.url)

# <codecell>

rgdatit = str(ransev.title)

# <codecell>

rgdatit

# <codecell>

#rd.get_top

# <codecell>

linkdict = {}

# <codecell>

ls

# <codecell>

ady = r.get_subreddit('artcontroldrawsyou')

# <codecell>

comrgd =  rgdatit + ' ' + rgdaturo

# <codecell>

comrgd

# <codecell>

import time

# <codecell>

loctime = time.localtime()

# <codecell>

loctime.tm_mday

# <codecell>

loctime.tm_mon

# <codecell>

thedat = (str(loctime.tm_mday) + '/' + str(loctime.tm_mon))

# <codecell>

thedat

# <codecell>

mixtut = (thedat + sutit + rgdautoz)

# <codecell>

loctime

# <codecell>

ady.submit(mixtut , (rgdaqwew, comrgd))

# <rawcell>

# for newa in rdnew:
#     #rint newa.url
#     print len(newa)
#     htmstr = (str(newa.title) + '<a href="' + 
#                  str(newa.url) + 
#                  '"><img class="aligncenter size-large wp-image-5723" alt="' +
#                  str(newa.author) +
#                  '" src="' + 
#                  str(newa.url) + 
#                  '" /></a>')
#     #ophtml.write(htmstr)
#     #ady.submit(('[RGD]' + newa.author), newa.url)
#     print newa.author
#     #print newa.media
#     ophtml.write(htmstr)
#     print newa.selftext
#     print newa.url
#     print newa.num_comments
#     
#     linkdict.update({str(newa.author): str(newa.url)})

# <codecell>

#print str(newa.title)

# <codecell>

import json

# <codecell>

newzjson = json.dumps(linkdict)

# <codecell>

#newzjson

# <codecell>


# <codecell>

rmine = r.get_redditor('itwillbemine')

# <codecell>

#opest = open('userurl.json', 'r')
#opest.read()
#opest.close()

# <codecell>

mincom = rmine.get_comments()

# <codecell>

#print mincom

# <codecell>

minels = []

# <codecell>


dausr = {}

# <codecell>

for newa in rdnew:
    #rint newa.url
    #print newa.author
    linkdict.update({str(newa.author): str(newa.url)})

# <codecell>

for con in mincom:
    #print con.body
    minels.append(con)
    dausr.update({str(con.id): str(con.body)})

# <codecell>

itwillbemine = dominate.document(title='itwillbemine')

# <codecell>

with itwillbemine.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with itwillbemine:
    with div():
        attr(cls='header')
        #<img src="smiley.gif" alt="Smiley face" height="42" width="42">
        h1('itwillbemine')
        p(img(scr='http://brobeur.com/artcontroldrawsyou/logo.gif'))
        for mine in minels:
            h1(mine.created)
            h2(mine.body)
        
    with div(id='author'):
        for tits in titlis:
            h3(tits)
    
    with div(id='body').add(p()):
        for i in jplis:
            li(img(i.lower(), src='%s' % i))
            li(a(i.lower(), href='%s' % i))
            



print itwillbemine

# <codecell>

minels

# <codecell>

noizjson = json.dumps(dausr)

# <codecell>

newposts = open('userurl.json', 'a')
newposts.write(newzjson)
print ('file userurl.json updated')
newcomments = open('idcomt.json', 'a')
newcomments.write(noizjson)
print ('user comments updated')
newposts.close()
newcomments.close()

# <codecell>

rdusr = str(con.author)

# <codecell>

minelsz = []

# <codecell>

#for mina in minels:
    #print mina.body
   # minelsz.append(mina.body)

# <codecell>

#minelsz

# <codecell>

#mina.body

# <codecell>


# <codecell>


# <codecell>


# <codecell>


