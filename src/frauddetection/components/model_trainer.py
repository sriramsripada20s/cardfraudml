import os
from frauddetection import logger
#from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import joblib
from frauddetection.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]


        dt = DecisionTreeClassifier(min_impurity_decrease=self.config.min_impurity_decrease,min_samples_leaf=self.config.min_samples_leaf,
                                    min_samples_split=self.config.min_samples_split,random_state=42)
        dt.fit(train_x, train_y.values.ravel())

        joblib.dump(dt, os.path.join(self.config.root_dir, self.config.model_name))
    
