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
	opTitle = opTitle.split("[W]")[0]
	print(opTitle)

	if any(string in opTitle for string in hitWords):
		return True
	return False

	# print (submission.title)
	# print (submission.author)
		
	# print (submission.author_flair_text)
	# print (submission.url)
	# if(submission.selftext == ""):
	# 	print (submission.selftext)
	# else:
	# 	print ("There was no selftext!")

	# comments = submission.comments.list()
	# for comment in comments:
	# 	print(comment.body)
	# print ("There are " + str(submission.num_comments) + " comments on this post.")
	# print("\n\n")

	
# TODO: Implement this function
def notifyMaster():
	print("I am supposed to be notifying the master")










## *************************** MAIN *************************** ##
redditClient = praw.Reddit(client_id=clientID,
                     client_secret=clientSecret,
                     password=redditPassword,
                     user_agent='testscript by /u/yrrep',
                     username=redditUsername)
					 
print ("Logged in as user /u/" + redditUsername + "..")

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
		notifyMaster
		validPosts = []

	time.sleep(15)


