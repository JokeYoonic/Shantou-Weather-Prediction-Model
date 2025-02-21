from sklearn.linear_model import LinearRegression

def train_multiple_linear_regression(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model