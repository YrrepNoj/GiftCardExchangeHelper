import praw
from AccountInfo import *
import logging
import smtplib

def notifyMaster(redditClient, validPosts):
    finalMessage = ""

    for validPost in validPosts:
        finalMessage += '[' + validPost.title.lower() + '] (%s)\n\n' % validPost.url

    redditClient.redditor(masterUser).message("ValidPosts",  finalMessage)


    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmailUser, gmailPassword)

        emailText = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (gmailUser, gmailReceiver, "ValidPosts", finalMessage)
        server.sendmail(gmailUser, gmailReceiver, emailText)
        server.close()

        logging.info("Sent email and closed server")
    except:
        logging.warn("Unable to connect to smtplib server")

    logging.info("Notifying master with %d new valid posts", len(validPosts))
    return finalMessage