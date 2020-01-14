class User:
    def __init__(self, redditUser, request):
        self.redditUser = redditUser
        self.request = request
        self.emailAddress = request.emailAddress
        self.phoneNumber = request.phoneNumber
        self.phoneProvider = request.phoneProvider #TODO Add logic to verify I know how to use this phoneProvider

