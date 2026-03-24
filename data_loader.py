import pandas as pd
from sklearn.model_selection import train_test_split
def load_dataset(path: str = "data/habits_ml.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    return df
def get_train_test_data(path: str = "data/habits_ml.csv"):
    df = load_dataset(path)
    feature_cols = ["sleep_hours", "screen_time_hours", "previous_day_done", "day_of_week"]
    X = df[feature_cols]
    y = df["completed_today"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test
