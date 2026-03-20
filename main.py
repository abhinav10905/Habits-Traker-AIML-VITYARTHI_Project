import numpy as np
from data_loader import get_train_test_data
from model import train_model
from evaluate import evaluate_model
def train_and_evaluate():
    """
    Load data, train the model, and evaluate it.
    Returns the trained model.
    """
    X_train, X_test, y_train, y_test = get_train_test_data()
    model = train_model(X_train, y_train)
    print("\nModel trained successfully.")
    evaluate_model(model, X_test, y_test)
    return model
def predict_for_user(model):
    """
    Ask the user for feature values and predict whether they will
    complete the habit today.
    """
    try:
        sleep = float(input("Hours of sleep last night (e.g., 7): "))
        screen = float(input("Screen time in hours yesterday (e.g., 4): "))
        prev_done = int(input("Did you complete this habit yesterday? (1=yes, 0=no): "))
        day = int(input("Day of week (1=Mon ... 7=Sun): "))
    except ValueError:
        print("Invalid input, please enter numeric values.")
        return
    features = np.array([[sleep, screen, prev_done, day]])
    pred = model.predict(features)[0]
    print("\nPrediction result:")
    if pred == 1:
        print("You are LIKELY to complete the habit today ✅")
    else:
        print("You may NOT complete the habit today ❌")
def main():
    model = None
    while True:
        print("\n=== HABIT COMPLETION PREDICTOR (AIML) ===")
        print("1. Train & evaluate model")
        print("2. Predict completion for a new day")
        print("3. Exit")
        choice = input("Enter choice (1-3): ").strip()
        if choice == "1":
            model = train_and_evaluate()
        elif choice == "2":
            if model is None:
                print("Model not trained yet. Training now...")
                model = train_and_evaluate()
            predict_for_user(model)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
if __name__ == "__main__":
    main()
