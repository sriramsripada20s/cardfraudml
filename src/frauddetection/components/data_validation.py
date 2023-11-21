import pandas as pd
from frauddetection.entity.config_entity import DataValidationConfig
from frauddetection  import logger

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None
            # Read the dataset
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            # Get schema columns from configuration
            all_schema = self.config.all_schema.keys()

            # Check each column against the schema
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            # droping nulll values column and unuseful columns
            #logger.info("droping nulll values column and unuseful columns")
            #data.drop(columns=["veil-type","stalk-root"],axis=1,inplace=True)
            logger.info("Data Converted to csv file")
            data.to_csv(self.config.root_dir+"/creditfraud.csv",index=False)

            return validation_status
        
        except Exception as e:
            raise e