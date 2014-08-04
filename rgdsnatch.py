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
# itwillbemine comments to html - currently being saved in contact 
# 
# work on css, div up page, title, side, body, footer
# 
# update twitter with ONE IMAGE and announce that the list has been updated.
# 
# write blog post and submits to artcontroldrawsyou/blog 
# 
# 
# 

# <codecell>

import os
import random
import requests
import re
import json
import time
import praw
import dominate
from dominate.tags import *

# <codecell>

os.chdir('/var/www/artcontroldrawsyou')

# <codecell>

r = praw.Reddit(user_agent='rgdsnatch')

# <codecell>

#r.login('artcontrol', 'taylor123vag!')

# <codecell>

rd = r.get_subreddit('redditgetsdrawn')

# <codecell>

subz = rd.get_hot().next()
istit = (subz.title)
istxt = (subz.selftext_html)
istick = (subz.stickied)

# <codecell>

istit

# <codecell>

istxt

# <codecell>

if istick = True:
    

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

from time import gmtime, strftime

# <codecell>

for iz in jplis:
    print iz

# <codecell>

for urz in urzlis:
    if '.jpg' in urz:
        jplis.append(urz)

# <codecell>

doc = dominate.document(title='artcontroldrawsyou')

# <codecell>


# <codecell>

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div():
        attr(cls='header')
        #<img src="smiley.gif" alt="Smiley face" height="42" width="42">
        h1('artcontroldrawsyou!')
        img(scr='logo.gif')
        h2('go away artcontrol')
        p(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        a('about', href='http://brobeur.com/artcontroldrawsyou/about')
        a('contact', href='http://brobeur.com/artcontroldrawsyou/contact') 
        a('blog', href='http://brobeur.com/wcmckee.com/wcmckee/output')
        
    with div(id='authors'):
        for tits in titlis:
            (tits)
            (a(tits, href='https://reddit.com/u/%s' % tits))
            
    
    with div(id='body').add(p()):
        for i in jplis:
            (img(i.lower(), src='%s' % i))
            (a(i.lower(), href='%s' % i))
            
    with div(id='footer'):
        p(a('artcontroldrawsyou is open source', href='https://github.com/wcmckee/wcmckee-notebook'))


            

print doc

# <codecell>

ophtml = open('index.html', 'w')

# <codecell>

ophtml.write(str(doc))

# <codecell>

ophtml.close()

# <codecell>

'''def fcopy(src,dest):
    """
    Copy file from source to dest.  dest can include an absolute or relative path
    If the path doesn't exist, it gets created
    """
    dest_dir = os.path.dirname(dest)
    try:
        os.makedirs(dest_dir)
    except os.error as e:
        pass #Assume it exists.  This could fail if you don't have permissions, etc...
    shutil.copy(src,dest)'''

# <markdowncell>

# cycle though folder and create file in each folder

# <codecell>

#fcopy('/var/www/artcontroldrawsyou/home/')

# <codecell>

for usz in titlis:
    print usz
    #os.mkdir(usz)
    #os.chdir('/var/www/artcontroldrawsyou/home/' + usz)

# <codecell>

'''for filz in titlis:
    print filz
    
    
    #os.chdir('/var/www/artcontroldrawsyou/home' + usz)
    bulkc = dominate.document(title=filz)
    with bulkc.head:
        link(rel='stylesheet', href='style.css')
        script(type='text/javascript', src='script.js')

    with bulkc:
        with div():
            attr(cls='header')
            #<img src="smiley.gif" alt="Smiley face" height="42" width="42">
            h1(filz)
            img(scr='http://artcontrol.me/wp-content/uploads/2014/08/daenuhlyn-headcoloe.png')
            h2('go away artcontrol')
        
        with div(id='photographs'):
            for tits in titlis:
                h3(tits)
                (a(tits, href='%s' % tits.lower))
            
    
        with div(id='body').add(p()):
            for i in jplis:
                li(img(i.lower(), src='%s' % i))
                li(a(i.lower(), href='%s' % i))
                
        with div(id='footer'):
            p(a('artcontroldrawsyou is opensource', href='https://github.com/wcmckee/wcmckee-notebook'))
        
        with open('/var/www/artcontroldrawsyou/home/' + filz + '/index.html', 'w') as fout:
            fout.write(str(bulkc))
            
    #with open('index.html', 'w') as indx:
       #bulkc = indx.write() 
        #print bulkc'''

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

ady = r.get_subreddit('artcontroldrawsyou')

# <codecell>

comrgd =  rgdatit + ' ' + rgdaturo

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

#ady.submit(mixtut , (rgdaqwew, comrgd))

# <codecell>

'''for newa in rdnew:
    #rint newa.url
    print len(newa)
    htmstr = (str(newa.title) + '<a href="' + 
                 str(newa.url) + 
                 '"><img class="aligncenter size-large wp-image-5723" alt="' +
                 str(newa.author) +
                 '" src="' + 
                 str(newa.url) + 
                 '" /></a>')
    #ophtml.write(htmstr)
    #ady.submit(('[RGD]' + newa.author), newa.url)
    print newa.author
    #print newa.media
    ophtml.write(htmstr)
    print newa.selftext
    print newa.url
    print newa.num_comments
    
    linkdict.update({str(newa.author): str(newa.url)})
'''

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
        img(scr='logo.gif')
        h2('go away artcontrol')
        p(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        a('about', href='http://brobeur.com/artcontroldrawsyou/about')
        a('contact', href='http://brobeur.com/artcontroldrawsyou/contact') 
        a('blog', href='http://brobeur.com/artcontroldrawsyou/wcmckee.com/wcmckee/output')
    
    with div():
        attr(cls='header')
        #<img src="smiley.gif" alt="Smiley face" height="42" width="42">
        h1('itwillbemine')
        p(img(scr='http://brobeur.com/artcontroldrawsyou/logo.gif'))
        #for mine in minels:
            #h1(mine.author_flair_text())
            #p(mine.body)
        
    with div(id='author'):
        for tits in titlis:
            h3(tits)
    
    with div(id='body').add(p()):
        for mine in minels:
            #h1(mine.created)
            p(mine.body)
            



print itwillbemine

# <codecell>

savmine = open('reddit.html', 'w')
savmine.write(str(itwillbemine))
savmine.close()

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

import feedparser

# <codecell>

mcs = feedparser.parse('http://mcsteffen.tumblr.com/rss')

# <codecell>

emcs = mcs['entries']

# <codecell>

for em in emcs:
    print em

# <codecell>

tumlis = []

# <codecell>

for em in emcs:
    tumlis.append((em['summary_detail']['value']))
    

# <codecell>

tumlis

# <codecell>

contactpage = dominate.document(title='contact')

# <codecell>

with contactpage.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with contactpage:
    with div():
        attr(cls='top')
        #<img src="smiley.gif" alt="Smiley face" height="42" width="42">
        h1('artcontroldrawsyou!')
        img(scr='logo.gif')
        h2('go away artcontrol')
        p(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        a('about', href='http://brobeur.com/artcontroldrawsyou/about')
        a('contact', href='http://brobeur.com/artcontroldrawsyou/contact') 
        a('blog', href='http://brobeur.com/artcontroldrawsyou/wcmckee.com/wcmckee/output')

    with div():
        attr(cls='header')
        #<img src="smiley.gif" alt="Smiley face" height="42" width="42">
        h1('contact')
        p('email: will@artcontrol.me twitter: art_control')
        p('Recent comments from itwillbemine:')
        #for mine in minels:
            #h1(mine.author_flair_text())
            #p(mine.body)
        
 #   with div(id='author'):
  #     for tum in tumlis:
   #         p(tum)
    
    
    with div(id='body'):
        for mine in minels:
            #h1(mine.created)
            li(mine.body)
            




print contactpage

# <codecell>

os.chdir('contact')

# <codecell>

savcon = open('index.html', 'w')
savcon.write(str(contactpage))
savcon.close()

# <codecell>

dirdir = os.chdir('/var/www/artcontroldrawsyou')

# <codecell>

dirdir

# <codecell>

aboutpage = dominate.document(title='about')
with aboutpage.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with aboutpage:
    with div():
        attr(cls='header')
        #<img src="smiley.gif" alt="Smiley face" height="42" width="42">
        h1('artcontroldrawsyou!')
        img(scr='logo.gif')
        h2('go away artcontrol')
        p(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        a('about', href='https://brobeur.com/artcontroldrawsyou/about')
        a('contact', href='http://brobeur.com/artcontroldrawsyou/contact') 
        a('blog', href='http://brobeur.com/artcontroldrawsyou/wcmckee.com/wcmckee/output')
    with div():
        attr(cls='header')
        #<img src="smiley.gif" alt="Smiley face" height="42" width="42">
        h1('about')
        p('artcontroldrawsyou is a website that takes RedditGetsDrawn data and posts it here.')
        p('artcontrol is not allowed to submit artwork to redditgetsdrawn so this was created')
        #for mine in minels:
            #h1(mine.author_flair_text())
            #p(mine.body)
        
    '''with div(id='author'):
        for tits in titlis:
            h3(tits)
    
    with div(id='body').add(p()):
        for mine in minels:
            #h1(mine.created)
            p(mine.body)
            



'''
print aboutpage

# <codecell>

os.chdir('about')

# <codecell>

aboucr = open('index.html', 'w')
aboucr.write(str(aboutpage))
aboucr.close()

# <codecell>

os.chdir('/var/www/artcontroldrawsyou/')

