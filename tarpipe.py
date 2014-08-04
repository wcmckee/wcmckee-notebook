# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#%%bash
#tar zcvf - /home/public/cam | ssh pi@10.1.1.14 "cat > /home/pi/sativacam.tar.gz"
#sudo rm /home/public/cam/*

# <codecell>

import tarfile

# <codecell>

ls

# <codecell>

tar = tarfile.open("sativacam.tar.gz", "w:gz")
tar.add("/home/sharedcam", arcname="TarName")
tar.close()

# <codecell>

ls -l

# <codecell>

ls

# <codecell>


