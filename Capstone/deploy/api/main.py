import numpy as np
import pandas as pd

from typing import List

from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from pydantic import BaseModel, ValidationError, validator
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from .ml.model import Model, get_model, n_features


class PredictRequest(BaseModel):
    data: List[List[float]]

    @validator("data")
    def check_dimensionality(cls, v):
        for point in v:
            if len(point) != n_features:
                raise ValueError(f"Each data point must contain {n_features} features")
        X=v[0]
        bmi = X[0]
        smoker = X[1]
        stroke = X[2]
        asthma = X[3]
        physical_activity = X[4]
        heavy_drinking = X[5]
        no_doctor_due_to_cost = X[6]
        any_healthcare_insurance = X[7]
        general_health_status = X[8]
        mental_health_status = X[9]
        physical_health_status = X[10]
        difficulty_walking = X[11]
        gender = X[12]
        age = X[13]
        education = X[14]
        income = X[15]
        race = X[16]
        routine_checkup = X[17]
        sleep_time = X[18]
        heart_related = X[19]
        
        issues = list()
        
        if ( bmi < 0 or bmi > 3 ):
            issues.append(f'Error: BMI[0] options are 0=Overweight, 1=Normal, 2=Obese, 3=Under - received {bmi}')
        if ( smoker < 0 or smoker > 3 ):
            issues.append(f'Error: Smoker[1] options are 0=No, 1=Some, 2=Current, 3=Former - received {smoker}')
        if ( stroke < 0 or stroke > 1 ):
            issues.append(f'Error: Stroke[2] options are 0=No, 1=Yes - received {stroke}')
        if ( asthma < 0 or asthma > 2 ):
            issues.append(f'Error: Asthma[3] options are 0=Never, 1=Current, 2=Former - received {asthma}')
        if ( physical_activity < 0 or physical_activity > 1 ):
            issues.append(f'Error: Physical Activity[4] options are 0=No, 1=Yes - received {physical_activity}')
        if ( heavy_drinking < 0 or heavy_drinking > 1 ):
            issues.append(f'Error: Heavy Drinking[5] options are 0=Yes, 1=No - received {heavy_drinking}')
        if ( no_doctor_due_to_cost < 0 or no_doctor_due_to_cost > 1 ):
            issues.append(f'Error: No doctor due to cost[6] options are 0=No, 1=Yes - received {no_doctor_due_to_cost}')
        if ( any_healthcare_insurance < 0 or any_healthcare_insurance > 10 ):
            issues.append(f'Error: Health Care Insurance[7] options are 0=Medicare, 1=Employer, 2=Military, 3=Private, 4=Medigap, 5=Other, 6=Medicaid, 7=No, 8=State, 9=Indian, 10=CHIP  - received {any_healthcare_insurance}')
        if ( general_health_status < 0 or general_health_status > 4 ):
            issues.append(f'Error: General Health[8] options are 0=Excellent, 1=Very good, 2=Fair, 3=Good, 4=Dont know - received {general_health_status}')
        if ( mental_health_status < 0 or mental_health_status > 2 ):
            issues.append(f'Error: Mental Health[9] options are 0=0 days, 1=1-13 days, 2=14+ days - received {mental_health_status}')
        if ( physical_health_status < 0 or physical_health_status > 2 ):
            issues.append(f'Error: Physical Health[10] options are 0=0 days, 1=1-13 days, 2=14+ days - received {physical_health_status}')
        if ( difficulty_walking < 0 or difficulty_walking > 2 ):
            issues.append(f'Error: Difficulty Walking[11] options are 0=No, 1=Yes, 2=Dont know - received {difficulty_walking}')
        if ( gender < 0 or gender > 1 ):
            issues.append(f'Error: Gender[12] options are 0=Female, 1=Male - received {gender}')
        if ( age < 0 or age > 12 ):
            issues.append(f"Error: age[13] options are 0='80 or older', 1='55 to 59', 2='40 to 44', 3='70 to 74', 4='65 to 69', 5='60 to 64', 6='75 to 79', 7='50 to 54', 8='45 to 49', 9='35 to 39', 10='25 to 29', 11='30 to 34', 12='18 to 24' - received {age}")
        if ( education < 0 or education > 3 ):
            issues.append(f'Error: education[14] options are 0=High School, 1=Graduated College, 2=Some College, 3=Middle School - received {education}')
        if ( income < 0 or income > 6 ):
            issues.append(f'Error: income[15] options are 0=$25,000 to < $35,000, 1=$100,000 to < $200,000, 2=$50,000 to < $100,000, 3=$35,000 to < $50,000, 4=< $15,000, 5=$15,000 to < $25,000, 6=> $200,000 - received {income}')
        if ( race < 0 or race > 7 ):
            issues.append(f'Error: race[16] options are 0=White, 1=Black or African American, 2=American Indian or Alaskan Native, 3=Native Hawaiian or other Pacific Islander, 4=Asian, 5=Dont know, 6=Multiracial, 7=No race - received {race}')
        if ( routine_checkup < 0 or routine_checkup > 4 ):
            issues.append(f'Error: routine_checkup[17] options are 0=Never, 1=Within Last Year, 2=Last 2 Years, 3=Last 5 Years, 4=5 or more years - received {routine_checkup}')
        if ( sleep_time < 0 or sleep_time > 24 ):
            issues.append(f'Error: sleep_time[18] options are 1 to 24- received {sleep_time}')
        if ( heart_related < 0 or heart_related > 1 ):
            issues.append(f'Error: heart_related[19] options are 0=No, 1=Yes - received {heart_related}')

        if len(issues) > 0:
            raise ValueError(issues)
        
        
        return v


class PredictResponse(BaseModel):
    data: List[float]


app = FastAPI()


@app.post("/predict", response_model=PredictResponse)
def predict(input: PredictRequest, model: Model = Depends(get_model)):
    """
    Returns an integer 0 for negative prediction for diabetes, and 1 for positive prediction for diabets.
    
    :param Array[int]: Array of 20 integers - BMI [0], Smoker[1], Stroke[2], Asthma[3],Physical Activity[4], Heavy Drinking[5], cost[6], Health Care Insurance[7], General Health[8],  Health[9], Health[10], Difficulty Walking[11], Gender[12], age[13], education[14], income[15], race[16], routine_checkup[17], sleep_time[18], Heart_related[19]
    :type Array[int]: integers
    :raise ValueException for missing or out of range parameters
    :return: 0 for negative and 1 for positive
    :rtype: array[int]
    """

    X = np.array(input.data)
    y_pred = model.predict(X)
    result = PredictResponse(data=y_pred.tolist())

    return result


# @app.post("/predict_csv")
# def predict_csv(csv_file: UploadFile = File(...), model: Model = Depends(get_model)):
#     try:
#         df = pd.read_csv(csv_file.file).astype(float)
#     except:
#         raise HTTPException(
#             status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Unable to process file"
#         )

#     df_n_instances, df_n_features = df.shape
#     if df_n_features != n_features:
#         raise HTTPException(
#             status_code=HTTP_422_UNPROCESSABLE_ENTITY,
#             detail=f"Each data point must contain {n_features} features",
#         )

#     y_pred = model.predict(df.to_numpy().reshape(-1, n_features))
#     result = PredictResponse(data=y_pred.tolist())

#     return result
