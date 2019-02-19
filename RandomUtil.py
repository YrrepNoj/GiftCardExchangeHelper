
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
searchDict = {"amazon": [], "starbucks": [], "googleplay": [], "itunes": []}        #TODO give this dict a better name
# validPostDict = {"amazon": [], "starbucks": [], "googleplay": [], "itunes": []}   //This is being used locally by the main function
