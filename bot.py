#!/usr/bin/env python


import os
from twitter import Twitter, OAuth, read_token_file
from twitter.cmdline import CONSUMER_KEY, CONSUMER_SECRET

MY_TWITTER_CREDS = os.path.expanduser('~/.twitter_oauth')
oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

t = Twitter(
        auth=OAuth(oauth_token, oauth_secret,
                   CONSUMER_KEY, CONSUMER_SECRET)
        )

#t.statuses.update(status="I'm alive!")

results = t.search.tweets(q="@drdaniellms", result_type="recent")
max_id_str = results['search_metadata']['max_id_str']

for stat in results['statuses']:
    print stat['user']['screen_name'], stat['text']


