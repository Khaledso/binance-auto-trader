import ta

def apply_indicators(df):
    df["ema50"] = ta.trend.EMAIndicator(df["close"], 50).ema_indicator()

    df["rsi"] = ta.momentum.RSIIndicator(df["close"], 14).rsi()

    stoch = ta.momentum.StochRSIIndicator(df["close"])
    df["stoch_k"] = stoch.stochrsi_k()
    df["stoch_d"] = stoch.stochrsi_d()

    df["vol_ma"] = df["volume"].rolling(20).mean()
    df["high_volume"] = df["volume"] > df["vol_ma"]

    return df