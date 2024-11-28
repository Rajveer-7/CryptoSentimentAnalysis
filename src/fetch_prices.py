from pycoingecko import CoinGeckoAPI
import pandas as pd

def fetch_crypto_prices(coin_id='bitcoin', vs_currency='usd', days=30):
    """
    Fetch historical cryptocurrency prices.

    Args:
        coin_id (str): Cryptocurrency ID (e.g., 'bitcoin').
        vs_currency (str): Currency for price comparison (e.g., 'usd').
        days (int): Number of past days to fetch data for.

    Returns:
        pd.DataFrame: DataFrame with timestamps and prices.
    """
    cg = CoinGeckoAPI()
    data = cg.get_coin_market_chart_by_id(id=coin_id, vs_currency=vs_currency, days=days)
    prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    prices['timestamp'] = pd.to_datetime(prices['timestamp'], unit='ms')
    return prices

# Test the function
if __name__ == "__main__":
    df = fetch_crypto_prices('bitcoin', days=7)
    print(df.head())

if __name__ == "__main__":
    df = fetch_crypto_prices('bitcoin', days=7)
    df.to_csv('../data/bitcoin_prices.csv', index=False)
    print("Data saved to data/bitcoin_prices.csv")
