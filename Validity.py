import praw
import logging


hitWords = ["amazon", "amz"]


# Extremely basic check to determine if a post if valid
# TODO: Improve upon this logic
def determineValidity(submission):
	opTitle = submission.title.lower()
	opTitle = opTitle.split("[w]")[0]

	if any(string in opTitle for string in hitWords):
		logging.info("Found a valid post: %s", opTitle)
		return True
	return True