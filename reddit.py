# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import json

# <codecell>

import PIL
import os

# <codecell>

from PIL import Image

# <codecell>

os.curdir

# <codecell>

os.EX_SOFTWARE

# <codecell>

os.chroot

# <codecell>

os.WNOHANG

# <codecell>

import random

# <codecell>

randNumbz = random.randint(0,80)

# <codecell>

print randNumbz

# <codecell>

for data in range(0,randNumbz):
    print data
    str(data)

# <codecell>

daNumz = str(data)

# <codecell>

print daNumz

# <codecell>

daNumz * randNumbz

# <codecell>

import json

# <codecell>

import flask

# <codecell>

import requests

# <codecell>

urlOpz = requests.get('http://reddit.com/r/redditgetsdrawn.json')

# <codecell>

daNum = dataChild[0]

# <codecell>

from bs4 import BeautifulSoup

# <codecell>

redditSort = BeautifulSoup(selfReddit)

# <codecell>

for link in redditSort.find_all('a'):
    print(link.get('href'))

# <codecell>

redditSort.a

# <codecell>

redditSort.get_text()

# <codecell>

selfReddit = blinkNum['selftext_html']

# <codecell>

blinkNum.popitem()

# <codecell>

blinkNum.values()

# <codecell>

blinkNum = daNum['data']

# <codecell>

dataChild = dataLawl['children']

# <codecell>

print dataLawl

# <codecell>

dataLawl = jawArt['data']

# <codecell>

print dataLawl

# <codecell>

jawArt.viewitems()

# <codecell>

jawArt = json.loads(urlOpz.text)
print jawArt

