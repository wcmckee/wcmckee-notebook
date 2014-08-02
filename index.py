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

# <markdowncell>

# <!DOCTYPE html>
# <html>
#   <head>
#     <title>BroBeur Notebooks</title>
#     <link href="style.css" rel="stylesheet">
#     <script src="script.js" type="text/javascript"></script>
#   </head>
#   <body>
#     <div id="header">
#       <ol>
#         <li>
#           <a href="/wcmgit.html">wcmgit.html</a>
#         </li>
#         <li>
#           <a href="/tlc.html">tlc.html</a>
#         </li>
#         <li>
#           <a href="/digzocean.html">digzocean.html</a>
#         </li>
#         <li>
#           <a href="/tpb.html">tpb.html</a>
#         </li>
#         <li>
#           <a href="/bugit.html">bugit.html</a>
#         </li>
#         <li>
#           <a href="/sortbooks.html">sortbooks.html</a>
#         </li>
#         <li>
#           <a href="/adypost.html">adypost.html</a>
#         </li>
#         <li>
#           <a href="/pyEmailz.html">pyEmailz.html</a>
#         </li>
#         <li>
#           <a href="/nbconv.html">nbconv.html</a>
#         </li>
#         <li>
#           <a href="/master.html">master.html</a>
#         </li>
#         <li>
#           <a href="/pydog.html">pydog.html</a>
#         </li>
#         <li>
#           <a href="/spellcheckin.html">spellcheckin.html</a>
#         </li>
#         <li>
#           <a href="/jsonBehind.html">jsonBehind.html</a>
#         </li>
#         <li>
#           <a href="/hamgar.html">hamgar.html</a>
#         </li>
#         <li>
#           <a href="/markdown.html">markdown.html</a>
#         </li>
#         <li>
#           <a href="/wcmdocker.html">wcmdocker.html</a>
#         </li>
#         <li>
#           <a href="/wirePIL.html">wirePIL.html</a>
#         </li>
#         <li>
#           <a href="/netcafe.html">netcafe.html</a>
#         </li>
#         <li>
#           <a href="/tarpipe.html">tarpipe.html</a>
#         </li>
#         <li>
#           <a href="/ftpWCM.html">ftpWCM.html</a>
#         </li>
#         <li>
#           <a href="/loop.html">loop.html</a>
#         </li>
#         <li>
#           <a href="/rgdsnatch.html">rgdsnatch.html</a>
#         </li>
#         <li>
#           <a href="/metatime.html">metatime.html</a>
#         </li>
#         <li>
#           <a href="/skins.html">skins.html</a>
#         </li>
#         <li>
#           <a href="/getdrawn.html">getdrawn.html</a>
#         </li>
#         <li>
#           <a href="/Untitled0.html">Untitled0.html</a>
#         </li>
#         <li>
#           <a href="/NumPyExplore.html">NumPyExplore.html</a>
#         </li>
#         <li>
#           <a href="/openimg.html">openimg.html</a>
#         </li>
#         <li>
#           <a href="/Untitled1.html">Untitled1.html</a>
#         </li>
#         <li>
#           <a href="/Game Of Thrones.html">Game Of Thrones.html</a>
#         </li>
#         <li>
#           <a href="/pyatakl.html">pyatakl.html</a>
#         </li>
#         <li>
#           <a href="/json.html">json.html</a>
#         </li>
#         <li>
#           <a href="/pyssh.html">pyssh.html</a>
#         </li>
#         <li>
#           <a href="/url redirect.html">url redirect.html</a>
#         </li>
#         <li>
#           <a href="/whai.html">whai.html</a>
#         </li>
#         <li>
#           <a href="/test.html">test.html</a>
#         </li>
#         <li>
#           <a href="/utils.html">utils.html</a>
#         </li>
#         <li>
#           <a href="/karen.html">karen.html</a>
#         </li>
#         <li>
#           <a href="/artcontrol.html">artcontrol.html</a>
#         </li>
#         <li>
#           <a href="/pynztacam.html">pynztacam.html</a>
#         </li>
#         <li>
#           <a href="/wallpapersav.html">wallpapersav.html</a>
#         </li>
#         <li>
#           <a href="/redTube.html">redTube.html</a>
#         </li>
#         <li>
#           <a href="/hackbrobeur.html">hackbrobeur.html</a>
#         </li>
#         <li>
#           <a href="/flask-test.html">flask-test.html</a>
#         </li>
#         <li>
#           <a href="/opche.html">opche.html</a>
#         </li>
#         <li>
#           <a href="/index.html">index.html</a>
#         </li>
#         <li>
#           <a href="/scrapnot.html">scrapnot.html</a>
#         </li>
#         <li>
#           <a href="/reddit.html">reddit.html</a>
#         </li>
#         <li>
#           <a href="/wordpress.html">wordpress.html</a>
#         </li>
#         <li>
#           <a href="/test-wp.html">test-wp.html</a>
#         </li>
#         <li>
#           <a href="/aklmcam.html">aklmcam.html</a>
#         </li>
#         <li>
#           <a href="/webData.html">webData.html</a>
#         </li>
#       </ol>
#     </div>
#     <div class="body">
#       <p>Lorem ipsum..</p>
#     </div>
#   </body>
# </html>

# <codecell>


