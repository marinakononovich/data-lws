import pandas as pd
from pandas import DataFrame
from library.algoritms.knn import neighbors

data = pd.read_csv(r"C:\\Users\\miga\\Desktop\\Data\\data.csv")

data['Class'].replace(['no-recurrence-events', 'recurrence-events'], [0, 1], inplace=True)
data['age'].replace(['90-99', '80-89', '70-79', '60-69', '50-59', '40-49', '30-39', '20-29', '10-19'], [9, 8, 7, 6, 5,
                                                                                                        4, 3, 2, 1],
                    inplace=True)
data['menopause'].replace(['lt40', 'ge40', 'premeno'], [1, 2, 3], inplace=True)
data['tumor-size'].replace(['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
                            '50-54', '55-59'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], inplace=True)
data['inv-nodes'].replace(['0-2', '3-5', '6-8', '9-11', '12-14', '15-17', '18-20', '21-23', '24-26', '27-29', '30-32',
                           '33-35', '36-39'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], inplace=True)
data['node-caps'].replace(['yes', 'no', '?'], [1, 0, 0], inplace=True)
data['breast'].replace(['left', 'right'], [1, 0], inplace=True)
data['breast-quad'].replace(['left_up', 'left_low', 'right_up', 'right_low', 'central'], [1, 2, 3, 4, 5] , inplace=True)
data['irradiat'].replace(['yes', 'no'], [1, 0], inplace=True)
data.replace(['?'], 1, inplace=True)

test = pd.read_csv(r"C:\\Users\\miga\\Desktop\\Data\\data_test.csv")

test['Class'].replace(['no-recurrence-events', 'recurrence-events'], [0, 1], inplace=True)
test['age'].replace(['90-99', '80-89', '70-79', '60-69', '50-59', '40-49', '30-39', '20-29', '10-19'], [9, 8, 7, 6, 5,
                                                                                                        4, 3, 2, 1],
                    inplace=True)
test['menopause'].replace(['lt40', 'ge40', 'premeno'], [1, 2, 3], inplace=True)
test['tumor-size'].replace(['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49',
                            '50-54', '55-59'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], inplace=True)
test['inv-nodes'].replace(['0-2', '3-5', '6-8', '9-11', '12-14', '15-17', '18-20', '21-23', '24-26', '27-29', '30-32',
                           '33-35', '36-39'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], inplace=True)
test['node-caps'].replace(['yes', 'no', '?'], [1, 0, 0], inplace=True)
test['breast'].replace(['left', 'right'], [1, 0], inplace=True)
test['breast-quad'].replace(['left_up', 'left_low', 'right_up', 'right_low', 'central'], [1, 2, 3, 4, 5] , inplace=True)
test['irradiat'].replace(['yes', 'no'], [1, 0], inplace=True)
test.replace(['?'], 1, inplace=True)

y_test = test['irradiat']
test = test.drop(['irradiat'], axis=1)
my_result = DataFrame()
my_result['before'] = y_test
knn_classifier = neighbors.Classifier(data, test, 6, 'irradiat')
my_result.insert(1, 'my_result', knn_classifier.forecast())
print('Точность алгоритма классификатора: ', knn_classifier.score(my_result, 'before', 'my_result'))

