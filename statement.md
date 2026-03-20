# Habit Completion Predictor – Fundamentals in AIML

## Problem Statement
It is difficult for students to know in advance whether they are likely to complete a particular habit on any given day. However, their behaviour depends on simple factors such as sleep, screen time, previous day performance, and the day of the week.

There is a need for a basic predictive model that, using past data, can estimate whether a habit will be completed today.

## Scope of the Project
This project focuses on a single binary classification task:
- Input: simple daily features (sleep hours, screen time hours, whether the habit was done yesterday, day of week).
- Output: a prediction whether the habit will be completed today (1 = yes, 0 = no).

The model is trained on a small CSV dataset and is intended for demonstration and learning, not for real-life medical or psychological advice.

## Target Users
- Students who want to understand their habit patterns.
- Beginners in AIML who want a simple end-to-end example of:
  - Data loading
  - Model training
  - Evaluation
  - Making predictions

## High-Level Features
- Load dataset from `data/habits_ml.csv`
- Split dataset into training and testing sets
- Train a Logistic Regression classifier
- Evaluate model performance using accuracy and classification report
- Accept user input and predict whether the habit will be completed for that day
