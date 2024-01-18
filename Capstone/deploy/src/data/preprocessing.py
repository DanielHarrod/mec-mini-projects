import pandas as pd

#SetDataFrameValue is a helper fuction that replaces an old value in a dataframe with a new value in a dataframe.
def SetDataFrameValue(ColumnName, Old, New, Df):
    Df.loc[Df[ColumnName] == Old, ColumnName] = New  

class DataProcessor:
    def __init__(self):
        # Create working dataframe
        global df
        df = pd.DataFrame()    

    def read_data(self, raw_data_path):
        global raw_df
        if (os.path.isfile(external_data_file_path) ) == False:
            raw_df = pd.read_sas(raw_data_path)
        else:
            print("Unable to read file")

    def transform(self, stable=True):
        global df
        df['diabetes'] = raw_df.DIABETE4
        # 1	Yes
        # 2	Yes, but female told only during pregnancy
        # 3	No
        # 4	No, pre-diabetes or borderline diabetes
        # 7	Don’t know/Not Sure
        # 9	Refused
        # BLANK	Not asked or Missing

        df.loc[df.diabetes.isin([1,2,4]), "diabetes"] = "Yes"
        df.loc[df.diabetes.isin([3]), "diabetes"] = "No"

        #Remove 7 Don't know/Not Sure and 9 Refused
        df.drop(df[df.diabetes.isin([7,9])].index, inplace=True)

        #Remove NA
        df.drop(df[df.diabetes.isna()].index, inplace=True)

        # Completed Survey 
        key = 'completed_survey'
        completed_survey_sort = ['Partial','Completed']

        df[key] = raw_df.DISPCODE

        SetDataFrameValue(key, 1100, "Completed",df)
        SetDataFrameValue(key, 1200, "Partial",df)


        # BMI
        key = 'bmi'
        bmi_sort = ['Under','Normal','Overweight',"Obese"]

        df[key] = raw_df._BMI5CAT
        # 1	Underweight
        # 2	Normal Weight
        # 3	Overweight
        # 4	Obese
        # BLANK	Don’t know/Refused/Missing

        SetDataFrameValue(key, 1, "Under",df)
        SetDataFrameValue(key, 2, "Normal",df)
        SetDataFrameValue(key, 3, "Overweight",df)
        SetDataFrameValue(key, 4, "Obese",df)


        # SMOKER
        key = 'smoker'
        smoker_sort = ['Current','Former','Some',"No"]

        df[key] = raw_df._SMOKGRP
        # 1	Current smoker, 20+ Pack Years
        # 2	Former smoker, 20+ Pack Years, quit < 15 years
        # 3	All other current and former smokers
        # 4	Never smoker
        # BLANK	Don’t know/Refused/Missing

        SetDataFrameValue(key, 1, "Current",df)
        SetDataFrameValue(key, 2, "Former",df)
        SetDataFrameValue(key, 3, "Some",df)
        SetDataFrameValue(key, 4, "No",df)


        #STROKE
        key = 'stroke'
        stroke_sort = ['Yes','No','Unsure','Refused']
        df[key] = raw_df.CVDSTRK3
        # 1	Yes
        # 2	No
        # 7	Don’t know/Not sure
        # 9	Refused
        # BLANK	Not asked or Missing

        SetDataFrameValue(key, 1, "Yes",df)
        SetDataFrameValue(key, 2, "No",df)
        SetDataFrameValue(key, 7, "Unsure",df)
        SetDataFrameValue(key, 9, "Refused",df)


        #heart_attack
        key = 'heart_attack'
        heart_attack_sort = ['Yes', 'No', 'Unsure', 'Refused']

        df[key] = raw_df.CVDINFR4
        # 1	Yes	
        # 2	No
        # 7	Don’t know/Not sure	
        # 9	Refused	
        # BLANK	Not asked or Missing

        SetDataFrameValue(key, 1, "Yes",df)
        SetDataFrameValue(key, 2, "No",df)
        SetDataFrameValue(key, 7, "Unsure",df)
        SetDataFrameValue(key, 9, "Refused",df)


        #ANGINA_OR_CHD
        key = 'angina_or_chd'
        angina_or_chd_sort = ['Yes', 'No', 'Unsure', 'Refused']

        df[key] = raw_df.CVDCRHD4
        # 1	Yes
        # 2	No
        # 7	Don’t know/Not sure
        # 9	Refused
        # BLANK	Not asked or Missing

        SetDataFrameValue(key, 1, "Yes",df)
        SetDataFrameValue(key, 2, "No",df)
        SetDataFrameValue(key, 7, "Unsure",df)
        SetDataFrameValue(key, 9, "Refused",df)


        #CHD_MI
        key = 'chd_mi'
        chd_mi_sort = ['Yes', 'No']

        df[key] = raw_df._MICHD
        # 1	Reported having MI or CHD
        # 2	Did not report having MI or CHD
        # BLANK	Not asked or Missing.

        SetDataFrameValue(key, 1, "Yes",df)
        SetDataFrameValue(key, 2, "No",df)


        #ASTHMA
        key = 'asthma'
        asthma_sort = ["Current", "Former", "Never", "Don't know"]

        df[key] = raw_df._ASTHMS1
        # 1	Current
        # 2	Former
        # 3	Never
        # 9	Don’t know/Not Sure Or Refused/Missing
        # Notes: ASTHMA3 = 7 or 9 or Missing or ASTHNOW = 7 or 9 or Missing

        SetDataFrameValue(key, 1, "Current",df)
        SetDataFrameValue(key, 2, "Former",df)
        SetDataFrameValue(key, 3, "Never",df)
        SetDataFrameValue(key, 9, "Don't know",df)


        #PHYSICAL_ACTIVITY
        key = 'physical_activity'
        physical_activity_sort = ["Yes", "No", "Don't know"]

        df[key] = raw_df._TOTINDA
        # 1	Had physical activity or exercise
        # 2	No physical activity or exercise in last 30 days
        # 9	Don’t know/Refused/Missing

        SetDataFrameValue(key, 1, "Yes",df)
        SetDataFrameValue(key, 2, "No",df)
        SetDataFrameValue(key, 9, "Don't know",df)


        #HEAVY DRINKING
        key = 'heavy_drinking'
        heavy_drinking_sort = ["Yes", "No", "Don't know"]

        df[key] = raw_df._RFDRHV8
        # 1	No
        # 2	Yes
        # 9	Don’t know/Refused/Missing

        SetDataFrameValue(key, 1, "Yes",df)
        SetDataFrameValue(key, 2, "No",df)
        SetDataFrameValue(key, 9, "Don't know",df)

        #NO DOCTOR DUE TO COST
        key = 'no_doctor_due_to_cost'
        no_doctor_due_to_cost_sort = ["Yes", "No", "Unsure", "Refused"]

        df[key] = raw_df.MEDCOST1
        # 1	Yes
        # 2	No
        # 7	Don’t know/Not sure
        # 9	Refused
        # BLANK	Not asked or Missing

        SetDataFrameValue(key, 1, "Yes",df)
        SetDataFrameValue(key, 2, "No",df)
        SetDataFrameValue(key, 7, "Unsure",df)
        SetDataFrameValue(key, 9, "Refused",df)

        #INSURANCE
        key = 'any_healthcare_insurance'
        any_healthcare_insurance_sort = ["Employer", "Private", "Medicare", "Medigap", "Medicaid", "CHIP", "Military", "Indian", "State", "Other", "No", "Unsure", "Refused"]

        df[key] = raw_df.PRIMINSR
        # 1	A plan purchased through an employer or union (including plans purchased through another person´s employer)
        # 2	A private nongovernmental plan that you or another family member buys on your own
        # 3	Medicare
        # 4	Medigap
        # 5	Medicaid
        # 6	Children´s Health Insurance Program (CHIP)
        # 7	Military related health care: TRICARE (CHAMPUS) / VA health care / CHAMP- VA
        # 8	Indian Health Service
        # 9	State sponsored health plan
        # 10 Other government program
        # 88 No coverage of any type
        # 77 Don’t know/Not Sure
        # 99 Refused
        # BLANK	Not asked or Missing

        SetDataFrameValue(key, 1, "Employer",df)
        SetDataFrameValue(key, 2, "Private",df)
        SetDataFrameValue(key, 3, "Medicare",df)
        SetDataFrameValue(key, 4, "Medigap",df)
        SetDataFrameValue(key, 5, "Medicaid",df)
        SetDataFrameValue(key, 6, "CHIP",df)
        SetDataFrameValue(key, 7, "Military",df)
        SetDataFrameValue(key, 8, "Indian",df)
        SetDataFrameValue(key, 9, "State",df)
        SetDataFrameValue(key, 10, "Other",df)
        SetDataFrameValue(key, 88, "No",df)
        SetDataFrameValue(key, 77, "Unsure",df)
        SetDataFrameValue(key, 99, "Refused",df)


        # GENERAL HEALTH
        key = 'general_health_status'
        general_health_status_sort = ["Excellent", "Very good", "Good", "Fair", "Poor", "Don’t know", "Refused"]

        df[key] = raw_df.GENHLTH
        # 1	Excellent
        # 2	Very good
        # 3	Good	
        # 4	Fair
        # 5	Poor
        # 7	Don’t know/Not Sure
        # 9	Refused
        # BLANK	Not asked or Missing

        SetDataFrameValue(key, 1, "Excellent",df)
        SetDataFrameValue(key, 2, "Very good",df)
        SetDataFrameValue(key, 3, "Good",df)
        SetDataFrameValue(key, 4, "Fair",df)
        SetDataFrameValue(key, 5, "Poor",df)
        SetDataFrameValue(key, 7, "Don’t know",df)
        SetDataFrameValue(key, 9, "Refused",df)


        #MENTAL HEALTH
        key = 'mental_health_status'
        mental_health_status_sort = ["0", "1-13", "14+", "Unknown"]

        df[key] = raw_df._MENT14D
        # 1	Zero days when mental health not good
        # 2	1-13 days when mental health not good
        # 3	14+ days when mental health not good
        # 9	Don’t know/Refused/Missing

        SetDataFrameValue(key, 1, "0",df)
        SetDataFrameValue(key, 2, "1-13",df)
        SetDataFrameValue(key, 3, "14+",df)
        SetDataFrameValue(key, 9, "Unknown",df)


        #PHYSICAL HEALTH
        key = 'physical_health_status'
        physical_health_status_sort = ["0", "1-13", "14+", "Unknown"]

        df[key] = raw_df._PHYS14D
        # 1	Zero days when physical health not good	
        # 2	1-13 days when physical health not good
        # 3	14+ days when physical health not good
        # 9	Don’t know/Refused/Missing

        SetDataFrameValue(key, 1, "0",df)
        SetDataFrameValue(key, 2, "1-13",df)
        SetDataFrameValue(key, 3, "14+",df)
        SetDataFrameValue(key, 9, "Unknown",df)

        #WALKING
        key = 'difficulty_walking'
        difficulty_walking_sort = ["Yes","No","Don’t know", "Refused"]

        df[key] = raw_df.DIFFWALK
        # 1	Yes	
        # 2	No	
        # 7	Don’t know/Not Sure
        # 9	Refused	
        # BLANK	Not asked or Missing

        SetDataFrameValue(key, 1, "Yes",df)
        SetDataFrameValue(key, 2, "No",df)
        SetDataFrameValue(key, 7, "Don’t know",df)
        SetDataFrameValue(key, 9, "Refused",df)


        #GENDER
        key = 'gender'
        gender_sort = ['Male','Female']

        df[key] = raw_df._SEX
        # 1	Male
        # 2	Female

        SetDataFrameValue(key, 1, "Male",df)
        SetDataFrameValue(key, 2, "Female",df)


        #AGE
        key = 'age'
        age_sort = ["18 to 24", "25 to 29", "30 to 34", "35 to 39", "40 to 44", "45 to 49", "50 to 54", "55 to 59", "60 to 64", "65 to 69", "70 to 74", "75 to 79", "80 or older", "Don’t know"]

        df[key] = raw_df._AGEG5YR
        # 1	Age 18 to 24
        # 2	Age 25 to 29
        # 3	Age 30 to 34
        # 4	Age 35 to 39
        # 5	Age 40 to 44
        # 6	Age 45 to 49
        # 7	Age 50 to 54
        # 8	Age 55 to 59
        # 9	Age 60 to 64
        # 10 Age 65 to 69
        # 11 Age 70 to 74
        # 12 Age 75 to 79
        # 13 Age 80 or older
        # 14 Don’t know/Refused/Missing

        SetDataFrameValue(key, 1, "18 to 24",df)
        SetDataFrameValue(key, 2, "25 to 29",df)
        SetDataFrameValue(key, 3, "30 to 34",df)
        SetDataFrameValue(key, 4, "35 to 39",df)
        SetDataFrameValue(key, 5, "40 to 44",df)
        SetDataFrameValue(key, 6, "45 to 49",df)
        SetDataFrameValue(key, 7, "50 to 54",df)
        SetDataFrameValue(key, 8, "55 to 59",df)
        SetDataFrameValue(key, 9, "60 to 64",df)
        SetDataFrameValue(key, 10, "65 to 69",df)
        SetDataFrameValue(key, 11, "70 to 74",df)
        SetDataFrameValue(key, 12, "75 to 79",df)
        SetDataFrameValue(key, 13, "80 or older",df)
        SetDataFrameValue(key, 14, "Don’t know",df)


        #EDUCATION
        key = 'education'
        education_sort = ["Middle School", "High School", "Some College", "Graduated College", "Not sure"]

        df[key] = raw_df._EDUCAG
        # 1	Did not graduate High School
        # 2	Graduated High School
        # 3	Attended College or Technical School
        # 4	Graduated from College or Technical School
        # 9	Don’t know/Not sure/Missing

        SetDataFrameValue(key, 1, "Middle School",df)
        SetDataFrameValue(key, 2, "High School",df)
        SetDataFrameValue(key, 3, "Some College",df)
        SetDataFrameValue(key, 4, "Graduated College",df)
        SetDataFrameValue(key, 9, "Not sure",df)


        #INCOME
        key = 'income'
        income_sort = ["< $15,000", "$15,000 to < $25,000", "$25,000 to < $35,000", "$35,000 to < $50,000", "$50,000 to < $100,000", "$100,000 to < $200,000", "> $200,000", "Don’t know"]

        df[key] = raw_df._INCOMG1
        # 1	Less than $15,000
        # 2	$15,000 to < $25,000
        # 3	$25,000 to < $35,000
        # 4	$35,000 to < $50,000
        # 5	$50,000 to < $100,000
        # 6	$100,000 to < $200,000
        # 7	$200,000 or more
        # 9	Don’t know/Not sure/Missing

        SetDataFrameValue(key, 1, "< $15,000",df)
        SetDataFrameValue(key, 2, "$15,000 to < $25,000",df)
        SetDataFrameValue(key, 3, "$25,000 to < $35,000",df)
        SetDataFrameValue(key, 4, "$35,000 to < $50,000",df)
        SetDataFrameValue(key, 5, "$50,000 to < $100,000",df)
        SetDataFrameValue(key, 6, "$100,000 to < $200,000",df)
        SetDataFrameValue(key, 7, "> $200,000",df)
        SetDataFrameValue(key, 9, "Don’t know",df)


        #RACE
        key = 'race'
        race_sort = ["White", "Black or African American", "American Indian or Alaskan Native", "Asian", "Native Hawaiian or other Pacific Islander", "Multiracial", "No race", "Don’t know", "Refused"]

        df[key] = raw_df._PRACE2
        # 1	White
        # 2	Black or African American
        # 3	American Indian or Alaskan Native
        # 4	Asian
        # 5	Native Hawaiian or other Pacific Islander
        # 7	Multiracial but no preferred race
        # 88	No race choice given
        # 77	Don’t know/Not sure
        # 99	Refused
        # BLANK	Missing

        SetDataFrameValue(key, 1, "White",df)
        SetDataFrameValue(key, 2, "Black or African American",df)
        SetDataFrameValue(key, 3, "American Indian or Alaskan Native",df)
        SetDataFrameValue(key, 4, "Asian",df)
        SetDataFrameValue(key, 5, "Native Hawaiian or other Pacific Islander",df)
        SetDataFrameValue(key, 7, "Multiracial",df)
        SetDataFrameValue(key, 88, "No race",df)
        SetDataFrameValue(key, 77, "Don’t know",df)
        SetDataFrameValue(key, 99, "Refused",df)

        #CHECKUPS
        key = 'routine_checkup'
        routine_checkup_sort = ["Within Last Year", "Last 2 Years", "Last 5 Years", "5 or more years", "Don't know", "Never", "Refused"]

        df[key] = raw_df.CHECKUP1
        # 1	Within past year (anytime less than 12 months ago)
        # 2	Within past 2 years (1 year but less than 2 years ago)
        # 3	Within past 5 years (2 years but less than 5 years ago)
        # 4	5 or more years ago
        # 7	Don’t know/Not sure
        # 8	Never
        # 9	Refused

        SetDataFrameValue(key, 1, "Within Last Year",df)
        SetDataFrameValue(key, 2, "Last 2 Years",df)
        SetDataFrameValue(key, 3, "Last 5 Years",df)
        SetDataFrameValue(key, 4, "5 or more years",df)
        SetDataFrameValue(key, 7, "Don't know",df)
        SetDataFrameValue(key, 8, "Never",df)
        SetDataFrameValue(key, 9, "Refused",df)


        #Sleeping
        key = 'sleep_time'
        df[key] = raw_df.SLEPTIM1

        # 1 - 24	Number of hours [1-24]
        # 77	Don’t know/Not Sure
        # 99	Refused
        # BLANK	Missing

        SetDataFrameValue(key, 77, "Don't Know",df)
        SetDataFrameValue(key, 99, "Refused",df)
        
        # Merge heart attack, chd/mi and angina/chd into a heart related feature due similar correlation between each other.
        df.loc[(df.heart_attack == 'Yes'),'heart_related'] = 'Yes'
        df.loc[(df.angina_or_chd == 'Yes'),'heart_related'] = 'Yes'
        df.loc[(df.chd_mi == 'Yes'),'heart_related'] = 'Yes'
        df.heart_related.fillna('No', inplace=True)
        df.drop(['heart_attack','angina_or_chd','chd_mi'], axis=1, inplace=True)     
        

        # Drop incomplete surveys
        df.drop(df[df.completed_survey == 'Partial'].index, inplace=True)

        #Drop the completed_survey column
        df.drop(["completed_survey"], axis=1, inplace=True)

        #remove nulls
        df.dropna(inplace=True)
        
        return df

    def write_data(self, processed_data_path, filename):
        df.to_csv(processed_data_path, compression={'method': 'zip', 'archive_name': filename}, index=False)