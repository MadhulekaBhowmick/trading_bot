import argparse
import logging

from bot.client import BinanceTestnetClient
from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)

from bot.logging_config import setup_logger

setup_logger()

parser = argparse.ArgumentParser()

parser.add_argument("--symbol", required=True)
parser.add_argument("--side", required=True)
parser.add_argument("--type", required=True)
parser.add_argument("--quantity", required=True, type=float)
parser.add_argument("--price", type=float)
parser.add_argument("--stop-price", dest="stop_price", type=float)

args = parser.parse_args()

try:

    validate_side(args.side)
    validate_order_type(args.type)
    validate_quantity(args.quantity)

    client = BinanceTestnetClient().get_client()
    manager = OrderManager(client)

    print("\nORDER REQUEST")
    print("-" * 30)

    print(f"Symbol: {args.symbol}")
    print(f"Side: {args.side}")
    print(f"Type: {args.type}")
    print(f"Quantity: {args.quantity}")

    if args.type == "MARKET":

        response = manager.market_order(
            args.symbol,
            args.side,
            args.quantity
        )

    elif args.type == "STOP_MARKET":

        if args.stop_price is None:
            raise ValueError(
                "STOP_MARKET requires --stop-price"
            )

        response = manager.stop_market_order(
            args.symbol,
            args.side,
            args.quantity,
            args.stop_price
        )

    elif args.type == "LIMIT":

        if args.price is None:
            raise ValueError(
                "LIMIT order requires --price"
            )

        response = manager.limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price
        )

    print("\nSUCCESS")
    print("-" * 30)

    print(f"Order ID: {response.get('orderId')}")
    print(f"Status: {response.get('status')}")
    print(f"Executed Qty: {response.get('executedQty')}")
    print(f"Average Price: {response.get('avgPrice')}")
    print(f"Symbol: {response.get('symbol')}")
    print(f"Order Type: {response.get('type')}")
    print(f"Side: {response.get('side')}")

    logging.info(response)

except Exception as e:

    logging.error(str(e))
    print(f"\nFAILED: {e}")