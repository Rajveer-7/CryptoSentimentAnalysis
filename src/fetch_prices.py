from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()

def get_trending_coins():
    coins = cg.get_search_trending()['coins']
    trending = pd.DataFrame([
        {
            'id': coin['item']['id'],
            'name': coin['item']['name'],
            'symbol': coin['item']['symbol'],
            'market_cap_rank': coin['item']['market_cap_rank']
        } for coin in coins
    ])
    return trending

def get_top_volume_coins():
    market_data = cg.get_coins_markets(vs_currency='usd', order='volume_desc')
    volume_data = pd.DataFrame(market_data)
    return volume_data[['id', 'name', 'symbol', 'total_volume', 'current_price']]

if __name__ == "__main__":
    trending_coins = get_trending_coins()
    print("Trending Coins:")
    print(trending_coins)

    volume_coins = get_top_volume_coins()
    print("\nTop Volume Coins:")
    print(volume_coins)
