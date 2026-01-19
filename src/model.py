import lightgbm as lgb

def build_model():
    return lgb.LGBMRegressor(
        n_estimators=500,
        learning_rate=0.04,
        num_leaves=51,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42
    )
