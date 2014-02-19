#!/usr/bin/env python


from utils import *
from datetime import datetime

t = get_twitter()


while True:
    results = t.search.tweets(q="@drdaniellms", result_type="recent", since_id=get_max_id())
    save_max_id(results['search_metadata']['max_id_str'])
    for result in results['statuses']:
        sender = result['user']['screen_name']
        their_tweet = result['text']
        current_time = str(datetime.now())
        t.statuses.update(status="Good morning @" + sender + ". The current time is " + current_time)
        print "Replied to " + sender


