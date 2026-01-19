def add_target_and_lags(df, horizon, lag_steps):
    df = df.copy()

    df["target_available_next"] = (
        df.groupby(["dropoff_longitude", "dropoff_latitude"])["dropoff_count"]
        .shift(-horizon)
    )

    for lag in lag_steps:
        df[f"lag_{lag}"] = (
            df.groupby(["dropoff_longitude", "dropoff_latitude"])["dropoff_count"]
            .shift(lag)
        )

    df["hour"] = df["time_bin"].dt.hour
    df["day_of_week"] = df["time_bin"].dt.dayofweek
    df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)

    return df.dropna().reset_index(drop=True)
