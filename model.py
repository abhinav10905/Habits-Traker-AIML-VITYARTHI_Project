from sklearn.linear_model import LogisticRegression
def train_model(X_train, y_train) -> LogisticRegression:
    """
    Train a Logistic Regression model on the habit dataset.
    """
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model
