import pandas as pd
from pandas import DataFrame
from library.algoritms.knn import neighbors

# Regression

data = pd.read_csv(r"C:\\Users\\miga\\Desktop\\Data\\slump_test_data.csv", encoding='utf-8')
test = pd.read_csv(r"C:\\Users\\miga\\Desktop\\Data\\slump_test_test_data.csv", encoding='utf-8')
y_test = test['SP']
test = test.drop(['SP'], axis=1)
my_result = DataFrame()
my_result['before'] = y_test
knn_regression = neighbors.Regression(data, test, 6, 'SP')
my_result.insert(1, 'my_result', knn_regression.forecast())
print('Точность алгоритма регрессии: ', knn_regression.score(my_result, 'before', 'my_result'))
