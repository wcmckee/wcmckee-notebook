# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# wcmckee docker. lets play 

# <codecell>

import docker

# <codecell>

c = docker.Client(base_url='unix://var/run/docker.sock',
                  version='1.12',
                  timeout=10)

# <codecell>

c.images()

# <codecell>

c.get_image('tutum/wordpress')

# <codecell>

c.pull('debian')

# <codecell>

c.inspect_con59bc5d6f4527

