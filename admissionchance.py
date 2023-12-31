# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1219m5AjvcI6k6A8HFVI0peXJFpFAvFIT
"""

import pandas as pd

admission = pd.read_csv('https://raw.githubusercontent.com/YBIFoundation/Dataset/main/Admission%20Chance.csv')

admission.head()

admission.info()

admission.describe()

admission.columns

y = admission['Chance of Admit ']

x = admission.drop(['Serial No','Chance of Admit '],axis=1)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, random_state = 2529)

x_train.shape, x_test.shape, y_train.shape, y_test.shape

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x_train, y_train)

model.intercept_

model.coef_

y_pred = model.predict(x_test)

y_pred

from sklearn.metrics import mean_absolute_percentage_error

mean_absolute_percentage_error(y_test, y_pred)