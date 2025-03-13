import pandas as pd
import numpy as np

data = pd.read_csv("./data/USA_Housing.csv")
data = data.drop("Address", axis=1)

X = data.drop("Price", axis=1).values
y = data["Price"].values

train_size = int(0.7 * len(X))
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

X_train = np.hstack([np.ones((len(X_train), 1)), X_train])

XTX = np.dot(X_train.T, X_train)
XTX_inv = np.linalg.inv(XTX)
XTY = np.dot(X_train.T, y_train)
w = np.dot(XTX_inv, XTY)

var1 = 79248.642454
var2 = 6.002899
var3 = 6.73082
var4 = 3.09
var5 = 40173.07217

def predict_price(var1, var2, var3, var4, var5):
    input_vars = np.array([1, var1, var2, var3, var4, var5])
    return np.dot(input_vars, w)

pred = round(predict_price(var1, var2, var3, var4, var5))
print("Giá nhà dự đoán:", pred)