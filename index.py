# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from IPython.display import Image

# <codecell>

brobeursite = ('/var/www/')
imgfold = (brobeursite + '/imgs/')
notebookdir = (brobeursite + '/wcmckee-notebook')

# <codecell>

welcometobrobeurstudios = Image(filename= imgfold + 'brobeur.png')

# <codecell>

welcometobrobeurstudios

# <markdowncell>

# Let us list the Notebooks

# <codecell>

import os
import dominate
from dominate.tags import *

# <codecell>

lisnb = []

# <codecell>

for fil in os.listdir(notebookdir):
    #print fil
    if '.html' in fil:
        lisnb.append(fil)

# <codecell>

for nbs in lisnb:
    print nbs

# <codecell>

nbdoc = dominate.document(title='BroBeur Notebooks')
with nbdoc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with nbdoc:
    with div(id='header').add(ol()):
        for nbs in lisnb:
            li(a(nbs, href='/%s' % nbs))

    with div():
        attr(cls='body')
        p('Lorem ipsum..')

print nbdoc

# <codecell>


# <codecell>


