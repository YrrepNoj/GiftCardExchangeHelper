import logging
from RandomUtil import *



# TODO: This class can run into a lot of issues because of how we are using 'None' in the constructor. Fix.
class Request:
    def __init__(self, card=None, redditUser=None, emailAddress=None, phoneNumber=None, phoneProvider=None):
        self.card = card
        self.redditUser = redditUser
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber
        self.phoneProvider = phoneProvider #TODO Add logic to verify I know how to use this phoneProvider


    def __str__(self):
        finalString = ""
        finalString += "Card(s): " + self.card
        finalString += "\nRedditUser: " + self.redditUser.name
        finalString += "\nEmailAddress: " + self.emailAddress
        finalString += "\nphoneNumber: " + self.phoneNumber
        finalString += "\nphoneProvider: " + self.phoneProvider
        return finalString

    def isValidRequest(self):
        if self.card is None or self.card not in searchDict.keys():
            return False
        if self.redditUser is None:
            return False

        return True

def handleNewRequest(messageRequest):
    logging.info("Received a private message from %s", messageRequest.author)

    bodyList = messageRequest.body.split("\n")
    logging.info("Message from %s: %s", messageRequest.author, bodyList)

    # Go through the text body and generate the request object
    request = Request()
    request.redditUser = messageRequest.author
    for bodyString in bodyList:

        # Giftcards they are searching for
        if (len(bodyString) > len(searchPhraseString)) and (searchPhraseString == bodyString[0:8]):
            request.card = bodyString.split(": ")[1]

        # EmailAAddress used to notify the user
        elif (len(bodyString) > len(emailPhraseString)) and (emailPhraseString == bodyString[0:7]):
            request.emailAddress = bodyString.split(": ")[1]

        # PhoneNumber used to notify the user
        elif (len(bodyString) > len(phoneNumberPhraseString)) and (phoneNumberPhraseString == bodyString[0:8]):
            request.phoneNumber = bodyString.split(": ")[1]

        # PhoneProvider the user has
        elif (len(bodyString) > len(phoneProviderPhraseString)) and (phoneProviderPhraseString == bodyString[0:10]):
            request.phoneProvider = bodyString.split(": ")[1]

    messageRequest.mark_read()
    return request