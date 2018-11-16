import praw
import time
from AccountInfo import *
from Notify import *
from Validity import *
import logging
import logging.config

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
    for submission in gfxSubreddit.new(limit=10):

        # check to see if this is a new post we haven't seen before
        if submission.created_utc < timeLastRefreshed:
            continue

        if determineValidity(submission):
            validPosts.append(submission)

    if len(validPosts) > 0:
        notifyMaster(redditClient, server, validPosts)
        validPosts = []

    logging.info("Sleeping for 15 seconds..")
    timeLastRefreshed = time.time()
    time.sleep(15)


