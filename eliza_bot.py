#!/usr/bin/env python


from utils import *
from datetime import datetime
from time import sleep
from eliza import eliza
from twitter.api import TwitterHTTPError

t = get_twitter()
therapist = eliza()

print "** The Eliza Twitter Bot is Now Listening **"
i=0

while True:
    # Run the search and get the results
    i = i+1
    print "Running query #%d" % i
    results = t.search.tweets(q="@drdaniellms", result_type="recent", since_id=get_max_id())
    save_max_id(results['search_metadata']['max_id_str'])
    
    # Loop through the results
    for result in results['statuses']:
        sender = result['user']['screen_name']
        their_tweet = result['text']
        tweet_id = result['id_str']
        
        # Get the exact question
        question = their_tweet.replace("@" + sender, "")
        print "@" + sender + " asked: " + question
        
        # Build the response
        reply = therapist.respond(question)
        twitter_response = "@" + sender + " " + reply
        twitter_response = twitter_response.replace("@drdaniellms", "")
        
        # Post the response to twitter
        try:
            t.statuses.update(status=twitter_response, in_reply_to_status_id=tweet_id)
            print "----- " + twitter_response
        except TwitterHTTPError as t_e:
            # it is common to get a duplicate status error
            print t_e

    # Sleep for 10 seconds to avoid pounding the Twitter API
    # _and_ avoids rate limits
    sleep(10)


