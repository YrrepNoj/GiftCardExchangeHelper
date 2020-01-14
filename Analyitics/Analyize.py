import praw
import datetime
import time
from datetime import datetime
from AccountInfo import *


processedList = []

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
	newCount = 0

	for submission in gfxSubreddit.new(limit=100):
		if submission.id in processedList:
			break
		processedList.append(submission.id)	
		newCount += 1

	activity = open("ActivityLog.txt", "a")
	activity.write("Time: (%s). Posts: (%d)\n" % (str(datetime.now()), newCount))	
	activity.close()

	print ("Sleeping for 15 minutes")
	time.sleep(900)
