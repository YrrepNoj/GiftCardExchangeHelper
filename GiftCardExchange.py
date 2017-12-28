import praw
from AccountInfo import *

r = praw.Reddit(client_id=clientID,
                     client_secret=clientSecret,
                     password=redditPassword,
                     user_agent='testscript by /u/yrrep',
                     username=redditUsername)
					 
print ("Logged in as user /u/" + redditUsername + "..")

print ("Grabbing /r/GiftCardExchange..")
subreddit = r.subreddit("GiftCardExchange")