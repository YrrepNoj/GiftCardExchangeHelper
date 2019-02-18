import praw
from AccountInfo import *
import logging
import smtplib

def notifyMaster(redditClient, server, validPosts):

    if masterUser:
        sendRedditMessage(redditClient, validPosts)

    # if emailReceiver:
    #     sendEmail(server, validPosts)
    #
    # if phoneProvider and phoneString:
    #     sendTextNotification(server)
    return

def notifyUser(redditClient, user, server, posts):
    if user.redditUser is not None:
        sendRedditMessage(redditClient, posts, redditUser = user.redditUser)

    if user.emailAddress is not None:
        sendEmail(server, posts, user.emailAddress)

    if user.phoneNumber is not None and user.phoneProvider is not None:
        sendTextNotification(server, user.phoneNumber, user.phoneProvider)


def sendEmail(server, validPosts, emailReceiver):
    emailMessage = ""

    # Formatting the email
    for validPost in validPosts:
        emailMessage +=  validPost.title.lower() + ' --- %s\n\n' % validPost.url
    emailText = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (gmailUser, emailReceiver, "ValidPosts", emailMessage)

    try:
        server.sendmail(gmailUser, emailReceiver, emailText)
        logging.info("Sent email with %d new valid posts", len(validPost))
    except:
        logging.warn("Unable to send mail through smtplib server")

    return

def sendTextNotification(server, phoneNumber, phoneProvider):
    phoneText = "A giftcard exchange has been found. Check your reddit account for more information!"

    if phoneProvider == "verizon":
        phoneEmailString = phoneNumber + "@vtext.com"
    else:
        logging.warn("Unsupported phone provider: %s", phoneProvider)
        return

    try:
        server.sendmail(gmailUser, phoneEmailString, phoneText)
        logging.info("Sent text notification")
    except:
        logging.warn("Unable to send mail through smtplib server")

    return

def sendRedditMessage(redditClient, validPosts, redditUser=masterUser):
    finalMessage = ""

    # Formatting the final message for a reddit PM
    for validPost in validPosts:
        finalMessage += '[' + validPost.title.lower() + '] (%s)\n\n' % validPost.url

        # Find and handle the 'rep' for each submission
        gcxRep = findRep(validPost.author)
        for repSubmission in gcxRep:
            finalMessage += "* [" + repSubmission.title.lower() + "] (%s)\n\n" % repSubmission.url
        if len(gcxRep) == 0:
            finalMessage += "* NO REP POSTS FOUND"

    # Send the PM to the user
    redditClient.redditor(redditUser.name).message("ValidPosts",  finalMessage)
    logging.info("Notifying master with %d new valid posts", len(validPosts))
    return

def findRep(redditor):
    repPosts = []

    # Find rep by searching the users post history
    allSubmissions = redditor.submissions.top('all')
    for submission in allSubmissions:
        if submission.subreddit.display_name.lower() == "gcxrep":
            repPosts.append(submission)

    return repPosts
