# GiftCardExchangeHelper


### Overview 
GiftCardExchangeHelper is a tool that helps users find trades on the subreddit /r/giftcardexchange. The GiftCardExchangeHelper constantly refreshs the new submissions on the subreddit and notifies the user if a new trade post has been create for a giftcard they were looking for.

This project was created because when using the /r/giftcardexchange subreddit you often find that the first person who finds a submission would be the one to complete the exchange. I wanted to be able to complete exchanges for giftcards I was interested in but didn't want to dedicate myself to refreshing the page and checking on it every few minutes. With this tool, I now know exactly when something I'm interested in is posted so I can have first dibs on the exchange if I want it.

### Examples
In the first image, you can see someone make a request to the bot. The first message was not useable so the bot responded with a detailed set of instructions of expected input.
![Requests](https://imgur.com/k0YncRh.jpg)


In the second image, you see the result of what the bot provides after we requested to receive submissions inovolving Amazon gift cards. As soon as the bot found a submission that involved an Amazon giftcard we received a message linking us to the post.
![Results](https://imgur.com/tN5VMwK.jpg)


### Getting Started
* This project will require:
   - Python 3.5+
   - Praw (https://praw.readthedocs.io/en/latest/)

### Retrospective
* **Lessons Learned**
   - 
* **Limitations and known issues**
   - Might be a bug with finding archieved 'reputation' for the Reddit users. 
   - Currently only supports verizon for SMS messaging

* **Future Possibilities**
   - Configure the service to run as a single web service that clients can then utilize instead of the clients needing to run the service on their own machines.
   - Create submissions to the subreddit for exchanges the user is attempting to make.
   - I'm sure there is a better way to store user credentials...

### Developer Info
* MIT license4
