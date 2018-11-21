import numpy as np
from operator import itemgetter
from scipy.spatial import distance
import pandas as pd


class Knn:
    def __init__(self, data, test, k, classColumnName):
        self.data = data
        self.test = test
        self.k = k
        self.classColumnName = classColumnName

    @staticmethod
    def getEuclidean(vector1, vector2):
        return distance.euclidean(vector1, vector2)

    @staticmethod
    def score(resultDataFrame, actualResultColumnName, predictedResultColumnName):
        counter = 0
        length = len(resultDataFrame)
        for i in range(length):
            if resultDataFrame.iloc[i][actualResultColumnName] != resultDataFrame.iloc[i][predictedResultColumnName]:
                counter = counter + 1
        return 1 - (counter / length)

    def getNeighbors(self):
        y_data = self.data[self.classColumnName]
        data = self.data.drop([self.classColumnName], axis=1)
        neighbors_list = []
        for test_index, test_row in self.test.iterrows():
            labels = []
            testDistances = {}
            for data_index, data_row in data.iterrows():
                testDistances[data_index] = self.getEuclidean(test_row, data_row)
            testDistancesSorted = (sorted(testDistances.items(), key=itemgetter(1)))

            for i in range(0, self.k):
                labels.append(y_data[testDistancesSorted[i][0]])
            neighbors_list.append(labels)
        return neighbors_list


class Classifier(Knn):
    def __init__(self, data, test, k, classColumnName):
        super().__init__(data, test, k, classColumnName)

    def forecast(self):
        neighbors_list = self.getNeighbors()
        length = len(neighbors_list)
        labeled_test = []
        for i in range(length):
            a_set = set(neighbors_list[i])

            popular_item = None
            count_popular = 0

            for item in a_set:
                list_neighbors_size = neighbors_list[i].count(item)
                if list_neighbors_size > count_popular:
                    count_popular = list_neighbors_size
                    popular_item = item

            labeled_test.append(popular_item)

        return pd.DataFrame(labeled_test)


class Regression(Knn):
    def __init__(self, data, test, k, classColumnName):
        super().__init__(data, test, k, classColumnName)

    def forecast(self):
        neighbors_list = self.getNeighbors()
        length = len(neighbors_list)
        result_test = []
        for i in range(length):
            avg_val = np.mean(neighbors_list[i])
            result_test.append(avg_val)

        return pd.DataFrame(result_test)
