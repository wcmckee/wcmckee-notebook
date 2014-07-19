# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from ftplib import FTP
import os

# <codecell>


def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)

# <codecell>

ftp = FTP('ftp.freshfigure.com')

# <codecell>

ftp.login('ipython', 'PassWord123!')

# <codecell>

upload(ftp, '33561.jpg')

# <codecell>

data = []

# <codecell>

ftp.dir(data.append)

# <codecell>

ftp.quit()

# <codecell>

for line in data:
    print '-', line

# <codecell>

from wand.image import Image

# <codecell>

from bs4 import BeautifulSoup4

# <codecell>

from __future__ import print_function
from urllib2 import urlopen
from wand.image import Image

response = urlopen('http://artcontrol.me/wp-content/uploads/2013/11/wpid-Sketch1521630.png')
try:
    with Image(file=response) as img:
        print('format =', img.format)
        print('size =', img.rotate(90))
finally:
    response.close()

# <codecell>

import gzip

from wand.image import Image

# <codecell>

gz = gzip.open('hello.png.gz')
with Image(filename='hello.png') as img:
    img.format = 'jpeg'
    img.save(file=gz)
gz.close()

# <codecell>

import requests

import json

# <codecell>

openWire = open('wirePIL.ipynb')
wireInfo = openWire.read()


# <codecell>

saveWire = json.loads(wireInfo)

# <codecell>

print(saveWire)

saveWire

# <codecell>

for wire in openWire():
    print wire()

# <codecell>

print(wireInfo)

# <codecell>

wireFormat = wireInfo.format

# <codecell>

wireFormat()

