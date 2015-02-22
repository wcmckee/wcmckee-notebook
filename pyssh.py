
# coding: utf-8

# <h2>pydigdrop</h2>
# 
# <p>This Python script uses Digital Ocean api services. Importing the features from the Python module digitalocean. Data is pulled and edited. 
# 
# <p>Here is a list of features and ideas.</p>
# <li>Returns user server list. </li>
# <li>Returns info about servers - name/ip/location/status/distro id/distro.</li>
# <li>shutdown, make snapshot, startup all servers (or just one!)</li>
# <li>save info off as json/html</li>
# 
# Plans start as little as $5.00 a month. Servers are charged per the hour. 
# [Digital Ocean]( https://www.digitalocean.com/?refcode=60d1553694c3 )
# 
# 
# 

# TODO:
# - fix login
# 

# In[28]:

import os
import json
import digitalocean


# In[29]:

opcli = open('passwd', 'r')
opapi = open('passap', 'r')


# In[30]:

digclip =  'a24a5636402aaf75d07b774d98591ea3'
digcli = 'dd418a3ea26e7a7ff9e7cd791c0f1b4d'


# In[30]:




# In[31]:

manager = digitalocean.Manager(client_id = digclip, api_key = digcli)


# In[32]:

mydrop = manager.get_all_droplets()


# In[33]:

print mydrop


# In[34]:

dropo = mydrop[0]


# In[35]:

print dropo


# In[36]:

events = dropo.get_events()


# In[37]:

for event in events:
    event.load()
    print event.percentage


# In[38]:

servlis = []


# In[39]:

meip.keys


# In[40]:

for meip in mydrop:
    print meip.name
    servlis.append(meip.name)
    print meip.ip_address
    servlis.append(meip.ip_address)
    print meip.status
    servlis.append(meip.status)
    print meip.image_id
    servlis.append(meip.image_id)
    servlis.append('wcmckee')
    servlis.append(meip.region_id)
    servlis.append(meip.)


# In[41]:

servlis.sort()


# In[42]:

fservlz = list(set(servlis))


# In[43]:

fservlz.sort()


# In[44]:

fservlz


# In[45]:

clisz = []


# In[46]:

thrlis = []


# In[27]:

dictac = zip(olis, servlis)


# In[26]:

dictac


# when converting to a dict why does it only take the first part of dictac.

# In[73]:

dicza = dict(dictac)


# In[74]:

dicza


# In[64]:

jsndigoc = json.dumps(dicza)


# In[66]:

jsndigoc


# In[67]:

digocz = open('/home/will/Desktop/brobeur-static/feeds/digocserv.json', 'w')


# In[68]:

digocz.write(jsndigoc)


# In[69]:

digocz.close()


# In[42]:

servlis


# In[43]:

dropo.ip_address


# In[44]:

dropo.name


# In[45]:

dropo


# In[46]:

droplis = []


# In[47]:

iplis = []


# In[48]:

dropdict = dict{}


# In[49]:

drstr = []


# In[50]:

for dr in mydrop:
    print dr.ip_address
    droplis.append(dr.name)
    droplis.append(dr.ip_address)
    iplis.append(dr.ip_address)
    droplis.append(dr.status)
    print dr.status
    droplis.append(dr.region_id)
    print dr.region_id
    droplis.append(dr.ssh_key_ids)
    droplis.append(dr.id)
    droplis.append(dr)
    print dr.name
    print dr.ssh_key_ids
    print dr.id
    print dr.image_id
    print dr
    drstr.append(dr)


# In[51]:

print droplis


# In[52]:

print drstr


# In[53]:

print iplis


# In[54]:

#!/usr/bin/python
 
# All SSH libraries for Python are junk (2011-10-13).
# Too low-level (libssh2), too buggy (paramiko), too complicated
# (both), too poor in features (no use of the agent, for instance)
 
# Here is the right solution today:
 
import subprocess
import sys
 
HOST= '74.50.51.32'
# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND="uname -a"
 
ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
shell=False,
stdout=subprocess.PIPE,
stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print result


# In[55]:

pwd


# In[40]:

from crontab import CronTab

system_cron   = CronTab()
system_cron.new


# In[50]:

dropo.api_key


# In[51]:

dropo.call_reponse


# In[52]:

dropo.image_id


# In[53]:

dropo.size_id


# In[54]:

dropo.events


# In[55]:

dropo.size_id


# In[56]:

domain = manager.get_all_domains


# In[57]:

print domain


# In[58]:

domain.im_self


# In[59]:

gimg = manager.get_global_images


# In[60]:

gimg


# In[61]:

list(gimg)


# In[96]:

mysnap = manager.get_my_images()


# In[97]:

my_droplets = manager.get_all_droplets()


# In[98]:

for snap in mysnap:
    print snap.name
    print snap.id


# In[73]:

my_droplets = manager.get_all_droplets()
for droplet in my_droplets:
    print droplet
    droplet.power_off()


# In[46]:

for droplet in my_droplets:
    print droplet
    droplet.power_on()


# In[64]:

for droplet in my_droplets:
    print droplet
    print droplet.name


# In[54]:

dropo.power_off()


# In[74]:

dropo.take_snapshot('deb')


# In[82]:

dropo.status


# In[75]:

dropo.rebuild()


# In[55]:

droplet.client_id


# In[67]:

myderp = manager.get_all_regions()


# In[68]:

print myderp


# In[69]:

myderp


# In[70]:

for derp in myderp:
    print derp
    droplis.append(derp.name)
    droplis.append(derp.id)
    print derp.name
    print derp.id


# In[72]:

print droplis


# In[102]:

dropserv = digitalocean.Droplet(client_id=digcli, api_key=apikey, name = 'uburub', region_id=5, image_id=3137635, size_id=66, backup_active=False)
#dropserv.create()
dropserv.Droplet


# In[ ]:



