# -*- coding: utf-8 -*-
"""miniproject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oNxoStevx9YFjv17uj1butivoL9FNos0
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df=pd.read_csv('Real_Combine.csv')

df.head()

sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap='viridis')

df=df.dropna()

X=df.iloc[:,:-1] ## independent features
y=df.iloc[:,-1] ## dependent features

X.isnull()

y.isnull()

#sns.pairplot(df)

df.corr()

import seaborn as sns
corrmat = df.corr()
top_corr_features = corrmat.index
#plt.figure(figsize=(20,20))
#g=sns.heatmap(df[top_corr_features].corr(),annot=True,cmap="RdYlGn")

corrmat.index

from sklearn.ensemble import ExtraTreesRegressor
import matplotlib.pyplot as plt
model = ExtraTreesRegressor()
model.fit(X,y)

X.head()

print(model.feature_importances_)

feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(5).plot(kind='barh')
#plt.show()

#sns.distplot(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

from sklearn.linear_model import LinearRegression

regressor=LinearRegression()
regressor.fit(X_train,y_train)

regressor.coef_

regressor.intercept_

print("Coefficient of determination R^2 <-- on train set: {}".format(regressor.score(X_train, y_train)))

print("Coefficient of determination R^2 <-- on train set: {}".format(regressor.score(X_test, y_test)))

from sklearn.model_selection import cross_val_score
score=cross_val_score(regressor,X,y,cv=5)

score.mean()

coeff_df = pd.DataFrame(regressor.coef_,X.columns,columns=['Coefficient'])
coeff_df

prediction=regressor.predict(X_test)

prediction

predictions=regressor.predict([[7.4,9.8,4.8,1017.6,93.0,0.5,4.3,9.4]])

predictions

#sns.distplot(y_test-prediction)

#plt.scatter(y_test,prediction)

from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_test, prediction))
print('MSE:', metrics.mean_squared_error(y_test, prediction))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, prediction)))

def survivalpredict(x_test):
  return regressor.predict(x_test)
'''
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
print(accuracy_score(y_test,predictions)*100)

print(confusion_matrix(y_test,predictions))

print(classification_report(y_test,predictions))

predictions=logmodel.predict([[22.0,1,0,7.2500,1,0,1,0,1]])
predictions

!pip install flask-ngrok

from flask_ngrok import run_with_ngrok
from flask import Flask,jsonify
app=Flask(__name__)
run_with_ngrok(app)
@app.route("/<float:Age>/<int:SibSp>/<int:Parch>/<float:Fare>/<Gender>/<int:Pclass>/<Place>")'''
def home(t,tm1,tm,slp,h,vv,v,vm):
  '''p=[]
  p+=[t,TM,tm,slp,h,vv,v]
  arr=np.array([p])'''
  predict1=regressor.predict([[t,tm1,tm,slp,h,vv,v,vm]])
  strings=[str(integer) for integer in predict1]
  a_string="".join(strings)
  an_integer=int(float(a_string))
  return an_integer