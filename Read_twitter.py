#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tweepy
import json
import time


# In[2]:


consumer_secret = 'fuohOf0ULWoxRUwSnKHdSkPQnOMfbcqUqnuTIuLHDfhVV4cgw9'
consumer_key = 'njVxMqP5jTvgf9Gb5OtMX5LRb'
access_token = '287606187-bqNC8diifHjH24SBLTVuifMraKJL4HP43t6FgkiJ'
access_secret = 'CiRWVD8BWAXr8HSigudo6ZOhjT0zmRJZEkS1gDXWcgrdX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


# In[4]:


def read_twitter(tweet_ids):

    counts = 0
    fails=0
    with open('tweets_json.txt','w') as f:
        for tweet_id in tweet_ids:
            counts += 1
            
            try:
                tweet=api.get_status(tweet_id,tweet_mode='extended',)
                print("succes")
                json.dump(tweet._json, f)
                f.write('\n')
            except:
                fails+=1
            time.sleep(1)
    
    return (counts-fails)


# In[ ]:




