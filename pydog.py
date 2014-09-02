# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import socket
hosName = (socket.gethostname())

# <codecell>

print hosName

# <codecell>

import time

# <codecell>

time.strftime("%D,%H:%M")

# <codecell>

print time.strftime("%c")

# <codecell>

import os

# <codecell>

os.getuid()

# <codecell>

import getpass

# <codecell>

userName = getpass.getuser()

# <codecell>

print userName

# <codecell>

import random

# <codecell>

pauseScript = random.randint(0,10)

# <codecell>

time.sleep(pauseScript)

# <codecell>

for user in userName:
    user == ('public'), user ==('public' + hosName)

# <codecell>

print user

# <codecell>

[('hello': '30')]

# <codecell>

users = dict(hunnyb=300, zcat=300, destiny=300)

# <codecell>

print users

# <codecell>

users.viewkeys()

# <codecell>

users.viewvalues()

# <codecell>

#users.popitem()

# <codecell>

users.update()

# <codecell>

users.itervalues

# <codecell>

users.items()

# <codecell>

sorted(users)

# <codecell>

import re
import sys


file = open(sys.argv[2], "r")

for line in file:
    if re.search(sys.argv[1], line):
        print line,

# <codecell>

import re
import sys


file = open(sys.argv[2], "r")

for line in file:
    if re.search(users, line):
        print line,

# <codecell>

from collections import defaultdict

data_dict = defaultdict(list)
for keyStr, load_val in users:
    data_dict[keyStr].append(load_val)

# <codecell>

if data in users:
    print 'hi'

# <codecell>


# <codecell>


