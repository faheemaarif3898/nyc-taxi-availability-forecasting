import pandas as pd

def load_and_aggregate_data(csv_path, time_bin_size):
    df = pd.read_csv(csv_path)
    df = df.dropna()

    df["dropoff_dt"] = pd.to_datetime(df["tpep_dropoff_datetime"])
    df["time_bin"] = df["dropoff_dt"].dt.floor(time_bin_size)

    agg = (
        df
        .groupby(["dropoff_longitude", "dropoff_latitude", "time_bin"])
        .size()
        .reset_index(name="dropoff_count")
    )

    return agg.sort_values(
        ["dropoff_longitude", "dropoff_latitude", "time_bin"]
    )
