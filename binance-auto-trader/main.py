from binance.client import Client
from config.config import *
from data.market_data import get_klines
from indicators.indicators import apply_indicators
from strategy.long_strategy import should_enter_long
from execution.trader import calculate_quantity, execute_trade
from utils.logger import log
import time

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

if USE_TESTNET:
    client.API_URL = "https://testnet.binance.vision/api"

log("Bot started")

while True:
    try:
        df = get_klines(client, SYMBOL, TIMEFRAME)
        df = apply_indicators(df)

        if should_enter_long(df):
            price = df.iloc[-1]["close"]
            qty = calculate_quantity(price, CAPITAL, RISK_PER_TRADE)
            execute_trade(client, SYMBOL, qty, price, TP_PCT, SL_PCT)

        time.sleep(60)

    except Exception as e:
        log(f"ERROR: {e}")
        time.sleep(30)
