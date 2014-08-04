# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Intercity Python API Development 

# <codecell>

from bs4 import BeautifulSoup
import requests
import pickle

# <codecell>

loadSite = requests.get('http://www.intercity.co.nz/')

# <codecell>

siteData =  loadSite.content

# <codecell>

blehData = siteData.split()

# <codecell>

blehData[0:20]

# <codecell>

siteData.swapcase()

# <codecell>

print siteData.find('a')

# <codecell>

omgSite = BeautifulSoup(siteData)

# <codecell>

linkZite = omgSite.text

# <codecell>


# <codecell>

pickle.dump(linkZite, open('outpuz.txt', 'wb'))

# <codecell>

ls

# <codecell>

dizTxt = open('outpuz.txt', 'r')
dizTxt.read()

# <codecell>

def save(linkZite):
    saveFilz = open('save.txt', 'w')
    
    for linz in linkZite:
        values = line.split()
        savefilz.write(values)
    saveFilz.close()

# <codecell>

print linkZite

# <codecell>

print omgSite.unwrap

# <codecell>

omgSite.encode

# <codecell>

savzSite = omgSite.find_all(id=True)

# <codecell>

sortSite = linkSite[0:30]

# <codecell>

print daSite.next_element

# <codecell>

daSite = sortSite[15]

# <codecell>

linkSite = omgSite.find_all('a')

# <codecell>

saveLinkz = open('htmldoc', 'w')
saveLinkz.write(siteData)
saveLinkz.close()

# <codecell>

openLinkz = open('htmldoc', 'r')
openLinkz.read()

# <codecell>

print omgSite.extract()

# <codecell>

print omgSite.setup

# <codecell>

print omgSite.title

# <codecell>

print omgSite.wrap

# <codecell>

print omgSite.body

# <codecell>

print omgSite.head

# <codecell>

print omgSite.currentTag()

# <codecell>

print omgSite.prettify

# <codecell>


# <codecell>


# <codecell>

print loadSite.url

# <codecell>

beaut = BeautifulSoup(loadSite)

# <codecell>

reTweetz = open('testing.txt', 'w')
reTweetz.write('Fixed request')
reTweetz.close()

# <codecell>

daTweetz = open('testing.txt', 'r')

daTweetz.read()

# <codecell>

print diemLink

# <codecell>

for data in loadSite:
    mixData = BeautifulSoup(data)
    diemLink = mixData.a
    print diemLink
    seioLink = mixData.findAll('a')
    print seioLink
    print(mixData.get_text())
    
    

# <codecell>

mixOpen = open('outputz', 'r')
mixOpen.read()

# <codecell>

%%bash
git add .
git commit -m daTweetz

# <codecell>

%%bash 
git push https://github.com/wcmckee/intercity

# <codecell>

testing = []

# <codecell>

testing.append(daTweetz)

# <codecell>

print testing

# <codecell>

for site in loadSite:
    

# <codecell>

for site in loadSite:
    daLink = []
    dafile = open('output', 'w')
    daLink.append(site)
    inter = BeautifulSoup(site)
    daLink.append(inter)
    geter = inter.text
    daLink.append(geter)
    beuLink = BeautifulSoup(daLink[0])
    print beuLink.a
    
    

# <codecell>

for site in loadSite:
    print'print site'
    inter = BeautifulSoup(site)
    print inter.titlefor site in loadSite:
    print'print site'
    inter = BeautifulSoup(site)
    print inter.title

# <codecell>

for site in loadSite:
    print'print site'
    inter = BeautifulSoup(site)
    print inter.title

# <codecell>


# <codecell>

print inter

# <codecell>

    print inter

# <headingcell level=2>

# Timetable 

# <codecell>

loadUrl = requests.get('http://www.intercity.co.nz/travel-info/timetable/')

# <codecell>

for da in loadUrl:
    print da.title()

# <codecell>

selz = BeautifulSoup(da)

# <codecell>

print selz.title

# <codecell>

timez = BeautifulSoup(loadUrl)

# <codecell>

nakedSite = requests.get('http://nakedbus.com/nz/bus/')

# <codecell>

for naked in nakedSite:
    print naked

# <codecell>


# <codecell>


