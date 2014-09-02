# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# TLC

# <codecell>

import requests
from bs4 import BeautifulSoup

# <codecell>

def geturl():
    return put

# <codecell>

urlReq = requests.get('http://tlcxpress.ac.nz/')

# <codecell>

def dtlc(webaddr):
    return requests.get(webaddr)

def 

# <codecell>

dtlc('http://tlcxpress.ac.nz/').text

# <codecell>

print urlReq.text

# <codecell>

f = open("myfile.txt", "a")


# <codecell>

for data in urlReq:
    #print data
    
    endAte = BeautifulSoup(data)
    
    #print >> f, '>', endAte
    
    #laAte = endAte.get_text()
    #print laAte
    
    liAte = endAte.find_all('a')
    print liAte
    
    cntAte = len(liAte)
    print cntAte
    leAte = endAte.p
    #print leAte
    
    

# <markdowncell>

# That's alot of [] that are totally not needed.

# <codecell>

%%bash

wget \
     --recursive \
     --no-clobber \
     --page-requisites \
     --html-extension \
     --convert-links \
     --restrict-file-names=windows \
     --domains http://www.tlcstudents.ac.nz \
     --no-parent \
         http://www.tlcstudents.ac.nz/home

# <codecell>

openSlc = open('home.html','r')

# <codecell>

opz = open('result','w')
for slc in openSlc:
    print slc[0]

opz.write(slc)
    
    

# <codecell>

endAte = BeautifulSoup(slc)
print endAte
    
laAte = endAte.get_text()
print laAte
    
liAte = endAte.find_all('a')
print liAte
cntAte = len(liAte)
#print cntAte

leAte = endAte.p
#print leAte

# <codecell>

filOpn = open('myfile.txt','r')
blehDat = filOpn.read()

# <codecell>

print blehDat

# <codecell>

blehDat = BeautifulSoup(blehDat)

# <codecell>

classz = blehDat.find_all(["a"])

# <codecell>

print classz.sort

# <codecell>

classString = str(classz)

# <codecell>

print classz[0]

# <codecell>

tlcSite = open('tlchome.html', 'w')

# <codecell>

tlcSite.write(classString)

# <codecell>

tlcSite.close()

# <codecell>

openClass = open('tlchome.html', 'r')

# <codecell>


# <codecell>

openClass.readlines()

# <codecell>

openClass.close()

# <codecell>

last_link = blehDat.find("a")

# <codecell>

print last_link

# <codecell>

blehDat.title

# <codecell>

blehDat.title.name

# <codecell>

blehDat.title.string

# <codecell>

blehDat.text

# <codecell>


# <codecell>


# <codecell>


# <codecell>


