import praw
import time
from AccountInfo import *

processedList = []
validPosts = []
hitWords = ["amazon", "amz"]


# Extremely basic check to determine if a post if valid
# TODO: Improve upon this logic
def determineValidity(submission):
	opTitle = submission.title.lower()
	opTitle = opTitle.split("[w]")[0]
	print(opTitle)

	if any(string in opTitle for string in hitWords):
		return True
	return True
	
def notifyMaster():
	finalMessage = ""

	for validPost in validPosts:
		finalMessage += '[' + validPost.title.lower() + '] (%s)\n\n' % validPost.url

	redditClient.redditor(masterUser).message("ValidPosts",  finalMessage)











## *************************** MAIN *************************** ##
redditClient = praw.Reddit(client_id=clientID,
                     client_secret=clientSecret,
                     password=redditPassword,
                     user_agent='GFX Helper Script',
                     username=redditUsername)
					 
print ("Logged in..")

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
		notifyMaster()
		validPosts = []

	print ("Sleeping for 15 seconds..")
	time.sleep(15)


