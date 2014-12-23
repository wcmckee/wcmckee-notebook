# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# <h1>Auckland Motor Camera</h1>
# 
# This script I run as a cronjob every minute in order to keep the json file updated. 
# It logs into the infoconnect highway cameras. This is a xml file. I am not a big fan of working with xml files. I can do it, but I'd rather json. This gives me access to my 

# <markdowncell>

# **TODO** Add more useful data to the json feed. 

# <codecell>

import subprocess
import requests
import os
import dominate
import xmltodict
import time 
from bs4 import BeautifulSoup
from time import gmtime, strftime
from dominate.tags import *

# <codecell>

os.chdir('/home/wcmckee')

# <markdowncell>

# [nzta](https://infoconnect1.highwayinfo.govt.nz/ "nzta")

# <codecell>

#subprocess.call('curl -k -H "username: williammckee" -H "password: J3e6t8q5y2" -o linkz https://infoconnect1.highwayinfo.govt.nz/ic/jbi/TrafficCameras/REST/FeedService/', shell=True)
# <codecell>
opcon = open('linkz', 'r')

# <codecell>

opcon = open('linkz', 'r')

# <codecell>

data = opcon.read()

# <codecell>


# <codecell>

datadict = xmltodict.parse(data)

# <codecell>

daval = datadict.values()

# <codecell>

daitem = datadict.items()

# <codecell>

daitem.sort()

# <codecell>

daiz = daitem[0][1]

# <codecell>

davalz = daiz.values()[4]

# <codecell>

dalenz = len(davalz)

# <codecell>

davalz[1]['tns:imageUrl']

# <codecell>

chret = []

# <codecell>

for deta in range(0, dalenz):
    print deta
    chret.append(davalz[deta]['tns:imageUrl'])

# <codecell>

os.chdir('/home/wcmckee/akltanpho')

# <codecell>

doc = dominate.document(title='AklMotorCam')

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')
    
    with div():
        attr(cls='header')
        h1('AklMotorCam')
        p(img('imgs/getsdrawn-bw.png', src='imgs/getsdrawn-bw.png'))
        h1('Updated ', strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        #p(panz)
        #p(bodycom)
    
    

with doc:
    with div(id='body').add(ol()):
        for csea in chret:
            #h1(rdz.title)
            p(img(csea, src='%s' % csea))
                
            #print rdz.url
            #if '.jpg' in rdz.url:
            #    img(rdz.urlz)
            #else:
            #    a(rdz.urlz)
            #h1(str(rdz.author))
            
            #li(img(i.lower(), src='%s' % i))

    with div():
        attr(cls='body')
        p('AklMotorCam is open source')
        a('https://github.com/wcmckee/wcmckee')
        #a('https://reddit.com/r/redditgetsdrawn')

print doc

# <codecell>

docakl = doc.render()

# <codecell>

yourstring = docakl.encode('ascii', 'ignore').decode('ascii')

# <codecell>

indfil = ('/home/wcmckee/akltanpho/index.html')

# <codecell>

mkind = open(indfil, 'w')
mkind.write(yourstring)
mkind.close()

# <codecell>

#panz()
for csea in chret:
    #(rdz.title)
    #a(rdz.url)
    #for csb in csea:
        #print rdz.url
        #print (rdz.url)
        #url = csb
    print csea
        #response = requests.get(url)
        #with open(str('/home/wcmckee/getsdrawndotcom/' + csea), 'wb') as out_file:
        #    shutil.copyfileobj(response.raw, out_file)
        #    del response

# <codecell>

chret

# <codecell>

flis = []

# <codecell>

for dinz in datadict.values():
    print (dinz)
    flis.append(dinz)

# <codecell>


# <codecell>

for itz in flis:
    print (itz)

# <codecell>

#savxml = open('/home/will/Desktop/brobeur-static/feeds/aklmcam.json', 'w')
#savxml.write(data)
#savxml.close()

# <codecell>

import json
jsononjz = json.dumps(datadict)
#read the data back in
#newDictionary = json.load(datadict)

# <codecell>

len(jsononjz)

# <codecell>

savcdat = open('/home/wcmckee/brobeur-static/feeds/aklmcam.json', 'w')
savcdat.write(str(jsononjz))
savcdat.close()
print('done uploading feed!')

# <codecell>


# <codecell>


