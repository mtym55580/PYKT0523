from sklearn import datasets
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression

iris = datasets.load_iris()
data = iris.data
target = iris.target

classifiers = [LogisticRegression()]
for clf in classifiers:
    print(f"classifier={clf}")
    score = model_selection.cross_val_score(clf, data, target, cv=3)
    print(score)