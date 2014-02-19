#!/usr/bin/env python


from utils import *
from datetime import datetime
from eliza import eliza

t = get_twitter()
therapist = eliza()

while True:
    results = t.search.tweets(q="@drdaniellms", result_type="recent", since_id=get_max_id())
    save_max_id(results['search_metadata']['max_id_str'])
    for result in results['statuses']:
        sender = result['user']['screen_name']
        their_tweet = result['text']

        question = their_tweet.replace("@" + sender, "")
        print "@" + sender + " asked: " + question
        
        reply = therapist.respond(question)
        twitter_response = "@" + sender + " " + reply
        twitter_response = twitter_response.replace("@drdaniellms", "")
        
        t.statuses.update(status=twitter_response)
        print "----- " + twitter_response

