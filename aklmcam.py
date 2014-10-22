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

# <markdowncell>

# [nzta](https://infoconnect1.highwayinfo.govt.nz/ "nzta")

# <codecell>

subprocess.call('curl -k -H "username: williammckee" -H "password: J3e6t8q5y2" -o linkz https://infoconnect1.highwayinfo.govt.nz/ic/jbi/TrafficCameras/REST/FeedService/', shell=True)

# <codecell>

opcon = open('linkz', 'r')

# <codecell>

data = opcon.read()

# <codecell>

import xmltodict

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


