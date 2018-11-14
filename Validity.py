import praw
import logging


hitWords = ["amazon", "amz"]


# Extremely basic check to determine if a post if valid
# TODO: Improve upon this logic
def determineValidity(submission):

    opFlair = submission.link_flair_text
    opTitle = submission.title.lower()
    opTitle = opTitle.split("[w]")[0]

    # Check to ensure the exchange hasn't already been completed
    if opFlair is not None and opFlair.lower() == "closed":
        return False

    # Check to see if any of the hitWords are contained in the title
    if any(string in opTitle for string in hitWords):
        logging.info("Found a valid post: %s", opTitle)
        return True

    return False