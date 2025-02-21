from sklearn.ensemble import RandomForestRegressor

def train_nonlinear_regression(X, y):
    model = RandomForestRegressor()
    model.fit(X, y)
    return model