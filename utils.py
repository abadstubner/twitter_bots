"""
Utilities to help make the Twitter bot easier to explain.
"""
import os
from twitter import Twitter, OAuth, read_token_file
from twitter.cmdline import CONSUMER_KEY, CONSUMER_SECRET

MAX_ID_FNAME = 'max_id.txt'

def save_max_id(max_id):
    f = open(MAX_ID_FNAME, 'w')
    f.write(max_id)
    f.close()

def get_max_id():
    f = open(MAX_ID_FNAME, 'r')
    s_id = f.read().strip()
    f.close()
    return s_id

def get_twitter():
    MY_TWITTER_CREDS = os.path.expanduser('~/.twitter_oauth')
    oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)
    t = Twitter(
            auth=OAuth(oauth_token, oauth_secret,
                       CONSUMER_KEY, CONSUMER_SECRET)
            )
    return t


