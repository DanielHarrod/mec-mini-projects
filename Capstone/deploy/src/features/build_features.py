import os
import sys

from pathlib import Path

from featureprocessing import FeatureProcessor

def main():    
    output_file_name = 'diabetes.csv'

    current_path = Path(__file__).parent
    input_data_file_path =  os.path.abspath(f"{current_path}\..\..\data\preprocessed\{output_file_name}.zip") 
    output_data_file_path = os.path.abspath( f"{current_path}\..\..\data\processed\{output_file_name}.zip"  )
        
    if (os.path.isfile(input_data_file_path) ) == False:
        print(f"Unable to find file {input_data_file_path}")
        sys.exit()  
        
    featureprocessor = FeatureProcessor()
    
    featureprocessor.read_data(input_data_file_path)
    
    featureprocessor.transform()
    
    featureprocessor.write_data(output_data_file_path,output_file_name)
    
main()
    
