# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# This is a script to get all notebooks from a github user and download, turning them into rst pages.

# <codecell>

ls

# <codecell>

import os

# <codecell>

listkindy = list(os.listdir(os.getcwd()))

# <codecell>

os.listdir(os.getcwd)

# <codecell>

gdir = ('/home/public/github/')

# <codecell>

os.listdir('/home/public/github/')

# <codecell>

dabook = []

# <codecell>

os.mkdir('notebooks')

# <codecell>

import shutil

# <codecell>

os.getcwd()

# <codecell>

for filz in os.listdir(gdir):
    print filz
    for fila in os.listdir(gdir + filz):
        print fila
        if 'ipynb' in fila:
            dabook.append(os.getcwd() + '/' + filz + '/' + fila)
        #    shutil.copy(fila, '/home/public/notebooks')
            
    

# <codecell>

#for da in dabook:
#    if 'checkpoints' or '.html' in da:
#        dabook.remove(da) # removes too many, filter so it only 
                            #removes files i don't want. if they dont end
    #with .ipynb, i dont want to see them. 

# <codecell>

dabook

# <codecell>


# <codecell>


# <codecell>


