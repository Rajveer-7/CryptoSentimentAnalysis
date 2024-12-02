import tweepy
import pandas as pd

# Configure API keys in config.py
from config import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Initialize Tweepy
auth = tweepy.OAuthHandler('ssnFddfhZSEiMkAlu9EYCW13C', '7fvniApt3htZaFYQDdI40sAfOQYogFYBQdP6lQaMYe2r8yGATU')
auth.set_access_token('1800402839593709568-GCV74Vw5d9DZqeYVJ43YoyxZmFBMxc','nzkmqKYyJ6dvCHnJX9xG8oe8nRo9TnWaz5LJx2bJNbPmG')
api = tweepy.API(auth)

def fetch_tweets(coin_symbol, limit=100):
    query = f"${coin_symbol} -filter:retweets"
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(limit)
    
    data = [{
        'timestamp': tweet.created_at,
        'text': tweet.full_text,
    } for tweet in tweets]
    return pd.DataFrame(data)

if __name__ == "__main__":
    symbol = input("Enter a coin symbol (e.g., BTC): ")
    tweets = fetch_tweets(symbol)
    print(tweets)
    tweets.to_csv(f"{symbol}_tweets.csv", index=False)


