import os
from box.exceptions import BoxValueError
import yaml
from frauddetection import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

#Uses os.makedirs to create directories. If verbose is True, it logs the path of the created directory.
@ensure_annotations
def create_directories(path_to_directories: list, verbose:bool=True):
    """Create directories from a list of paths

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

"""
@ensure_annotations
def dir_demo(path_to_directories: list, verbose:bool=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
"""

#Loads the YAML file using yaml.safe_load. If successful, returns the content wrapped in a ConfigBox. 
# If the file is empty, raises a ValueError.
@ensure_annotations
def read_yaml(path_to_yaml: Path)->ConfigBox:
    """read yaml file and returns content as ConfigBox

    Args:
        path_to_yaml (Path): Path to input YAML file

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox object with file content
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content =yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e

#Uses json.dump to write the dictionary data into the specified JSON file with proper indentation. 
# Logs the path where the JSON file is saved.
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")



# Loads the JSON file using json.load. Returns the content wrapped in a ConfigBox object.
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


#Uses joblib.dump to save the data in the specified path. Logs the path where the binary file is saved.
@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

#Loads the binary file using joblib.load and returns the loaded data.
@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


#Uses os.path.getsize to get the file size and converts it to KB. Returns the size as a string.
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"



"""
1. create_directories:

Purpose: Creates directories if they don't exist.
Need: When working with file I/O, it's common to ensure specific directories exist to store output files, logs, or intermediate data. This function creates necessary directories to avoid errors when writing files.

2. read_yaml:

Purpose: Reads YAML files and returns content as a ConfigBox.
Need: Often, configuration files are stored in YAML format. Reading YAML files into a structured data format like ConfigBox enables easier access and manipulation of configuration settings in your code.

3. save_json:

Purpose: Saves dictionary data as a JSON file.
Need: Storing data in JSON format is commonly used for data serialization. This function helps save Python dictionaries into JSON files for later retrieval or sharing with other systems.

4. load_json:

Purpose: Loads JSON files and returns content as a ConfigBox.
Need: Loading JSON data into a structured format allows easy access to the data within your code. It's useful for accessing configuration settings or data saved in JSON format.

5. save_bin:

Purpose: Saves binary data using joblib.
Need: Binary serialization is often used to store complex Python objects or models. This function helps save such data in a serialized form for later use or distribution.

6. load_bin:

Purpose: Loads binary data previously saved with joblib.
Need: After storing binary data, this function retrieves the serialized data for further use within your code, such as model loading or handling complex objects.

7. get_size:

Purpose: Retrieves file size in KB.
Need: Knowing the size of files can be essential for various reasons, such as monitoring disk usage, verifying data integrity, or ensuring files are within size limits for transmission or storage.



"""