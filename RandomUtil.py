
amazonString = "amazon"
itunesString = "itunes"
googlePlayString = "googlePlay"
stackbucksString = "starbucks"

searchPhraseString = "Search: "
emailPhraseString = "Email: "
phoneNumberPhraseString = "Phone#: "
phoneProviderPhraseString = "Provider: "

amazonHitWords = ["amazon", "amz"]
itunesHitWords = ["itunes", "apple"]
googlePlayHitWords = ["googleplay", "google play", "gplay"]
starbucksHitWords = ["starbucks"]

hitWordDict = {"amazon": amazonHitWords, "starbucks": starbucksHitWords, "googleplay": googlePlayHitWords, "itunes": itunesHitWords}
searchDict = {"amazon": [], "starbucks": [], "googleplay": [], "itunes": []}
# validPostDict = {"amazon": [], "starbucks": [], "googleplay": [], "itunes": []}   //This is being used locally by the main function


clarificationResponse = """ 
Sorry I did not understand your last message. Here is a user's guide so that I can actually be useful to you!
Please cut and paste the bottom part of this response into your next message and replace the parts in brackets `{...}` with whatever options you want.

---
Search: {REQUIRED. Gift card you are searching for. (Ex: Amazon, iTunes, google play, Starbucks)}

Email: {OPTIONAL: Your email address so that we may send you an email notification when we find a matching post}

Phone#: {OPTIONAL: Your phone number so we may send you an SMS notification when we find a matching post}

Provider: {OPTIONAL: Your phone provider so we may send you an SMS notification when we find a matching post}

---"""