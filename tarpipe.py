# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#%%bash
#tar zcvf - /home/public/cam | ssh pi@10.1.1.14 "cat > /home/pi/sativacam.tar.gz"
#sudo rm /home/public/cam/*

# <codecell>

import tarfile
import time
import os

curtime = time.strftime("%d-%b-%Y-%H", time.gmtime())

# <codecell>

tar = tarfile.open(curtime + ".tar.gz", "w:gz")
tar.add("/home/shared/cam", arcname="TarName")
tar.close()
os.rmdir('/home/shared/cam')

# <codecell>


# <codecell>


