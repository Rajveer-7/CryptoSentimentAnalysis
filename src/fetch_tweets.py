import tweepy

# Set up Twitter API credentials
consumer_key = 'ssnFddfhZSEiMkAlu9EYCW13C'
consumer_secret = '7fvniApt3htZaFYQDdI40sAfOQYogFYBQdP6lQaMYe2r8yGATU'
access_token = '1800402839593709568-GCV74Vw5d9DZqeYVJ43YoyxZmFBMxc'
access_token_secret = 'nzkmqKYyJ6dvCHnJX9xG8oe8nRo9TnWaz5LJx2bJNbPmG'

# Authenticate
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Fetch tweets
for tweet in tweepy.Cursor(api.search_tweets, q="bitcoin", lang="en").items(10):
    print(tweet.text)
