import praw
from AccountInfo import *

def notifyMaster(redditClient, validPosts):
	finalMessage = ""

	for validPost in validPosts:
		finalMessage += '[' + validPost.title.lower() + '] (%s)\n\n' % validPost.url

	print (finalMessage)
	redditClient.redditor(masterUser).message("ValidPosts",  finalMessage)

	return (finalMessage)