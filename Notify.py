import praw
from AccountInfo import *
import logging

def notifyMaster(redditClient, validPosts):
	finalMessage = ""

	for validPost in validPosts:
		finalMessage += '[' + validPost.title.lower() + '] (%s)\n\n' % validPost.url

	print (finalMessage)
	redditClient.redditor(masterUser).message("ValidPosts",  finalMessage)

	logging.info("Notifying master with %d new valid posts", len(validPosts))
	return finalMessage