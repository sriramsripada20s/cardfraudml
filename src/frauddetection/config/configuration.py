from frauddetection.constants import *
from frauddetection.utils.common import read_yaml, create_directories

from frauddetection.entity.config_entity import (DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig,ModelEvaluationConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        # Read configuration files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # Create necessary directories
        create_directories([self.config.artifacts_root])


    # Retrieve Data Ingestion Configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        # Create required directories to store data ingestion output
        create_directories([config.root_dir])
        
        ## Construct DataValidationConfig object . DataIngestionConfig object is a representation of configuration settings 
        # related to data ingestion within your application or workflow
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    # Retrieve Data Validation Configuration
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        # Create required directories to store data validation output
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config   

    #Retrieve Data Transformation Configuration
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        # Create required directories to store data transofrmation  output
        create_directories([config.root_dir])
        ##Construct DataTransformationConfig object
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config

    # Retrieve Model Trainer Configuration
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.DecisionTree
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])
        # Construct ModelTrainerConfig object
        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            min_impurity_decrease = params.min_impurity_decrease,
            min_samples_leaf = params.min_samples_leaf,
            min_samples_split = params.min_samples_split,
            target_column = schema.name
            
        )

        return model_trainer_config
    
    # Retrieve Model Evaluation Configuration
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.RandomForest
        schema =  self.schema.TARGET_COLUMN

        create_directories([config.root_dir])
        # Construct ModelEvaluationConfig object
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path = config.model_path,
            all_params=params,
            metric_file_name = config.metric_file_name,
            target_column = schema.name,
            mlflow_uri="https://dagshub.com/sriramsripada20s/cardfraudml.mlflow",
            
           
        )

        return model_evaluation_config