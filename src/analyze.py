# from textblob import TextBlob
# import pandas as pd

# def analyze_sentiment(tweet):
#     analysis = TextBlob(tweet)
#     return analysis.sentiment.polarity

# if __name__ == "__main__":
#     tweets_df = pd.read_csv("BTC_tweets.csv")
#     tweets_df['sentiment'] = tweets_df['text'].apply(analyze_sentiment)
#     tweets_df['sentiment_label'] = tweets_df['sentiment'].apply(
#         lambda x: "positive" if x > 0 else "negative" if x < 0 else "neutral"
#     )
#     print(tweets_df)
#     tweets_df.to_csv("BTC_sentiment.csv", index=False)

from textblob import TextBlob
import pandas as pd
import re
from tqdm import tqdm

# Preprocessing function
def clean_tweet(tweet):
    tweet = re.sub(r"http\S+", "", tweet)  # Remove URLs
    tweet = re.sub(r"@\S+", "", tweet)     # Remove mentions
    tweet = re.sub(r"[^A-Za-z\s]", "", tweet)  # Remove special characters
    return tweet

# Sentiment analysis function
def analyze_sentiment(tweet):
    try:
        analysis = TextBlob(tweet)
        return analysis.sentiment.polarity
    except Exception as e:
        print(f"Error analyzing tweet: {e}")
        return 0

if __name__ == "__main__":
    # Read tweets
    tweets_df = pd.read_csv("BTC_tweets.csv")

    # Clean and filter data
    tweets_df = tweets_df.dropna(subset=['text'])
    tweets_df['text'] = tweets_df['text'].apply(clean_tweet)

    # Progress bar for large datasets
    tqdm.pandas()

    # Analyze sentiment
    tweets_df['sentiment'] = tweets_df['text'].progress_apply(analyze_sentiment)
    
    # Label sentiment
    tweets_df['sentiment_label'] = tweets_df['sentiment'].apply(
        lambda x: "positive" if x > 0 else "negative" if x < 0 else "neutral"
    )

    # Display and save the result
    print(tweets_df)
    tweets_df.to_csv("BTC_sentiment.csv", index=False)

