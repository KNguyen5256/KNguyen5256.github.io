# Part 1
# import the libraries
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score

# Part 2
# load the Iris dataset with pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

X = dataset.values[:,0:4].astype(float)
Y = dataset.values[:,4].astype(str)

# Part 3
# We will randomly split the data into 60% training and 40% test
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=.40)

clf = MLPClassifier(solver='sgd', activation='logistic', 
 learning_rate_init=0.1, learning_rate='constant', max_iter=1000, verbose='true',
 hidden_layer_sizes=(5,))

# 5-fold cross validation
cv_results = cross_val_score(clf, X_train, y_train, cv=5)

msg = "Average Accuracy on cross-validation: %f (%f)" % (cv_results.mean(), cv_results.std())

clf.fit(X_train, y_train)

# Part 4
# Predictions
nn_predictions = clf.predict(X_test)

# Test set accuracy score
final_msg = "Accuracy score of MLP NN: %f" % accuracy_score(y_test, nn_predictions)
print(final_msg)
