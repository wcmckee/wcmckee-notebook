# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import geopy

# <codecell>

import requests
import json
import random

# <markdowncell>

# <h1>Python Auckland Transport</h1> 
# 
# This was created during the Hack Auckland: Auckland Transport event in Auckland.
# The first day was spent visiting the vendors and having a play with bitcoin.
# 2nd day was more productive with this python code being typed.
# My plan was to use data from the Auckland Motorcams to detect crashes or events happening on the road. I really should of said this when I got up and talked in front of people about my plan for the event - instead I mentioned the camera feed and how I would like to improve it with more relatient information - including gps of the cameras. 

# <codecell>

atdat = requests.get('https://api.at.govt.nz/v1/public/display/parkinglocations?api_key=433feddb-d4b9-473b-a0c2-ac982a6d78cd')

# <codecell>

atext = atdat.text

# <codecell>

atdict = json.loads(atext)

# <codecell>

atres = atdict['response']

# <codecell>

atlen = len(atres)

# <codecell>

ranpark = random.randint(0, atlen)

# <codecell>

mything = parks()

# <codecell>

for a in mything.getparks():
    print a.keys()

# <codecell>

blen = atres[0:atlen]

# <codecell>

ranitem = test.ranpark()

# <codecell>

thekeys = ranitem.keys()

# <codecell>

thekeys

# <codecell>

listz = []

# <codecell>

for kez in thekeys:
    #print key
    print atres[0][kez]
    listz.append(atres[0][kez])
    

# <codecell>

#dait = atdict.items()

# <codecell>

print listz[3]

# <codecell>

class parks(object):
    def getparks(self):
        return atres
    
    def items(self):
        return atres[0]
    
    def ranpark(self):
        return atres[ranpark]
    
    def genpark(self):
        return (geo.geocode(listz[3]))
    
    def parkloc(self):
        return(atres[ranpark]['address'])
    
    def parkid(self):
        return(atres[renpark]['id'])
    
    def parkcheck():
        return(atres[renpark]['type'])
    
    def parknon(self, inpuz ):
        return(atres[renpark][inpuz])

# <codecell>

geo = geopy.GoogleV3()

# <codecell>

geo.geocode(listz[3])

# <codecell>

olenz = len(listz)

# <codecell>

dachoice = random.randint(0, olenz)

# <codecell>

dachoice

# <codecell>


# <codecell>

park = parks()

# <codecell>

park.genpark()

# <codecell>

park.parkloc()

park.parknon('check')

# <codecell>

park.parkid()

# <codecell>

test.geopark()

# <codecell>

geo.geocode(listz[3])

# <codecell>

listz.sort()

# <codecell>

listz

# <codecell>

#atdict.viewkeys()

# <codecell>

#atrespon = atdict['response']

# <codecell>


# <codecell>

#savdict = open('/home/wcmckee/pyatakl/tests/presets/carparks.json', 'w')
#savdict.write(str(atdict))

# <codecell>

#dait

# <codecell>


# <codecell>

#atdict.values()

# <codecell>

#for d in blen:
#    print d['address']

# <codecell>

#print atext

# <codecell>


# <codecell>

#atke

# <codecell>

#atkey.name

# <codecell>


# <codecell>

getdispl = ('http://api.at.govt.nz/v1/public/realtime/vehiclelocations?api_key=433feddb-d4b9-473b-a0c2-ac982a6d78cd')

# <codecell>

getres = requests.get(getdispl)

# <codecell>

gettx = getres.text

# <codecell>

pajson = json.loads(gettx)

# <codecell>

patza = pajson.keys()

# <codecell>

pajson.keys()

# <codecell>

for i in pajson:
    print i

# <codecell>

patze = pajson['response']['entity'][0]

# <codecell>

patze

# <codecell>

paveh = patze['vehicle']

# <codecell>

pala = paveh['position']

# <codecell>

print pala

# <codecell>

palat = pala['latitude'] 

# <codecell>

palat

# <codecell>

palong = pala['longitude']

# <codecell>

palong

# <codecell>

class busdata(object):
    
    def latdata(self):
        return palat
    def longdata(self):
        return palong
    

# <codecell>

busdata = busdata()

# <codecell>

busdata.longdata()

# <codecell>

longdatas = str(busdata.longdata())

# <codecell>

longdatas

# <codecell>

latdatas = str(busdata.latdata())

# <codecell>

latdatas

# <codecell>

busdata.latdata()

# <codecell>

bothdata

# <codecell>

from geopy.geocoders import GoogleV3
geolocator = GoogleV3()

# <codecell>

address, (longdatas, longitude) = geolocator.reverse(longdatas, latdatas)
print(address, latitude, longitude)

# <codecell>

print geolocator.reverse(longdatas, latdatas)

# <codecell>

print geolocator.geocode(latdatas, longdatas)

# <codecell>

for d in geolocator.geocode(busdata.latdata(), busdata.longdata()):
    print d

# <codecell>

testgeo = geolocator.geocode(-36.921086, 174.80408)

# <codecell>

print testgeo

# <codecell>

import chess

# <codecell>

pos = chess.time

# <codecell>

pos.clock()

# <codecell>

chess.A2

# <codecell>

board = chess.Bitboard()
board.push_san("e4")
board.push_san("e5")
board.push_san("Qh5")
board.push_san("Nc6")
board.push_san("Bc4")
board.push_san("Nf6")
board.push_san("Qxf7")
assert board.is_checkmate()

# <codecell>

assert board

# <codecell>

print board

# <codecell>

chess.WHITE

# <codecell>

board.pawns

# <codecell>

import pprint

# <codecell>

pprint.pprint(board)

# <codecell>

print board

# <codecell>

print board.is_pseudo_legal

# <codecell>

import os

# <codecell>

os.getppid()

# <codecell>

os.geteuid()

# <codecell>

os.access()

# <codecell>

%%HTML
<h1>test</h1>

# <codecell>

getart = requests.get('http://artcontrol.me/mays-paint/')

# <codecell>

getart.json()

# <codecell>


# <codecell>


