import praw
from praw.models import Message
import time
from AccountInfo import *
from Notify import *
from Validity import *
from Request import *
import logging
import logging.config
from User import *


processedList = []
validPosts = []
timeLastRefreshed = 0

## *************************** MAIN *************************** ##
logging.basicConfig(filename="app.log", filemode="w", format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s", level=logging.INFO, datefmt="%d-%b-%y %H:%M:%S")

redditClient = praw.Reddit(client_id=clientID,
                           client_secret=clientSecret,
                           password=redditPassword,
                           user_agent='GFX Helper Script',
                           username=redditUsername)

logging.info("Logged in as user (%s).." % redditUsername)

logging.info("Grabbing /r/GiftCardExchange..")
gfxSubreddit = redditClient.subreddit("GiftCardExchange")


logging.info("Connecting to smtplib server")
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(gmailUser, gmailPassword)
except:
    logging.error("Unable to connect to smtplib server")

while (True):

    validPostDict = {"amazon": [], "starbucks": [], "googleplay": [], "itunes": []}
    # Process any new private messages we have received to see if another user wants use to look up exchanges for them
    for item in redditClient.inbox.unread(limit=None):
        if isinstance(item, Message):
            request = handleNewRequest(item)
            if request.isValidRequest():
                logging.info("Incrementing the searchDict for '%s' after receiving a new request from '%s'", request.card, item.author.name)
                logging.info("The request object: " + request.__str__())

                user = User(item.author, request)
                searchDict[request.card].append(user)

    for submission in gfxSubreddit.new(limit=10):
        # check to see if this is a new post we haven't seen before
        if submission.created_utc < timeLastRefreshed:
            continue

        postType = determineExchangeType(submission)
        if postType != "":
            validPostDict[postType].append(submission)


    for cardType in validPostDict:
        if len(validPostDict[cardType]) > 0:
            for user in searchDict[cardType]:
                notifyUser(redditClient, user, server, validPostDict[cardType])

    logging.info("Sleeping for 15 seconds..")
    timeLastRefreshed = time.time()
    time.sleep(15)


