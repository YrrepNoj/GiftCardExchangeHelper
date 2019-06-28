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
        finalString += "Card(s): " + str(self.card)
        finalString += "\nRedditUser: " + str(self.redditUser.name)
        finalString += "\nEmailAddress: " + str(self.emailAddress)
        finalString += "\nphoneNumber: " + str(self.phoneNumber)
        finalString += "\nphoneProvider: " + str(self.phoneProvider)
        return finalString

    def isValidRequest(self):
        if self.card is None or self.card not in searchDict.keys() or self.redditUser is None:
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

        # TODO: This could use a revamp too.. this seems too easy for the user to mess up..
        # Giftcards they are searching for
        if (len(bodyString) > len(searchPhraseString)) and (searchPhraseString.lower() == bodyString[0:8].lower()):
            request.card = bodyString.split(": ")[1].lower()

        # EmailAAddress used to notify the user
        elif (len(bodyString) > len(emailPhraseString)) and (emailPhraseString.lower() == bodyString[0:7].lower()):
            request.emailAddress = bodyString.split(": ")[1].lower()

        # PhoneNumber used to notify the user
        elif (len(bodyString) > len(phoneNumberPhraseString)) and (phoneNumberPhraseString.lower() == bodyString[0:8].lower()):
            request.phoneNumber = bodyString.split(": ")[1].lower()

        # PhoneProvider the user has
        elif (len(bodyString) > len(phoneProviderPhraseString)) and (phoneProviderPhraseString.lower() == bodyString[0:10].lower()):
            request.phoneProvider = bodyString.split(": ")[1].lower()

    messageRequest.mark_read()
    return request