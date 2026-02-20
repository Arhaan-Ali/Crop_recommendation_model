from copyreg import pickle
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import pickle

def explore_data(df):
    print("Number of Instances and Attributes:", df.shape)
    print("\nDataset columns:\n", df.columns)
    print("\nData info:")
    print(df.info())

def checking_removing_duplicates(df):
    count_dups = df.duplicated().sum()
    print("Number of Duplicates:", count_dups)
    if count_dups > 0:
        df.drop_duplicates(inplace=True)
        print("Duplicate values removed")
    else:
        print("No duplicate values found")


def read_in_and_split_data(data, target):
    X = data.drop(target, axis =1)
    y =data[target]
    return train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

def train_random_forest(X_train, y_train):
    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=42,
        n_jobs=-1 )
    model.fit(X_train, y_train)
    return model

def classification_metrics (model, X_train, X_test, y_train, y_test):
    print(f"Training accuracy: {model.score(X_train, y_train) * 100:.2f}")
    print(f"Validation accuracy: {model.score(X_test, y_test) * 100:.2f}")

    y_pred = model.predict(X_test)

    conf_matrix = confusion_matrix(y_test,y_pred)

    plt.figure(figsize=(8,6))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="YlGnBu")
    plt.xlabel("Predicted label")
    plt.ylabel("Actual label")
    plt.title("Confusion matrix")
    plt.show()

    print("Classification report")
    print(classification_report(y_test,y_pred))

def save_model(model, filename):
    with open(filename, "wb") as file:
        pickle.dump(model,file)
    print(f"model saved as {filename}")


if __name__ == "__main__" :
    df = pd.read_csv("../csv datasets/Crop_recommendation.csv")

    explore_data(df)
    checking_removing_duplicates(df)

    target = "label"

    X_train, X_test, y_train, y_test = read_in_and_split_data(df, target)

    dt_model = train_random_forest(X_train, y_train)

    classification_metrics(dt_model, X_train, X_test, y_train, y_test)

    save_model(dt_model, "../models/random_forest_crop_model.pkl")
