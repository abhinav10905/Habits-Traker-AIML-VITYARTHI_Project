# Habits-Traker-AIML-VITYARTHI_Project

## 1. Introduction
This project is a simple **machine learning classifier** that predicts whether a user is likely to complete a habit on a given day based on:
- Hours of sleep
- Screen time
- Whether the habit was done yesterday
- Day of the week

This project is about understanding the basic **AIML** concepts: data preparation, model training, and model evaluation.

---

## 2. Problem Statement
It is hard to maintain daily habits. For instance, lack of sleep, excessive screen time, or irregular behavior could influence the chances of completing a daily habit. Being able to predict daily habit completion could help the user develop self-awareness about their daily behaviors.

This project is based on a small synthetic dataset to predict whether a habit will be completed or not by classifying it as:
- `completed_today = 1` (i.e., the habit is likely completed), or
- `completed_today = 0` (i.e., the habit is not completed).

---

## 3. Objectives
- Develop a **Binary Classification** model using **Logistic Regression**.
- Learn the following:
  - How to load data from a CSV file using pandas.
  - How to split data into training sets.
  - How to evaluate a model using scikit-learn.
  - How to use the model to predict values for new data.
  
---

## 4. Functional Requirements

1. **Load Dataset**
   - Load habit data from `data/habits_ml.csv`.

2. **Train Model**
   - Train a Logistic Regression model to predict `completed_today`.

3. **Evaluate Model**
   - Compute and display accuracy and a classification report on the test set.

4. **Predict for New Day**
   - Accept user input for:
     - `sleep_hours`
     - `screen_time_hours`
     - `previous_day_done`
     - `day_of_week`
   - Output a prediction: likely to complete / not complete.

---

## 5. Non-Functional Requirements

- **Performance**
  - Model should train quickly on a small dataset on a normal laptop.

- **Simplicity**
  - Code is intentionally kept simple and easy to read for beginners.

- **Maintainability**
  - Code is split into multiple modules:
    - `data_loader.py`
    - `model.py`
    - `evaluate.py`
    - `main.py`

- **Extensibility**
  - The dataset and features can be extended in the future with more rows and additional columns.

---

## 6. Dataset Description

File: `data/habits_ml.csv`

Columns:
- `sleep_hours` – number of hours slept in the previous night (float/int).
- `screen_time_hours` – number of hours of screen time yesterday.
- `previous_day_done` – `1` if the habit was completed yesterday, else `0`.
- `day_of_week` – integer from `1` (Monday) to `7` (Sunday).
- `completed_today` – label: `1` if the habit was completed today, else `0`.

The provided dataset is a small synthetic sample used to demonstrate model training.

---

## 7. Model & Methodology

- **Model Type**: Logistic Regression (binary classification).
- **Features Used**:
  - sleep_hours
  - screen_time_hours
  - previous_day_done
  - day_of_week
- **Train/Test Split**:
  - 80% training, 20% testing using `train_test_split` from scikit-learn.
- **Evaluation Metrics**:
  - Accuracy
  - Precision, Recall, F1-score (via classification report)

---

## 8. Implementation Details

### 8.1 Modules

- `data_loader.py`
  - Loads the dataset from CSV.
  - Splits it into training and test sets.

- `model.py`
  - Defines the `train_model` function which trains a Logistic Regression model.

- `evaluate.py`
  - Contains `evaluate_model` to print accuracy and classification report.

- `main.py`
  - Provides a text-based menu:
    - Train & evaluate model
    - Predict completion for a new day
    - Exit

---

## 9. How to Run the Project

### 9.1 Install Dependencies

Make sure you have Python 3 installed.

Install the required libraries:

```bash
pip install numpy pandas scikit-learn
