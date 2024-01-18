import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

class FeatureProcessor:
    def __init__(self):
        pass
        
    def factorize(self, df, ignore_column_names=None):
        factorize_keys = pd.DataFrame(columns=['ColumnName','factors'])
        pg_df = df.copy()
        if (ignore_column_names != None):
            pg_df = pg_df.drop(ignore_column_names, axis=1)
        
        for object_column_name in pg_df.select_dtypes(include=['object']).columns:
            pg_df[object_column_name],y = pd.factorize(pg_df[object_column_name])
            self.AddRowToDF(factorize_keys,[object_column_name,y])
                
        return pg_df, factorize_keys
    
    def AddRowToDF(self, df, array):
        df.loc[len(df.index)] = array        
    
    def DropDataFrameValue(self, ColumnName, Old):
        self.encoded_df.drop(self.encoded_df[self.encoded_df[ColumnName] == Old].index, inplace=True)
    
    def read_data(self, pre_processed_path):
        self.features_df = pd.read_csv(pre_processed_path)
        return self.features_df
        # if (os.path.isfile(pre_processed_path) ) == False:
        #     features_df = pd.read_csv(pre_processed_path)
        # else:
        #     print(f"uUnable to read file {pre_processed_path}")
    
    def transform(self, stable=True):                
        self.encoded_df = self.features_df.copy()
        self.DropDataFrameValue( 'stroke','Unsure')
        self.DropDataFrameValue( 'stroke','Refused')

        self.DropDataFrameValue('asthma',"Don't know")

        self.DropDataFrameValue('physical_activity',"Don't know")
        self.DropDataFrameValue('heavy_drinking',"Don't know")

        self.DropDataFrameValue( 'no_doctor_due_to_cost','Unsure')
        self.DropDataFrameValue( 'no_doctor_due_to_cost','Refused')

        self.DropDataFrameValue( 'any_healthcare_insurance','Unsure')
        self.DropDataFrameValue( 'any_healthcare_insurance','Refused')

        self.DropDataFrameValue( 'general_health_status',"Don't know")
        self.DropDataFrameValue( 'general_health_status',"Refused")

        self.DropDataFrameValue( 'mental_health_status','Unknown')
        self.DropDataFrameValue( 'physical_health_status','Unknown')

        self.DropDataFrameValue( 'difficulty_walking',"Don't know")
        self.DropDataFrameValue( 'difficulty_walking','Refused')

        self.DropDataFrameValue( 'age', "Don’t know")

        self.DropDataFrameValue( 'education','Not sure')

        self.DropDataFrameValue('income',"Don’t know")

        self.DropDataFrameValue('race',"Don't know")
        self.DropDataFrameValue('race','Refused')

        self.DropDataFrameValue('routine_checkup',"Don't know")
        self.DropDataFrameValue('routine_checkup','Refused')

        self.DropDataFrameValue('sleep_time','Refused')
        self.DropDataFrameValue('sleep_time',"Don't Know")    

        self.factorized_data, self.factorize_data_keys = self.factorize(self.encoded_df)
        return self.factorized_data, self.factorize_data_keys
    
    def write_data(self, processed_data_path, filename):        
        self.factorized_data.to_csv(processed_data_path, compression={'method': 'zip', 'archive_name': filename}, index=False)
        keys_path = f'{processed_data_path[:-8]}_key.csv'
        self.factorize_data_keys.to_csv(keys_path, index=False)
