#whatever variables deifned in config.yml file are defined here in each class for pipelines
#data classes in Python to define configurations for different parts of a pipeline. These data classes 
#help organize and encapsulate different sets of parameters needed for various stages of your data processing pipeline.

from dataclasses import dataclass
from pathlib import Path

#Configuration related to data ingestion, including source URLs, local data files, etc.
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

#Configuration for data validation, handling status files, schemas
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

#Configuration for data transformation steps.
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

#Configuration for model training, including paths, model specifics
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    min_impurity_decrease: int
    min_samples_leaf: int
    min_samples_split: int 
    target_column: str

#Configuration for model evaluation, test data paths, model paths, parameters, metrics,#
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    mlflow_uri: str