from bot.client import BinanceTestnetClient

client = BinanceTestnetClient().get_client()

try:
    account = client.futures_account()

    print("SUCCESS")
    print("Connected to Binance Futures Demo")

except Exception as e:
    print("ERROR")
    print(e)