# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Hack BroBeur

# <markdowncell>

# python script to make account at centre for logins.

# <codecell>

from github import Github
import os 
import getpass
import git
import time
from clint.textui import colored
import dominate
from dominate.tags import *
import envoy

# <codecell>

zeuser = getpass.getuser()

# <codecell>

g = Github(zeuser, 'blzh123!')

# <codecell>


# <codecell>

gitlist = []

# <codecell>

searchpy = g.search_repositories(zeuser)

# <codecell>

for pya in searchpy:
    print pya.full_name
    wcm = pya.full_name

# <codecell>

for repo in g.get_user('wcmckee').get_repos():
    gitlist.append(repo.name)

# <codecell>

os.mkdir('/home/wcmckee/github')

# <codecell>

lisdir = os.listdir('/home/wcmckee/github/')

# <codecell>

lisdir

# <codecell>

curlis = []

# <codecell>

for lis in lisdir:
    curlis.append(ls)

# <codecell>

dlrepo = list(set(gitlist) - set(curlis))

# <codecell>

print dlrepo

# <codecell>

wafi = time.sleep(5)

# <codecell>

import sh

# <codecell>

import git
repo = git.Repo( '/home/wcmckee/learnpython' )
print repo.git.status()

# <codecell>

assert repo.bare == False

# <codecell>

ycmds = ['git', 'clone', ']

# <codecell>

%%bash
df

# <codecell>

pwd

# <codecell>

import git
os.chdir()

# <codecell>

for gitbl in dlrepo:
    print (colored.red('Downloading - ' + (colored.blue('wcmckee') + ' - ' + gitbl)))
    #git.Git().clone("https://github.com/wcmckee/" + gitbl)
    envoy.run('git clone https://github.com/wcmckee/' + gitbl )
    t = envoy.run('df')
    t.std_out
    print ('Download complete. Waiting 5 secs till the next')
    wafi

# <codecell>

from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('example.com')

# <codecell>

import subprocess

# <codecell>


# <codecell>

%%bash 
source `dirname $0`/github-config.sh

# <codecell>


# <codecell>

cmdrun = ['sudo', 'pip', 'install', 'paramiko']

# <codecell>

supi = envoy.run(cmdrun)

# <codecell>

insvn = subprocess.check_output(cmdrun)

# <codecell>

newlis = []

# <codecell>

for repoz in g.get_user('wcmckee').get_repos():
                        newlis.append(repo.name)

# <codecell>

gitlist

# <codecell>

ls

# <codecell>

cd brobeur-web/

# <codecell>

minex = open(')

# <codecell>

indop = open('index.html', 'r')

# <codecell>


# <codecell>

indop.read()

# <codecell>

from paramiko import SSHClient
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.connect('example.com')

# <codecell>

import envoy

# <codecell>

import clon

# <codecell>


# <codecell>


