# This module contains functions, that generate a classifier
import os.path

from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import MinMaxScaler, StandardScaler, PolynomialFeatures
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
import pickle

from Decorators import time
from Utility.functions import vectorize_word, map_to_numbers
from Utility.data import alphabet


class Classifier:
    """Universal classifier class. It incapsulates all
    the work inside and provides a simple interface to
    use internal classifier.

    Fields:
        __classifier - internal classifier
        __X_test - test set of data
        __y_test - test answers
    """

    def __init__(self):
        """Initializes and creates internal classifier.
        Classifier is built by pipeline; this strategy
        helps to achieve a better results.
        """

        pipeline = Pipeline([
            ('1', MinMaxScaler()),
            ('2', PolynomialFeatures()),
            ('3', GaussianNB())
        ])

        params = [{
            '1': [StandardScaler(), MinMaxScaler()],
            '3': [KNeighborsClassifier(), XGBClassifier(), GaussianNB()]
        }]

        self.__classifier = GridSearchCV(pipeline, param_grid=params)
        self.__X_test = None
        self.__y_test = None

    def fit(self, X, y):
        """Wraps 'fit' method of internal classifier.
        This function provides model learning.

        :param X: data to fit
        :param y: answers to fit
        """

        self.__classifier.fit(list(X.values), y)

    def predict(self, data: list):
        mapped_alphabet = map_to_numbers(0, *tuple(alphabet))

        data_to_pass = list()
        for word in data:
            data_to_pass.append(list(vectorize_word(word, mapped_alphabet)))

        return self.__classifier.predict(data_to_pass)


@time.benchmark
def make_classifier(X, y, path):
    classifier = Classifier()

    if os.path.exists(path):
        print('Read from {}'.format(path))
        with open(path, 'rb') as binary:
            classifier = pickle.load(binary)

    else:
        classifier.fit(X, y)
        with open(path, 'wb') as binary:
            pickle.dump(classifier, binary)
            print('Written to {}'.format(path))

    return classifier
