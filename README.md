﻿# GiftCardExchangeHelper


### Overview 
GiftCardExchangeHelper is a tool that helps users find trades on the subreddit /r/giftcardexchange. The GiftCardExchange helper constantly refreshs the new submissions on the subreddit and notifies the user if a new trade post has been create for a giftcard they were looking for.

This project was created because often times, the first person who found a submission on the giftcardexchange subreddit would get to complete the exchange. I wanted to be able to complete exchanges for giftcards I was interested in but didn't want to dedicate myself to refreshing the page and checking on it every few minutes. With this tool, I now know exactly when something I'm interested in is posted so I can have first dibs on the exchange if I want it.

### Examples
* Example Usages, screenshots / links to videos / demos
- high level

### Getting Started
* This project will require:
- Python ?.?
- Praw (https://praw.readthedocs.io/en/latest/)
* The program will look for environment variables for the log in credentials. You will need to configure:
- $VARIABLE_ONE
* How it works???

### Retrospective
* **Lessons Learned**
   - 
* **Limitations and known issues**
   - This tool isn't very scaleable in terms of the number of users.
   - Might be a bug with finding archieved 'reputation' for the Reddit users. 

* **Future Possibilities**
   - Configure the service to run as a single web service that clients can then utilize instead of the clients needing to run the service on their own machines.
   - Create submissions to the subreddit for exchanges the user is attempting to make.
   - I'm sure there is a better way to store user credentials...

### Developer Info
* MIT license
* Uses the SMMRY API to summerize text (https://smmry.com/api)

