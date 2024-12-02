from textblob import TextBlob
import pandas as pd

def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    return analysis.sentiment.polarity

if __name__ == "__main__":
    tweets_df = pd.read_csv("BTC_tweets.csv")
    tweets_df['sentiment'] = tweets_df['text'].apply(analyze_sentiment)
    tweets_df['sentiment_label'] = tweets_df['sentiment'].apply(
        lambda x: "positive" if x > 0 else "negative" if x < 0 else "neutral"
    )
    print(tweets_df)
    tweets_df.to_csv("BTC_sentiment.csv", index=False)
