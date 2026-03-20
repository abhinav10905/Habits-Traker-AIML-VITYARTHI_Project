from sklearn.metrics import accuracy_score, classification_report
def evaluate_model(model, X_test, y_test):
    """
    Print basic evaluation metrics for the model.
    """
    y_pred = model.predict(X_test)
    a = accuracy_score(y_test, y_pred)
    print(f"\nModel accuracy: {a:.2f}")
    print("\nClassification report:")
    print(classification_report(y_test, y_pred, digits=2))
