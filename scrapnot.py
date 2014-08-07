# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Scrapnot
# ========
# <h2>testing</h2>
# <h3>this is heading 3</h3>
# blah blah blah
# --------------
# 
# 
# This is a scrapbook for exploring some python ideas and modules that i plan to take into other notebooks.
# *Test!*
# What I really need to start doing with these notebooks is a daily notebook. At the end of the week the blog .

# <codecell>

import markdown

# <codecell>

import requests
import json
import xmltodict

# <codecell>

hcpux = requests.get('http://feeds.feedburner.com/HamiltonComputerClub?format=xml')

# <codecell>

cerz = hcpux.text

# <codecell>

hamx = xmltodict.parse(cerz)

# <codecell>

for ha in hamx['rss']['channel']:
    print ha

# <codecell>

staz = hamx['rss']['channel']

# <codecell>

alket = staz.keys()

# <codecell>

len(alket)

# <codecell>

savlis = []

# <codecell>

print alket[3]

# <codecell>

savcal = staz.values

# <codecell>

staz

# <codecell>

savcal()[0:7]

# <codecell>

for ket in alket:
    #print staz[ket]
    print staz['title']
    savlis.append(staz[ket])

# <codecell>

opd = json.dumps(hamxy)

# <codecell>

savopd = open('cpuclu.json', 'w')

# <codecell>

savopd.write(opd)

# <codecell>

savopd.close()

# <codecell>

zopa = open('cpuclu.json', 'r')

# <codecell>

print zopa.read()

# <codecell>

myjson = zopa.read()

# <codecell>

sjson = json.dumps(hamx)

# <codecell>

print sjson

# <codecell>

cerz

# <codecell>

#markdown.to_html_string('*testing one two three*')

# <codecell>

html = markdown.markdown('testing123!')

# <codecell>

print html

# <codecell>

import os

# <codecell>

posfol = ("/home/will/hamiiltoncomputerclub.org.nz/static/posts")
blotil = ("wcmckee")

# <codecell>

rstz = open((blotil + '.rst'), 'w')

# <codecell>


# <codecell>

conv = markdown.markdownFromFile

# <codecell>

import pandoc

# <codecell>

pandoc.PANDOC_PATH = ('/usr/bin/pandoc')

# <codecell>

panout = pandoc.Document.OUTPUT_FORMATS

# <codecell>

for pa in panout:
    print pa

# <rawcell>


# <codecell>

panin = pandoc.Document.INPUT_FORMATS

# <codecell>

panin

# <codecell>

for nai in panin:
    print nai

# <codecell>

nai

# <codecell>

doc = pandoc.Document()
doc.markdown = '''
# I am a tag

*omg this is a test!

[artcontrol](https://artcontrol.me)
'''

# <codecell>

print doc.html

# <codecell>


