# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# bugit - github repo bulk download

# <codecell>

from github import Github
import os
import random
import git
import getpass
import socket

# <codecell>

g = Github()

# <codecell>

gitlist = []

# <codecell>

def gitusr(gitn):
    for repo in g.get_user(gitn).get_repos():
        print repo.name
        gitlist.append(repo.name)

# <codecell>

thehost = socket.gethostname()

# <codecell>

theuser = getpass.getuser()

# <codecell>

theuser

# <codecell>

gitusr('wcmckee')

# <codecell>

%%bash 
./job.sh

# <codecell>

os.mkdir('/home/' + theuser + '/github')

# <codecell>

os.chdir('/home/' + theuser + '/github')

# <codecell>

for gi in gitlist:
    print gi
    git.Git().clone('https://github.com/wcmckee/' + gi)

# <codecell>

git.

# <codecell>

import git
git.Git().clone("https://github.com/wcmckee/pyatakl")

# <codecell>

git.Blob()

# <codecell>


# <codecell>


