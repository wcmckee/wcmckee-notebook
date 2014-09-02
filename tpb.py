# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# The Pirate Bay

# <codecell>

from tpb import TPB
from tpb import CATEGORIES, ORDERS

# <codecell>

t = TPB('https://thepriatebay.sx')

# <codecell>

search = t.search('homeland', category=CATEGORIES.VIDEO.MOVIES)

# <codecell>

pagSea = search.page(0).multipage()

for pag in pagSea:
    print pag

# <codecell>

t.top().category(CATEGORIES.VIDEO.MOVIES)

# <codecell>

t.search('24').order(ORDERS.SEEDERS.ASC).page(3)

# <codecell>

search = t.search('breaking bad', category=CATEGORIES.VIDEO.MOVIES)

# <codecell>

search.page(2)

# <codecell>


# <codecell>

search.order(ORDERS.SEEDERS.ASC).multipage()

# <codecell>

breaking = t.search('breaking bad').order(ORDERS.SEEDERS.ASC).page(0)

# <codecell>

for brea in breaking:
    print brea

# <codecell>

blah = t.search('babylon 5').page(0).multipage()

# <codecell>

for bad in blah:
    print bad

# <codecell>


# <codecell>


