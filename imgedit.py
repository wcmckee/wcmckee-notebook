# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <h1>imgedit</h1>

# <markdowncell>

# This is a project dealing with the website http://centralkids.org.nz.
# I just want to play with it and see what I can do.
# 
# My first step was downloading the site with wget.
# Adding source control, a new external folder to hold a new website/data/notebooks (keep everything clean and build it up), and a ipython notebook/py file that is used to generate the new site. This notebook currently sits in the repo main dir. 
# 
# The script starts by looking at the main dir and filtering the list of folders and files. I do this many times. 
# 
# Over use of lists. Attempting to use more dict.
# 
# 

# <markdowncell>

# Ideas for
# 
# dominate 

# <markdowncell>

# TODO:
# 
# makes folder - centre kindy - had folder of all kindys - inside of this is static blog - 
# 
# linked to main centre kindy blog. 
# 
# admin - roll
# 
# generates a list of students at centre
# 
# generates a list of teachers at centre
# 
# warnings on ratio
# 
# communication with other centre
# 
# each centre has static page with info about each centre - open hours, list of teachers, job/opotunity, 
# 
# central kids os: linux debian 7
# 
# os locationed inside thieir folder. This is based off Debian7 (root7.tar.gz install7). All computers have this os. Unable to access certain areas outside of os (rsa ssh from inside central kids os into secure server)
# 
# Ways to keep privacy safe
# 
# i have no idea what im doing, but i hope something works!

# <codecell>

from IPython.display import display, Javascript

def markdown_below():
    display(Javascript("""
    IPython.notebook.insert_cell_below('markdown')
    """));

markdown_below()

# <codecell>

from shutil import make_archive

# <markdowncell>


# <codecell>

import os
import re

# <codecell>

whaidir = ('/var/www/whai')

# <codecell>

listkindy = list(os.listdir(whaidir))

# <codecell>

for kin in listkindy:
    print kin

# <codecell>

for kin in listkindy:
    print kin

# <codecell>

listen = []

# <codecell>

savlis = []

# <codecell>

for kin in listkindy:
    if 'kinder' in kin:
        print kin
        listen.append(kin)

# <codecell>


# <codecell>

for kin in listkindy:
    if 'early' in kin:
        print kin
        listen.append(kin)

# <markdowncell>


# <codecell>

#listen.sort()

# <codecell>

for itz in listen:
    if 'html' in itz:
        print itz
        listen.remove(itz)

# <codecell>

import re

# <codecell>

for lix in listen:
    print lix
    savlis.append(geopy.Location(lix))

# <codecell>

s = 'abc-d-ef ghijk'
s1 = s.replace('-', ' ')

# <codecell>

splist = []

# <codecell>

oplist = []

# <codecell>

for spz in listen:
    savall = open('/home/public/' + spz + '/index.html')
    oplist.append(savall.read())
    #oplist.append(spz)
    

# <codecell>

for iz in listen:
    print iz
    splist.append(iz.replace('-', ' '))
    

# <codecell>

caplis = []

# <codecell>

for caz in splist:
    caplis.append(str.capitalize(caz))

# <codecell>

chars = []

# <codecell>

for line in caplis:
    for c in line:
        chars.append(c)

# <codecell>

for car in chars:
    print car

# <codecell>

geolz = []

# <codecell>

for iz in caplis:
    print iz
    geolz.append(geopy.Location(iz))
    

# <codecell>

openhtm = open('index.html', 'r')

# <codecell>

mydoc = str(openhtm.read())

# <codecell>

mydoc

# <codecell>

from bs4 import BeautifulSoup

# <codecell>

cent = BeautifulSoup(mydoc)

# <codecell>

ctent = cent.title

# <codecell>

pcent = cent.find_all('p')

# <codecell>

cenimg = cent.findAll('img')

# <codecell>

import dominate
from dominate.tags import *

# <codecell>

dominate.tags

# <codecell>

allcent = dominate.document(title='central')

# <codecell>

with allcent.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', scr='script.js')

# <codecell>

(pcent)

# <codecell>

for pcz in pcent:
    print pcz

# <codecell>

for cen in cenimg:
    print cen

# <codecell>

with allcent:
    with div(id='header').add(ol()):
        for i in listen:
            li(a(i.title(), href='/%s' % i))

    with div():
        attr(cls='body')
        #p(str(pcent))
        for pcz in pcent:
            p(pcz)
        #p(str(pcent))

# <codecell>

print allcent

# <codecell>

mkhtm = open('test.html', 'w')
mkhtm.write(str(splist))
mkhtm.close()

# <codecell>

cendict = {}

# <codecell>

mynum = 0

# <codecell>

splist

# <codecell>

for iza in splist:
    if 'kindergarten' or 'centre' in iza:
        cendict.update({iza: mynum})
        mynum = (mynum + 1)

# <codecell>

cendict

# <codecell>

import re

# <codecell>

a = re.sub('[.!,;]', 'bssdg!aassada.', a)

# <codecell>

re.sub()

# <codecell>

s = 'A.B-!C?'
print s.translate(None, '" "'.join('-'))

# <codecell>

import string

specials = '-"/.' #etc
trans = string.maketrans(specials, ' '*len(specials))
#for line in file
cleanline = 'test'.translate(trans)

# <codecell>

s = 'abc-d-ef ghijk'
s1 = s.replace('-', ' ')

# <markdowncell>

# dict.
# kindergartens: list all the kindergarten, centre: list all centre

# <codecell>

os.listdir('/home/public/whai/imgs')

# <markdowncell>

# make folder of kindyname-index.html

# <codecell>

os.removedirs('/home/public/central-test')

# <codecell>

cents = ('/home/public/central-test/centres')

# <codecell>

os.mkdir('imgs')

# <codecell>

os.listdir('/home/public/whai/imgs/')

# <codecell>

osliz = []

# <codecell>

os.chdir(cents)

# <markdowncell>

# this makes the centre folders

# <codecell>

for oubz in listen:
    os.mkdir(oubz)

# <codecell>

for oslis in listen:
    print oslis
    
    osliz.append(os.listdir('/home/public/whai/' + oslis))

# <codecell>

osliz

# <codecell>

finlis = []

# <codecell>

for osl in osliz:
    finlis.append(osl)
    if 'index' in osl:
        print 'yes!'
    

# <codecell>

indlis = []

# <codecell>

for fin in finlis:
    if 'index' in fin:
        indlis.append(fin)
        

# <codecell>

telis = []

# <codecell>

for f in finlis:
    #print f
    for te in f:
        print te
        if 'index.html' or 'wp' in te:
            telis.append(te)
            

# <codecell>

filis = []

# <codecell>

for tez in telis:
    if '.' in tez:
        filis.append(tez)
        

# <codecell>

filis

# <codecell>

%%bash 
#!/bin/bash

# Add a user to the system, if they don't already exist. This script must be run as root.
# If the user exists in Stanford LDAP, we'll user their Stanford-wide UID. Otherwise,
# they get assigned a local UID that's outside the Stanford UID range.

# Copyright 2012 by Gunnaer Schaefer (gsfr@stanford.edu)  and Bob Dougherty (bobd@stanford.edu)

if [ ! $1 ]; then
    echo "Usage: $0 SUNetID"
    exit 999
fi

if id $1 &> /dev/null ; then
    if [ -z "`groups $1 | grep ipython`" ]; then
        /usr/sbin/adduser $1 ipython
    else
    	echo "User $1 already exists and is a member of the ipython group."
    fi
    exit 1
else
    ldapinfo=$(ldapsearch -x -h ldap.stanford.edu uid=$1)
    uid_num=$(echo "$ldapinfo" | grep uidNumber); uid_num=${uid_num##*: }
    firstname=$(echo "$ldapinfo" | grep suDisplayNameFirst); firstname=${firstname##*: }
    lastname=$(echo "$ldapinfo" | grep suDisplayNameLast); lastname=${lastname##*: }
    if [ -z $uid_num ]; then
        echo "User $1 does not exist in LDAP. Assigning a local UID."
        uid_num=$((`(echo 69999; cut -d':' -f3 /etc/passwd) | sort -n | tail -1` + 1))
    fi
    echo "Creating user $1 ($firstname $lastname, uid = $uid_num)..."
    /usr/sbin/adduser --disabled-password --uid $uid_num --gecos "$firstname $lastname" $1
    /usr/sbin/adduser $1 ipython
fi

# <codecell>


# <codecell>

os.chdir('/home/public/')

# <codecell>

os.mkdir('central-test')

# <codecell>

os.chdir('central-test')

# <codecell>

import delican

# <codecell>

import tarfile

# <codecell>

mytar = tarfile.TarFile('/home/public/central-test/centralblog.tar.gz')

# <codecell>

import shutil

# <codecell>

shutil.copytree('/home/public/central-test/central/' '/home/public/central-test/waipahihi-kindergarten/')

# <codecell>

for ipz in os.listdir('/home/public/central-test'):
    #print ipz
    cfpath, cfname = os.path.split(os.getcwd())
    print cfname
    

# <codecell>

import dominate

# <codecell>

dominate.tags(p('test'))

# <codecell>

current_folder_path, current_folder_name = os.path.split(os.getcwd())

# <codecell>

current_folder_name

# <codecell>

centar = '/home/public/central.tar.gz'
centes = '/home/public/central-test/'

# <codecell>

for imz in os.listdir('/home/public/central-test'):
    print imz
    os.chdir(imz)
    shutil.copyfile(centar, '/home/public/central-test/whaihanga-early-learning-centre/test.tar.gz')

# <codecell>

os.urandom(512)

# <codecell>

import os

archive_name = os.path.expanduser(os.path.join('~', 'central'))
root_dir = os.path.expanduser(os.path.join('~', 'central-test/central'))
make_archive(archive_name, 'gztar', root_dir)

# <codecell>

shutil.copyfile('/home/public/central.tar.gz', '/home/public/central-test/whaihanga-early-learning-centre/test.tar.gz')

# <codecell>

cendict

# <markdowncell>

# Parse the blog, because - why not?

# <codecell>

import feedparser

# <codecell>

cenblog = feedparser.parse('http://feeds.feedburner.com/CentralKidsKindergartens')

# <codecell>

lenblog = len(cenblog['entries'])

# <codecell>

lenblog

# <markdowncell>

# I want to write the blog posts to html file with dominate. 
# it needs to take the print cen['title', ['updated'], ['summary_details'] etc... and make it be be formated nice in html.

# <codecell>

blogplz = dominate.document(title='Centre Kids News')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with blogplz:
    with div(id='header').add(ol()):
        for cen in cenblog['entries']:
            #print cen
            print cen['title']
            li(a(cen['title'](), href='/%s.html' % cen['title']))
            print cen['updated']
            li(a(cen['updated'](), href='/%s.html' % cen['updated']))
            print cen['summary_detail']['value']
            li(a(cen['summary_detail'](), href='/%s.html' % cen['summary_detail']))
            print cen['author']
            li(a(cen['author'](), href='/%s.html' % cen['author']))
        #for i in ['home', 'about', 'contact']:
        #    li(a(i.title(), href='/%s.html' % i))

    with div():
        attr(cls='body')
        p('Lorem ipsum..')

print blogplz

# <codecell>

tilis = []

# <codecell>

tilis

# <codecell>

with allcent:
    with div(id='header').add(ol()):
        for i in listen:
            li(a(i.title(), href='/%s' % i))

    with div():
        attr(cls='body')
        #p(str(pcent))
        for cen in cenblog['entries']:
            #print cen
            print cen['title']
            tilis.append(cen['title'])
            print cen['updated']
            tilis.append(cen['updated'])
            print cen['summary_detail']['value']
            tilis.append(cen['summary_detail']['value'])
            print cen['author']
            tilis.append(cen['author'])

    #print cen['value']
        #p(str(pcent))
        
    with div():
        fo

# <codecell>

def getallpost():
    for cen in cenblog['entries']:
        #print cen
        print cen['title']
        print cen['updated']
        print cen['summary_detail']['value']
        print cen['author']

    #print cen['value']

# <codecell>

getallpost()

# <codecell>

cenblog['entries']

# <markdowncell>


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


