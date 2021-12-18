# Lab Sheet

![[Lab 13 Supervised Learning and Logistic Regression.pdf]]

# Answers
1) I would use a logistical regression model with a lot of features (like if the email contains some specific words, or if the sender's email is known to be fraudulent etc.) and make a model that takes in consideration all of these variables.
2) 
	-    0.47 | 0.93 | 0.1
	-    $F1 = \frac{(2\bullet0.93\bullet0.96)}{0.93+0.96} = \frac{1.79}{1.89} = 0.95$
	-    (0.49, 0,51), (0.95, 0.05), (0.11, 0.89)
	-    The third and the second

3) 

```jupyter
from sklearn.datasets import make_classification
X,Y=make_classification(n_samples=20,n_features=1,n_classes=2,n_clusters_per_class=1,
flip_y=0.03,n_informative=1,n_redundant=0,n_repeated=0)
print(X)
print("\n")
print(Y)
print("\n")
from matplotlib	import pyplot as plt
plt.scatter(X,Y,cmap = 'Blue')
plt.show()
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20)
print(X_train)
print("\n")
print(Y_train)
print("\n")
print(X_test)
print("\n")
print(Y_test)
print("\n")
from sklearn.linear_model import LogisticRegression
logistic_regression_model=LogisticRegression()
logistic_regression_model.fit(X_train,Y_train)
prediction=logistic_regression_model.predict(X_test)
print(prediction)
print("\n")
print(Y_test)
print("\n")
coeff=logistic_regression_model.coef_
print(coeff)
print("\n")
intercept=logistic_regression_model.intercept_
print(intercept)
print("\n")
from sklearn.metrics import	confusion_matrix
print(confusion_matrix(Y_test,prediction))
print("\n")
from sklearn.metrics import	accuracy_score
model_accuracy=accuracy_score(Y_test,prediction)
model_accuracy