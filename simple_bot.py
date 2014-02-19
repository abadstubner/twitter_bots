#!/usr/bin/env python


from utils import *
from datetime import datetime
from time import sleep

t = get_twitter()

print "** The Eliza Twitter Bot is Now Listening **"

while True:
    # Run the search and get the results
    results = t.search.tweets(q="@drdaniellms", result_type="recent", since_id=get_max_id())
    save_max_id(results['search_metadata']['max_id_str'])

    # Loop through the results
    for result in results['statuses']:
        # Get the user name
        sender = result['user']['screen_name']

        # Build the response and post it
        # Adding the current time to avoid duplicates
        # It _is_ a hack, but it works for the demo
        current_time = str(datetime.now())
        t.statuses.update(status="Good morning @" + sender + ". The current time is " + current_time)
        
        # Log the action so we can follow along
        print "Replied to " + sender

    # Sleep for 10 seconds to avoid pounding the Twitter API
    # _and_ avoids rate limits
    sleep(10)


