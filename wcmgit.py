# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# WCMCKEE GIT
# 
# register form.
# script runs. asks for users name and password. 
# saves this as a hash to login. 
# 
# login: enter username and password. 

# <codecell>

import getpass
import hashlib

# <codecell>

m = hashlib.md5()

# <codecell>

m.update('testing123')

# <codecell>

m.digest()

# <codecell>

paset = raw_input('set password: ')

# <codecell>

print hashlib.md5(paset).hexdigest()

# <codecell>

pa = getpass.getpass()

# <codecell>

# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>


# <h1>pywgit</h1>

# pywgit
# ======
# 
# + Give user, or lookup via user. ty 
# + Downloads repos from github
# 
# This is a python script to download repos from github
# It takes the login name (wcmckee in my case) and downloads the repos of github user (the system login name). It downloads it to the home dir. 
# The program checks if you have local folders that are also on github. It will skip them from downloading from github. 

# <markdowncell>

# This notebook also contains a project using new zealand transport data - cameras from around the country. It is a xml file that is opened and converted to a python dict. It is also converted to a json object, for giggles. 
# I am always working with for loops and lists in python and rarely with dict. This project was perfect to getting me back to using dict. There is no python module for nz transport data so i had to work from xml (json doesn't seem to be an option). I had never converted xml over to python dict so it was a great chance to give it a go.
# During the process I felt I lost lots of work. Maybe it's because I'm working on a enourmous notebook.
# I have problems with getting the xml file and reading it. NZ Transport requires a login to access the data. I couldn't figure out how to get this to work with requests, but managed to run bash and curl then just save the output to file (linkz). 

# <codecell>

from github import Github
import os
import getpass
import git

# <codecell>

theuser = getpass.getuser()

# <markdowncell>

# muliti support for user names - cycle through a list, user input, and get username from login. 

# <codecell>

usergen = raw_input('Github Username: ')

# <codecell>

for us in usergen:
    print us

# <codecell>

#opaz = open('gpaz', 'r')

# <codecell>

#opac = opaz.read()

# <codecell>
pausr = raw_input('Github Password: ')

g = Github(usergen, pausr )

# <codecell>

gitlist = []

# <codecell>

searchpy = g.search_repositories(theuser)

# <codecell>

typy = g.search_users(theuser)

# <codecell>

blehgit = g.search_repositories('reddit')

# <markdowncell>

# oh man, what have i got happening here. This started with a way of downloading repos in bulk from a user and ive started to bring in more github module. Here I am searching repositories on github for reddit. 
# What things could i get it to search for?
# - list
# - search your repos on global to find similar named ones.
# - 

# <codecell>

repolis = []

# <codecell>

print repolis

# <codecell>

for bleh in blehgit:
    repolis.append(bleh)
    #print bleh.full_name

# <markdowncell>

# I'm having a problem with auth! Need to get myself loged in here. 
# Needs better security for logging in. - SSH Key? - hash the password 

# <markdowncell>

# What to do with all the output i am geting from searching. appending it into a list. maybe turn to dict? Make a rest feed? 

# <codecell>

for blzgit in blehgit:
    print blzgit.name

# <codecell>

print blehgit.totalCount

# <codecell>

print typy.totalCount

# <codecell>

print typy

# <codecell>
orgtolookup = raw_input('Github Organization: ')
gepy = g.get_organization(orgtolookup)

# <codecell>

gepy.email

# <codecell>

gepy.blog

# <codecell>

gepy.url

# <codecell>

gepy.created_at

# <codecell>

brorepo.totalCount()

# <codecell>

gepy.public_repos

# <codecell>

gepic = gepy.avatar_url

# <codecell>

gepic

# <codecell>

with open(gepic, 'wb') as handle:
    response = requests.get(jpgcam, stream=True)

    for block in response.iter_content(1024):
        if not block:
            break
        handle.write(block)

# <codecell>

gepy.type

# <codecell>

gepy.raw_data

# <codecell>

print alrepo

# <codecell>

brorepo = gepy.get_repo('linux')

# <codecell>

brorepo.size

# <codecell>

gepy.get_public_members()

# <codecell>


# <codecell>

gepy.location

# <codecell>

searchbleh = g.get_api_status()

# <codecell>

print searchbleh.status
print searchbleh.last_modified

# <codecell>

searchpy.totalCount

# <codecell>

import geopy

# <codecell>

koapi = ('d2b321e45a2041f19551a3f3b223fce0')

# <codecell>

geoloc = geopy.geocoders.GoogleV3()

# <codecell>

address = geoloc.geocode('8 Margaret Street Levin')

# <codecell>

print address

# <codecell>

address.point

# <codecell>

for se in searchpy:
    print se.url

# <codecell>

for repo in g.get_user('wcmckee').get_repos():
    gitlist.append(repo.name)

# <codecell>

os.mkdir('/home/will/github')

# <codecell>

os.chdir('/home/' + 'wcmckee')

# <codecell>

lisdir = os.listdir('/home/wcmckee')
curlist = []
for ls in lisdir:
    #print ls
    curlist.append(ls)

# <codecell>

dlrepo = list(set(gitlist) - set(curlist))

# <codecell>

print dlrepo

# <codecell>


# <codecell>

'''
for gi in gitlist:
    #print gi
    #git.Git().clone("https://github.com/" + theuser + "/" + dlrepo)
    print ("Downloading: " + theuser + "/" + dlrepo)



'''

# <codecell>

from clint.textui import colored

# <codecell>

for gitbl in dlrepo:
        #print ('Downloading - ' + theuser + " - "  + gitbl)
        print (colored.red('Downloading - ' + 'wcmckee' + " - "  + gitbl))
        #git.Git().clone("https://github.com/" + 'wcmckee' + "/" + gitbl)

# <codecell>

def printme( str ):
   "This prints a passed string into this function"
   print str;
   return;

# Now you can call printme function
printme("I'm first call to user defined function!");
printme("Again second call to the same function");

# <codecell>

import requests
import json

# <codecell>

jamft = requests.get('https://raw.githubusercontent.com/leafo/compohub/master/jams/2014.json')

# <codecell>

jamft.text

# <codecell>

compdict = json.loads(jamft.text)

# <codecell>

compjam = compdict[u'jams']

# <codecell>

lencomp = len(compjam)

# <codecell>

import random

# <codecell>

genlin = random.randint(0, lencomp)

# <codecell>

ggj = compjam[genlin]

# <codecell>

jamlis = []

# <codecell>

#for gj in ggj.keys():
    #print gj
    #print ggj[gj]

for jec in range(lencomp):
    print compjam[jec][u'name']
    jamlis.append(compjam[jec][u'name'])

# <codecell>

len(jamlis)

# <codecell>

fujamft = list(set(jamlis))

# <codecell>

lencv = len(fujamft)

# <codecell>

chran = random.randint(0, lencv)

# <codecell>

lencv

# <codecell>

import re

a = 'a b .c???d;;'
chars = [' ']

print re.sub('[%s]' % ''.join(chars), '-', a)

# <codecell>

for fuj in fujamft:
    a = 'a b .c???d;;'
    chars = [' ']

    print re.sub('[%s]' % ''.join(chars), '-', a)
    

# <codecell>

fujamft[chran]

# <codecell>

jamlis

# <codecell>

for mehc in ggj.keys():
    print mehc

# <codecell>

compft = compjam[0:lencomp]

# <codecell>

compft.sort

# <codecell>

dictv = compdict.values()

# <codecell>

dictv.count('id')

# <markdowncell>

# <h1>This is header one</h1>
# 
# This is going to be a 
# 
# new line.
# 

# <codecell>



# <codecell>


# <codecell>


g = Github('wcmckee',  'bill123now!')

# <codecell>

gitlist = []

# <codecell>

searchpy = g.search_repositories(theuser)

# <codecell>

typy = g.search_users(theuser)

# <codecell>

blehgit = g.search_repositories('reddit')

# <markdowncell>

# oh man, what have i got happening here. This started with a way of downloading repos in bulk from a user and ive started to bring in more github module. Here I am searching repositories on github for reddit. 
# What things could i get it to search for?
# - list
# - search your repos on global to find similar named ones.
# - 

# <codecell>

repolis = []

# <codecell>

print repolis

# <codecell>

for bleh in blehgit:
    repolis.append(bleh)
    #print bleh.full_name

# <markdowncell>

# I'm having a problem with auth! Need to get myself loged in here. 
# Needs better security for logging in. - SSH Key? - hash the password 

# <markdowncell>

# What to do with all the output i am geting from searching. appending it into a list. maybe turn to dict? Make a rest feed? 

# <codecell>

for blzgit in blehgit:
    print blzgit.name

# <codecell>

print blehgit.totalCount

# <codecell>

print typy.totalCount

# <codecell>

print typy

# <codecell>


# <codecell>

gepy = g.get_organization('brobeur')

# <codecell>

brorepo = gepy.get_repo('linux')

# <codecell>

brorepo.size

# <codecell>

gepy.get_public_members()

# <codecell>


# <codecell>

gepy.location

# <codecell>

searchbleh = g.get_api_status()

# <codecell>

print searchbleh.status
print searchbleh.last_modified

# <codecell>

searchpy.totalCount
address.point

# <codecell>

for se in searchpy:
    print se.url

# <codecell>

for repo in g.get_user('wcmckee').get_repos():
    gitlist.append(repo.name)

# <codecell>

os.mkdir('/home/will/github')

# <codecell>

os.chdir('/home/' + 'wcmckee')

# <codecell>

lisdir = os.listdir('/home/wcmckee')
curlist = []
for ls in lisdir:
    #print ls
    curlist.append(ls)

# <codecell>

dlrepo = list(set(gitlist) - set(curlist))

# <codecell>

print dlrepo

# <codecell>


# <codecell>

'''
for gi in gitlist:
    #print gi
    #git.Git().clone("https://github.com/" + theuser + "/" + dlrepo)
    print ("Downloading: " + theuser + "/" + dlrepo)



'''

# <codecell>

from clint.textui import colored

# <codecell>

for gitbl in dlrepo:
        #print ('Downloading - ' + theuser + " - "  + gitbl)
        print (colored.red('Downloading - ' + 'wcmckee' + " - "  + gitbl))
        #git.Git().clone("https://github.com/" + 'wcmckee' + "/" + gitbl)

# <codecell>

import geopy
# <codecell>

geoloc = geopy.geocoders.GoogleV3()

# <codecell>

address = geoloc.geocode(raw_input('What address: '))

# <codecell>

print address

# <codecell>


