# -*- coding: utf-8 -*-
"""Credit_Card_Fraud_Detection_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1raZdOhrjfFGJDVzSqgzx-4zV9q_sE6l7
"""

import pandas as pd # data processing
import numpy as np # working with arrays
import matplotlib.pyplot as plt # visualization
import seaborn as sns

!pip install -q scikit-plot

import scikitplot as skplt
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler # data normalization
from sklearn.model_selection import train_test_split # data split
# from sklearn.neighbors import KNeighborsClassifier # KNN algorithm
from sklearn.linear_model import LogisticRegression # Logistic regression algorithm
from sklearn.ensemble import RandomForestClassifier # Random forest tree algorithm
from imblearn.over_sampling import SMOTE

from sklearn.metrics import confusion_matrix # evaluation metric
from sklearn.metrics import accuracy_score # evaluation metric
from sklearn.metrics import f1_score # evaluation metric

df = pd.read_csv('/content/drive/MyDrive/creditcard.csv')
df.drop('Time', axis = 1, inplace = True)
df.head()

"""Performing EDA"""

print('Non Fraud items:', len(df[df.Class == 0]))
print('Fraud items:', len(df[df.Class == 1]))

s = StandardScaler()
df['Amount'] = s.fit_transform(df['Amount'].values.reshape(-1, 1))

plt.figure(figsize=(12,8))
sns.heatmap(df.corr())
# from the result below we see that the columns have very low to no correlation at all.

X=df.drop('Class',axis=1)
Y=df['Class']
# appling oversampling techniques as we know the data is highly imbalanced
X_resample, y_resample = SMOTE().fit_resample(X, Y)
X_resample.shape , y_resample.shape

X_train,X_test,y_train,y_test=train_test_split(X_resample.values,y_resample.values,test_size = 0.25, random_state = 38)

DT = DecisionTreeClassifier(max_depth = 5, criterion = 'entropy')
DT.fit(X_train, y_train)
dt_y_pred = DT.predict(X_test)

print('F1 score of the Decision Tree model is {}'.format(f1_score(y_test, dt_y_pred)))

skplt.metrics.plot_confusion_matrix(y_test, dt_y_pred)

LR = LogisticRegression()
LR.fit(X_train, y_train)
y_pred_LR = LR.predict(X_test)
print('F1 score of the Decision Tree model is {}'.format(f1_score(y_test, y_pred_LR)))
skplt.metrics.plot_confusion_matrix(y_test, y_pred_LR)

rf = RandomForestClassifier(max_depth = 7)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print('F1 score of the Decision Tree model is {}'.format(f1_score(y_test, y_pred_rf)))
skplt.metrics.plot_confusion_matrix(y_test, y_pred_rf)