import numpy as np
from sklearn import linear_model, datasets

diabetes = datasets.load_diabetes()
print(type(diabetes))
features = diabetes.data
targets = diabetes.target
print(features.shape, targets.shape)
dataForTest = -60
data_train = features[:dataForTest]
target_train = targets[:dataForTest]
data_test = features[dataForTest:]
target_test = targets[dataForTest:]

regression1 = linear_model.LinearRegression()
regression1.fit(data_train, target_train)
print(f"coef")
print(regression1.coef_)
print(f"intercept")
print(regression1.intercept_)