import os
import sys
import pickle
import numpy as np

import pandas as pd

from pathlib import Path

sys.path.append('../features')
from featureprocessing import FeatureProcessor

from sklearn.metrics import make_scorer
from sklearn.metrics import roc_auc_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from sklearn.ensemble import ExtraTreesClassifier

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split


class Model:
    def __init__(self):
        self.roc_auc_score = ''
        self.accuracy = ''
        current_path = Path(__file__).parent
        file_name = 'diabetes.csv'
        self.feature_data_file_Path =  f"{current_path}\..\..\data\preprocessed\{file_name}.zip"  
        if (os.path.isfile(self.feature_data_file_Path) ) == False:
            print(f"Unable to find file in expected location {self.feature_data_file_Path}")
            sys.exit()         
    
    def TrainTestSplit(self, data):
        self.train_features, self.test_features, self.train_labels, self.test_labels = train_test_split(data, data.diabetes, stratify=data.diabetes, random_state=42, test_size=0.20)
        self.test_features['diabetes'] = self.test_labels
        return self.train_features, self.test_features
    
    def train_save_etc_model(self):
        fp = FeatureProcessor()
        fp.read_data(self.feature_data_file_Path)
        data, keys = fp.transform()
        
        self.train_features, self.test_features = self.TrainTestSplit(fp.factorized_data)

        self.train_labels = self.train_features.diabetes
        self.train_features = self.train_features.drop('diabetes', axis=1)

        params = [{ 'criterion': ['gini'],
                    'n_estimators': [80], #700
                    'min_samples_split': [40],
                    'min_samples_leaf':[3]
                }]

        etc  = GridSearchCV(ExtraTreesClassifier(),
                            param_grid=params,
                            #scoring=make_scorer(PositivePredictedValue, greater_is_better=True),
                            scoring='recall',
                            cv=5,
                            verbose=0)
        etc.fit(self.train_features, self.train_labels)

        self.model = etc.best_estimator_

        self.roc_auc_score =  roc_auc_score(self.train_labels, self.model.predict_proba(self.train_features)[:, 1])

        self.test_labels = self.test_features.diabetes
        self.test_features = self.test_features.drop('diabetes', axis=1)

        self.test_prediction = etc.predict(self.test_features)

        self.accuracy = accuracy_score(self.test_labels, self.test_prediction)
        
        filename = f'{Path(__file__).parent.parent.parent}\\api\ml\extra_trees_classifier.pickle'
        #pickle.dump(self.model, open(filename,'wb'))
        print(f'Saved Model {filename}')

                
if __name__ == '__main__':
    saver = Model()
    saver.train_save_etc_model()
    
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
           
    for count, value in enumerate(saver.test_prediction):
        if(value==1):
            print(count, value)
            print(saver.test_features.iloc[[count]])
