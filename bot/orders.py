import logging

class OrderManager:

    def __init__(self, client):
        self.client = client

    def market_order(
        self,
        symbol,
        side,
        quantity
    ):

        logging.info(
            f"MARKET ORDER | "
            f"{symbol} | "
            f"{side} | "
            f"{quantity}"
        )

        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

    def limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        logging.info(
            f"LIMIT ORDER | "
            f"{symbol} | "
            f"{side} | "
            f"{quantity} | "
            f"{price}"
        )

        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

    def stop_market_order(
        self,
        symbol,
        side,
        quantity,
        stop_price
    ):

        logging.info(
            f"STOP_MARKET ORDER | "
            f"{symbol} | "
            f"{side} | "
            f"{quantity} | "
            f"{stop_price}"
        )

        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP_MARKET",
            stopPrice=stop_price,
            quantity=quantity
        )