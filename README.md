# CryptoSentimentAnalysis

## Objective
Analyze cryptocurrency trends by:
1. Identifying trending coins with high trading volume.
2. Scouring Twitter and the web for hype.
3. Performing sentiment analysis to predict potential price movements.

## Features
- Fetch top cryptocurrencies based on trading volume.
- Sentiment analysis on tweets and web content about selected coins.
- Visualization of sentiment trends and price correlation.

## Tech Stack
- Python
- Tweepy
- Pandas
- Matplotlib/Seaborn
- Streamlit (for dashboard)
- TextBlob/VADER (for sentiment analysis)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/CryptoSentimentAnalysis.git
    cd CryptoSentimentAnalysis
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Add your Twitter API keys in `src/config.py`.

## Usage
1. Run `fetch_prices.py` to fetch trending coins and prices.
2. Run `fetch_tweets.py` for tweet sentiment analysis.
3. Run the dashboard using:
    ```bash
    streamlit run dashboard.py
    ```
