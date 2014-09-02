# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# Website for my Mothers yoga class (calling it Clarke Yoga for now) 
# Signup to a one off/weekly/monthly donation payment system.
# All money raised goes towards resorces for early childhood education. 
# 
# tiers of donation rewards

# <codecell>

import os

# <codecell>

import dominate
from dominate.tags import *

# <codecell>

yogind = dominate.document(title='Clarke Yoga')

# <codecell>

with yogind.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with yogind:
    with div():
        attr(cls='header')
        #<img src="smiley.gif" alt="Smiley face" height="42" width="42">
        (h1(a('Clarke Yoga', href='http://brobeur.com/clarkeyoga')))
        img(scr='logo.gif')
        h2('awesome funtime yoga')
        #p(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
        a('about', href='#about')
        a('contact', href='#contact') 
        a('join', href='#join')
        
    with div(id='authors'):
        (a('test', href='https://reddit.com/u/test'))
            
    
    #with div(id='body').add(p()):
        #for i in jplis:
            #(img(i.lower(), src='%s' % i))
            #(a(i.lower(), href='%s' % i))
            
    with div(id='footer'):
        p(a('artcontroldrawsyou is open source', href='https://github.com/wcmckee/wcmckee-notebook'))


            

print yogind

# <codecell>

cyog = ('/var/www/clarkeyoga')

# <codecell>

os.chdir(cyog)

# <codecell>

os.listdir(cyog)

# <codecell>

ophtml = open('index.html', 'w')
ophtml.write(str(yogind))

# <codecell>


# <codecell>


# <codecell>


# <codecell>


