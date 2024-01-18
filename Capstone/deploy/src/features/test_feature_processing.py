import os
import sys
import pytest
import pandas as pd

from pathlib import Path

from featureprocessing import FeatureProcessor

output_file_name = 'diabetes.csv'

current_path = Path(__file__).parent
input_data_file_path =  os.path.abspath(f"{current_path}\..\..\data\preprocessed\{output_file_name}.zip") 
output_data_file_path = os.path.abspath( f"{current_path}\..\..\data\processed\{output_file_name}.zip"  )

featureprocessor = FeatureProcessor()

featureprocessor.read_data(input_data_file_path)

featureprocessor.transform()

featureprocessor.write_data(output_data_file_path,output_file_name)
def test_cow():
    assert True
    
#Not really a test, but needs to be there to test stuff.
def test_input_path_exist():
    assert os.path.isfile(input_data_file_path)
    
#Not really a test, but needs to be there to test stuff.
def test_output_path_exist():
    assert os.path.isfile(output_data_file_path)

def test_check_binary_diabetes():
    assert featureprocessor.encoded_df.diabetes.unique().shape[0] == 2
    
def test_check_encoding_21_features():
    assert featureprocessor.encoded_df.shape[1] == 21

def test_max_feature_values():
    for index, row in pd.melt(featureprocessor.factorized_data.describe()[-1:]).iterrows():
        if row['variable'] == 'diabetes':
            assert row['value'] == 1.0
        elif row['variable'] == 'bmi':
            assert row['value'] == 3.0
        elif row['variable'] == 'smoker':
            assert row['value'] == 3.0
        elif row['variable'] == 'stroke':
            assert row['value'] == 1.0
        elif row['variable'] == 'asthma':
            assert row['value'] == 2.0
        elif row['variable'] == 'physical_activity':
            assert row['value'] == 1.0
        elif row['variable'] == 'heavy_drinking':
            assert row['value'] == 1.0
        elif row['variable'] == 'no_doctor_due_to_cost':
            assert row['value'] == 1.0
        elif row['variable'] == 'any_healthcare_insurance':
            assert row['value'] == 10.0
        elif row['variable'] == 'general_health_status':
            assert row['value'] == 5.0
        elif row['variable'] == 'mental_health_status':
            assert row['value'] == 2.0
        elif row['variable'] == 'physical_health_status':
            assert row['value'] == 2.0
        elif row['variable'] == 'difficulty_walking':
            assert row['value'] == 2.0
        elif row['variable'] == 'gender':
            assert row['value'] == 1.0
        elif row['variable'] == 'age':
            assert row['value'] == 12.0
        elif row['variable'] == 'education':
            assert row['value'] == 3.0
        elif row['variable'] == 'income':
            assert row['value'] == 6.0
        elif row['variable'] == 'race':
            assert row['value'] == 7.0
        elif row['variable'] == 'routine_checkup':
            assert row['value'] == 4.0
        elif row['variable'] == 'sleep_time':
            assert row['value'] == 22.0
        elif row['variable'] == 'heart_related':
            assert row['value'] == 1.0

def test_min_feature_values():
    for index, row in pd.melt(featureprocessor.factorized_data.describe()[3:4]).iterrows():          
        if row['variable'] == 'diabetes':
            assert row['value'] == 0.0
        elif row['variable'] == 'bmi':
            assert row['value'] == 0.0
        elif row['variable'] == 'smoker':
            assert row['value'] == 0.0
        elif row['variable'] == 'stroke':
            assert row['value'] == 0.0
        elif row['variable'] == 'asthma':
            assert row['value'] == 0.0
        elif row['variable'] == 'physical_activity':
            assert row['value'] == 0.0
        elif row['variable'] == 'heavy_drinking':
            assert row['value'] == 0.0
        elif row['variable'] == 'no_doctor_due_to_cost':
            assert row['value'] == 0.0
        elif row['variable'] == 'any_healthcare_insurance':
            assert row['value'] == 0.0
        elif row['variable'] == 'general_health_status':
            assert row['value'] == 0.0
        elif row['variable'] == 'mental_health_status':
            assert row['value'] == 0.0
        elif row['variable'] == 'physical_health_status':
            assert row['value'] == 0.0
        elif row['variable'] == 'difficulty_walking':
            assert row['value'] == 0.0
        elif row['variable'] == 'gender':
            assert row['value'] == 0.0
        elif row['variable'] == 'age':
            assert row['value'] == 0.0
        elif row['variable'] == 'education':
            assert row['value'] == 0.0
        elif row['variable'] == 'income':
            assert row['value'] == 0.0
        elif row['variable'] == 'race':
            assert row['value'] == 0.0
        elif row['variable'] == 'routine_checkup':
            assert row['value'] == 0.0
        elif row['variable'] == 'sleep_time':
            assert row['value'] == 0.0
        elif row['variable'] == 'heart_related':
            assert row['value'] == 0.0