from binance.client import Client
from config.config import *
from data.market_data import get_klines
from indicators.indicators import apply_indicators
from strategy.long_strategy import should_enter_long
from execution.trader import calculate_quantity, execute_trade
from utils.logger import log
import time

# =========================
# Binance Client
# =========================
client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

if USE_TESTNET:
    client.API_URL = "https://testnet.binance.vision/api"

log("Bot started")

# =========================
# Check if already in position
# =========================
def already_in_position(client, symbol):
    account = client.get_account()
    base_asset = symbol.replace("USDC", "").replace("USDT", "")

    for balance in account["balances"]:
        if balance["asset"] == base_asset and float(balance["free"]) > 0:
            return True
    return False

# =========================
# Main Loop
# =========================
while True:
    try:
        for symbol in SYMBOLS:
            df = get_klines(client, symbol, TIMEFRAME)
            df = apply_indicators(df)

            last = df.iloc[-1]
            log(
                f"{symbol} | Close={last['close']:.6f} | "
                f"EMA50={last['ema50']:.6f} | "
                f"StochK={last['stoch_k']:.2f} | "
                f"VolOK={last['high_volume']}"
            )

            if should_enter_long(df):
                if already_in_position(client, symbol):
                    log(f"{symbol} Already in position, skipping trade")
                else:
                    price = last["close"]
                    qty = calculate_quantity(price, CAPITAL, RISK_PER_TRADE)
                    execute_trade(client, symbol, qty, price, TP_PCT, SL_PCT)

        time.sleep(60)

    except Exception as e:
        log(f"ERROR: {e}")
        time.sleep(30)
