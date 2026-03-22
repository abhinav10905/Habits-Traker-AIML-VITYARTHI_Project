# Habit Completion Predictor – Fundamentals in AIML

## Problem Statement
It is difficult for students to know in advance whether they are likely to complete a particular habit on any given day. However, their behaviour depends on simple factors such as sleep, screen time, previous day performance, and the day of the week.

There is a need for a basic predictive model that, using past data, can estimate whether a habit will be completed today.

## Scope of the Project
This project will involve a single binary classification task. This includes the following:
- Input: simple daily features like the number of hours slept, the number of hours spent on the screen, if the habit was done the day before, and the day of the week.
- Output: a prediction if the habit will be done today or not (1 = yes, 0 = no).

This model will be trained using a small CSV file and will be used for learning purposes only. This model will not be used for real-life medical or psychological purposes.

## Target Users
- Students who want to understand their habit patterns.
- Beginners in AIML who want a simple end-to-end example of:
  - Data loading
  - Model training
  - Evaluation
  - Making predictions

## High-Level Features
- Load the dataset from the `data/habits_ml.csv` file
- Split the data into training and testing data
- Train a Logistic Regression classifier
- Test the model using the accuracy metric and the classification report
- Accept user input and make a prediction if the habit will be done for the day
