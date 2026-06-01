import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

class BinanceTestnetClient:

    def __init__(self):

        self.client = Client(
            os.getenv("API_KEY"),
            os.getenv("API_SECRET")
        )

        self.client.FUTURES_URL = (
            "https://demo-fapi.binance.com/fapi"
        )

    def get_client(self):
        return self.client