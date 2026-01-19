from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def evaluate_model(model, valid_df, features, target):
    X_valid = valid_df[features]
    y_valid = valid_df[target]

    preds = model.predict(X_valid)

    mae = mean_absolute_error(y_valid, preds)
    rmse = np.sqrt(mean_squared_error(y_valid, preds))

    return mae, rmse
