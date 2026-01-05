def should_enter_long(df):
    last = df.iloc[-1]

    return (
        last["close"] > last["ema50"] and
        last["high_volume"] and
        last["stoch_k"] > last["stoch_d"] and
        last["stoch_k"] < 20
    )
