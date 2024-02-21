
import pandas as pd


#columns = ['Overall Qual', 'Overall Cond', 'Gr Liv Area','Central Air', 'Total Bsmt SF', 'SalePrice']
#
#df = pd.read_csv('http://jse.amstat.org/v19n3/decock/AmesHousing.txt', sep='\t',usecols=columns)
#
#df.head()
#
#df.to_csv('ames_housing.csv', index=False, encoding='utf-8')
from sklearn.datasets import fetch_openml
X, y = fetch_openml('mnist_784', version=1, return_X_y=True, parser='auto')
X = X.values
y = y.values.astype(int)
print(X.shape)
print(y.shape)
print(X)
print(y)
