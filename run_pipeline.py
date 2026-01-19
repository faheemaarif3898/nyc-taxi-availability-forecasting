from src.config import *
from src.data_preparation import load_and_aggregate_data
from src.feature_engineering import add_target_and_lags
from src.model import build_model
from src.train import train_model
from src.evaluate import evaluate_model

def main():
    agg = load_and_aggregate_data(DATA_PATH, TIME_BIN_SIZE)

    df = add_target_and_lags(
        agg,
        horizon=FORECAST_HORIZON,
        lag_steps=LAG_FEATURES
    )

    train_df = df[df["time_bin"] < TRAIN_SPLIT_DATE]
    valid_df = df[df["time_bin"] >= TRAIN_SPLIT_DATE]

    model = build_model()
    model = train_model(
        model,
        train_df,
        FEATURE_COLUMNS,
        "target_available_next"
    )

    mae, rmse = evaluate_model(
        model,
        valid_df,
        FEATURE_COLUMNS,
        "target_available_next"
    )

    print(f"MAE: {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")

if __name__ == "__main__":
    main()
