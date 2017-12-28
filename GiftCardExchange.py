import praw
import time
from AccountInfo import *
from Notify import *
from Validity import *

processedList = []
validPosts = []


## *************************** MAIN *************************** ##
redditClient = praw.Reddit(client_id=clientID,
                     client_secret=clientSecret,
                     password=redditPassword,
                     user_agent='GFX Helper Script',
                     username=redditUsername)
					 
print ("Logged in as user (%s).." % redditUsername)

print ("Grabbing /r/GiftCardExchange..")
gfxSubreddit = redditClient.subreddit("GiftCardExchange")

while(True):
	for submission in gfxSubreddit.new(limit=10):
		if submission.id in processedList:
			continue

		processedList.append(submission.id)
		if determineValidity(submission):
			validPosts.append(submission)

	if len(validPosts) > 0:
		notifyMaster(redditClient, validPosts)
		validPosts = []

	print ("Sleeping for 15 seconds..")
	time.sleep(15)


