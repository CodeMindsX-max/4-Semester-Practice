"""
Suppose you have a pre-populated dictionary containing student data with the following keys:
{"Attendance","MidScore","LabSocre","InternalScore" (all numbers), and "WillPass"(either 1 or 0).
This dictionary is loaded into a panda data frame where each key becomes a feature. Implement a function that takes three inputs:
1. The data frame containing the student data
2. The name of the target column feature("WillPass")
3. Split data into train test (test size 80 - 20)
The function should split the data into training and testing sets ("x_train","x_test","y_train","y_test") and will return all these four. To handle large data sets efficiently, you must read and process the data frame chunks. You have to split each chunk in such a way that train and test data separable according to size
4. Split chunks in Stratified K Folds and apply cross validation
"""

import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold

def process_data(df, target_col):

    chunk_size = 50   # number of rows per chunk

    X_train_list = []
    X_test_list = []
    y_train_list = []
    y_test_list = []

    # Process dataframe in chunks
    for start in range(0, len(df), chunk_size):

        chunk = df.iloc[start:start + chunk_size]

        X = chunk.drop(columns=[target_col])
        y = chunk[target_col]

        # Train Test Split (80-20)
        x_train, x_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, stratify=y, random_state=42
        )

        X_train_list.append(x_train)
        X_test_list.append(x_test)
        y_train_list.append(y_train)
        y_test_list.append(y_test)

    # Combine all chunks
    x_train = pd.concat(X_train_list)
    x_test = pd.concat(X_test_list)
    y_train = pd.concat(y_train_list)
    y_test = pd.concat(y_test_list)

    # Stratified K-Fold Cross Validation
    skf = StratifiedKFold(n_splits=5)

    for train_index, test_index in skf.split(x_train, y_train):
        X_fold_train = x_train.iloc[train_index]
        X_fold_test = x_train.iloc[test_index]

        y_fold_train = y_train.iloc[train_index]
        y_fold_test = y_train.iloc[test_index]

        print("Fold Train Size:", len(X_fold_train))
        print("Fold Test Size:", len(X_fold_test))

    return x_train, x_test, y_train, y_test

data = {
    "Attendance":[90,80,70,60,50],
    "MidScore":[75,65,55,45,35],
    "LabScore":[80,70,60,50,40],
    "InternalScore":[78,68,58,48,38],
    "WillPass":[1,1,1,0,0]
}

df = pd.DataFrame(data)

x_train, x_test, y_train, y_test = process_data(df,"WillPass")