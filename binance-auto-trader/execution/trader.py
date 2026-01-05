
def calculate_quantity(price, capital, risk_pct):
    usd_amount = capital * risk_pct
    return round(usd_amount / price, 0)

def execute_trade(client, symbol, qty, price, tp_pct, sl_pct):
    tp = price * (1 + tp_pct)
    sl = price * (1 - sl_pct)

    print(f"[TRADE] BUY {symbol} qty={qty}")
    print(f"TP={tp:.6f} | SL={sl:.6f}")

    # TESTNET ONLY
    # client.create_order(...)
