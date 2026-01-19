def train_model(model, train_df, features, target):
    X_train = train_df[features]
    y_train = train_df[target]

    model.fit(X_train, y_train)
    return model
