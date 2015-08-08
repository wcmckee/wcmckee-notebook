
# coding: utf-8

# BroBeur Tweet
# 
# Sends tweets for brobeur

# In[53]:

from TwitterFollowBot import TwitterBot
import praw
import random


# In[54]:

my_bot = TwitterBot()


# In[56]:

r = praw.Reddit('brobeurtweet')


# In[57]:

subredz = ['DevBlogs', 'gamedev', 'gamejams', 'Games', 'gaming']


# In[58]:

randsubrepo = random.choice(subredz)


# In[59]:

hashthi = ('#' + randsubrepo)


# In[60]:

rgvz = r.get_subreddit(randsubrepo)


# In[61]:

rgtnew = rgvz.get_new


# In[62]:

ransub = rgvz.get_random_submission()


# In[63]:

rantit = ransub.title


# In[ ]:




# In[64]:

randurl = ransub.url


# In[65]:

my_bot.send_tweet(rantit + ' ' + randurl + ' '  + hashthi)


# In[66]:

my_bot.auto_rt("#gamejams", count=1)


# In[67]:

my_bot.auto_follow("#gamedev", count=1)


# In[ ]:



