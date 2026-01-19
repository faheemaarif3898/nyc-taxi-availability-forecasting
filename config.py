DATA_PATH = "data/yellow_tripdata_2015-01.csv"

TIME_BIN_SIZE = "15min"
FORECAST_HORIZON = 2  # 2 × 15min = 30 minutes

TRAIN_SPLIT_DATE = "2015-11-01"

LAG_FEATURES = [1, 2, 4, 8]

FEATURE_COLUMNS = [
    "dropoff_longitude",
    "dropoff_latitude",
    "lag_1",
    "lag_2",
    "lag_4",
    "lag_8",
    "hour",
    "day_of_week",
    "is_weekend"
]
