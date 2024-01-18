import os
import sys
from pathlib import Path

from preprocessing import DataProcessor

def main():    
    current_path = Path(__file__).parent
    external_data_file_path = f"{current_path}\..\..\data\external\LLCP2022.XPT.zip"  
    
    output_file_name = 'diabetes.csv'
    output_data_file_Path =  f"{current_path}\..\..\data\preprocessed\{output_file_name}.zip"  
    
    if (os.path.isfile(external_data_file_path) ) == False:
        print(f"Unable to find file {external_data_file_path}")
        sys.exit()  

    print('Making data analysis dataset from raw data')
    preprocessor = DataProcessor()

    print('  Reading data')
    preprocessor.read_data(external_data_file_path)

    print('  Processing data')
    preprocessor.transform()

    print('  Saving processed data')
    preprocessor.write_data(output_data_file_Path, output_file_name)
    
    print(f'  Saved: {output_data_file_Path}')
    
main()

