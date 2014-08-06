# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# adpost: Reddit script to post data from RedditGetsDrawn and post to artcontroldrawsyou

# <codecell>

import os
import requests
import praw
import json
import time

# <codecell>

os.chdir('/home/wcmckee/rgd')

# <codecell>

opfil = open('userurl.json', 'r')

# <codecell>

userurl = opfil.read()

# <codecell>

usrst = str(userurl)

# <codecell>

print userurl.upper()

# <codecell>

usjson = json.dump(userurl)

