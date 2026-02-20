import pickle

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def div_dataset(df, target):
    X = df.drop(target, axis =1)
    y = df[target]

    le = LabelEncoder()
    y = le.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)


    return X_train, X_test, y_train, y_test, le, scaler


def neural_network(X_train, y_train, num_classes):
    model = Sequential([
        Dense(64, activation="relu", input_shape=(X_train.shape[1],)),
        Dense(32, activation="relu"),
        Dense(num_classes, activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )
    model.fit(
        X_train,
        y_train,
        epochs=25,
        batch_size=16,
        validation_split=0.1
    )
    return model

def model_evaluate(model, X_test, y_test):
    loss, accuracy = model.evaluate(X_test, y_test)
    print("Accuracy:", accuracy)



def save_model(model, filename):
    with open(filename, "wb") as file:
        pickle.dump(model,file)
    print(f"model saved as {filename}")


if __name__ == '__main__':
    df = pd.read_csv("../csv datasets/Fertilizer_NPK_clean.csv")
    target = "Fertilizer Name"

    X_train, X_test, y_train, y_test, le, scaler = div_dataset(df, target)

    num_classes = len(set(y_train))

    nn_model = neural_network(X_train, y_train, num_classes)

    model_evaluate(nn_model,X_test,y_test)

    save_model(nn_model, "../models/fertilizer_model_neural.pkl")