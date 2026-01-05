import os
from dotenv import load_dotenv

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

SYMBOL = "BONKUSDC"
TIMEFRAME = "15m"

CAPITAL = 1000
RISK_PER_TRADE = 0.20

TP_PCT = 0.05
SL_PCT = 0.03

USE_TESTNET = True
