# Binance Futures Demo Trading Bot

## Overview

A Python-based trading bot that interacts with Binance Futures Demo/Testnet.

The application supports:

* BUY and SELL orders
* MARKET orders
* LIMIT orders
* STOP_MARKET orders (Bonus Feature)
* Input validation
* Logging
* Error handling
* Command-line interface

---

## Project Structure

trading_bot/

├── bot/

│ ├── client.py

│ ├── orders.py

│ ├── validators.py

│ ├── logging_config.py

│ └── exceptions.py

├── logs/

├── cli.py

├── test_connection.py

├── requirements.txt

└── README.md

---

## Installation

Create virtual environment:

python3 -m venv venv

Activate:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

---

## Configuration

Create a .env file:

API_KEY=your_api_key

API_SECRET=your_api_secret

---

## Usage

### MARKET BUY

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT SELL

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 200000

### STOP MARKET SELL

python cli.py --symbol BTCUSDT --side SELL --type STOP_MARKET --quantity 0.001 --stop-price 100000

---

## Logging

Logs are written to:

logs/trading.log

The log file records:

* Order requests
* Order responses
* Errors

---

## Features

* Binance Futures Demo API integration
* BUY / SELL support
* MARKET orders
* LIMIT orders
* STOP_MARKET orders
* Input validation
* Exception handling
* Logging
* Modular code structure
