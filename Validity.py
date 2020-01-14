import logging
from Request import *
from RandomUtil import *





# Extremely basic check to determine if a post is what we are looking for
def determineExchangeType(submission):

    opFlair = submission.link_flair_text
    opTitle = submission.title.lower()
    opTitle = opTitle.split("[w]")[0]

    # Check to ensure the exchange hasn't already been completed
    if opFlair is not None and opFlair.lower() == "closed":
        return ""

    for cardType in searchDict:
        if len(searchDict[cardType]) > 0:
            if any(string in opTitle for string in hitWordDict[cardType]):
                logging.info("Found a valid %s post: %s", cardType, opTitle)
                return cardType

    return ""