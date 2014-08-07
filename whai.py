# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import requests
import bs4

# <codecell>

beurz = requests.get('http://www.centralkids.org.nz/whaihanga-early-learning-centre/')

# <codecell>

beurz

# <codecell>

waitxt = beurz.text

# <codecell>

bswai = bs4.BeautifulSoup(waitxt)

# <codecell>

bswai.find('')

# <codecell>

bswai.title

# <codecell>

bswai.contents

# <codecell>

bswai.link

# <codecell>

bswai.prettify

# <codecell>

bswai.index

# <codecell>


# <codecell>


# <codecell>


