# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# nbconv script to convert all ipynb in a folder into html

# <codecell>

from ipython import nbconv

# <codecell>

cd brobeur-web/

# <codecell>

import os

# <codecell>

dadir = '/home/wcmckee/artcontrol-api'

# <codecell>

opnb = os.listdir('/home/wcmckee/artcontrol-api')

# <codecell>

strliz = []

# <codecell>

if '.ipynb' in opz:
    strliz.append(opz)

# <codecell>

for opz in opnb:
    print opz
    if '.ipynb' in opz:
        strliz.append(opz)

# <codecell>

strliz

# <codecell>

nbfol = '/home/wcmckee/brobeur-web/notebook'

# <codecell>

os.chdir(dadir)
strliz

# <codecell>

for bnz in strliz:
    print bnz

# <codecell>

%%bash 
#ipython nbconvert notebook.ipynb
ipython nbconvert --to=latex --template=latex_book --post=pdf pyssh.ipynb

# <codecell>

import envoy
import subprocess

# <codecell>

import IPython.nbconvert

# <codecell>

from IPython.config import Config
from IPython.nbconvert import HTMLExporter,RSTExporter

# <codecell>

os.chdir('/home/wcmckee/brobeur-web/')

# <codecell>

exrst = RSTExporter.from_notebook_node

# <codecell>

for itz in ipy:
    lsr = envoy.run('ipython nbconvert pywgit.ipynb')

# <codecell>

lsr.std_out

# <codecell>

os.chdir(dadir)

# <codecell>

xc = subprocess.check_output('ipython nbconvert')

# <codecell>

xc

# <codecell>

cb = run('ls')

# <codecell>

cb.

