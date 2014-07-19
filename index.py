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

# <codecell>

lisnb = []

# <codecell>

for fil in os.listdir(notebookdir):
    #print fil
    if '.html' in fil:
        lisnb.append(fil)

# <codecell>

lisnb

# <codecell>


