# Assignment 24.6 

## 24.6 - Part 1 Folder overview
- src\data - has external, preprocessed, and processed data(with key)
- src\features - data preprocessing and data feature processing
- src\models - trains the model and saves to the api folder
- src\visualization - future

## 24.6 - Part 2 Folder overview
- \ - docker container and configuration
- api- web service code using fastapi
- api\ml - model pickle file and model class used by api

## Project setup for 24.6
1. Acquire original src file from CDC Website, LLCP2022.XPT.zip 
   - https://www.cdc.gov/brfss/annual_data/annual_2022.html
2. Store file in \data\external\ folder
3. Preprocess data
   - Saves diabetes.csv in data\preprocessed\ folder
```
cd src\data\
python make_dataset.py
```
4. Build Features
   - Saves diabetes.csv and diabetes_key.csv in data\processed\ folder
```
cd src\features\
python build_features.py
```
5. Test Features
   - Tests files exist
   - Test for binary classification
   - Tests for expected features
   - For each feature, tests that the values are within the category range.
```
cd src\features\
pytest
```
6. Create and store model.
   - Uses preprocessed diabetes.csv file to train model.
   - Saves model.pickle in api\ml\ for deployment
```
cd src\models
python train_model.py
```

7. Test model
   - Basic model test
```
cd api\ml
python model.py
```

## Project setup for 24.6 - Part 2 
1. Run Docker Desktop
2. conda activate (base)
3. cd deploy\src\models
4. python train_model.py
5. cd deploy
6. docker compose up

## Posted data layout
### Parameter index:
 bmi, smoker, stroke, asthma, physical_activity, heavy_drinking, no_doctor_due_to_cost, any_healthcare_insurance, general_health_status, mental_health_status, physical_health_status, difficulty_walking, gender, age, education, income, race, routine_checkup, sleep_time, heart_related


## Deployed Test Samples
### Negative Test
```
curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"data\":[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]}"

curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"data\":[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]}"
```

### Positive Test samples
```
curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"data\":[[2,1,0,1,0,0,0,0,4,2,2,1,1,4,0,5,0,1,3,1]]}"

curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"data\":[[2,1,1,0,1,0,0,0,4,2,1,1,0,5,2,5,0,1,0,1]]}"
```

### Out of bounds samples
```
curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"data\":[[99,1,1,0,1,0,0,0,4,2,1,1,0,5,2,5,0,1,0,1]]}"
```

### Short data
```
curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"data\":[[1]]}"
```
### Long data
```
curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"data\":[[2,1,1,0,1,0,0,0,4,2,1,1,0,5,2,5,0,1,0,1,1,1,11,1,1]]}"
```

## Setting up sphinx
```
(base) C:\Springboard\mec-mini-projects\Capstone\deploy>mkdir docs
cd docs
sphinx-quickstart 
(Accept defaults)

cd C:\Springboard\mec-mini-projects\Capstone\deploy>
sphinx-apidoc -o docs .

(base) C:\Springboard\mec-mini-projects\Capstone\deploy>sphinx-apidoc -o docs .
Creating file docs\api.rst.
Creating file docs\api.ml.rst.
Creating file docs\api.tests.rst.
Creating file docs\api.tests.api.rst.
Creating file docs\src.rst.
Creating file docs\modules.rst.

added extensions to conf.py, added abs path to conf.py, added phinx_rtd_theme

Goto
(base) C:\Springboard\mec-mini-projects\Capstone\deploy\docs>

make html
```

## Quick Start notebook.
See quick-start.ipynb shows how to run docker container and call the api with options.
<!-- 

Note: Good stuff in here I might need it.

# fastAPI ML quickstart


## Project setup
1. Create the virtual environment.
```
virtualenv /path/to/venv --python=/path/to/python3
```
You can find out the path to your `python3` interpreter with the command `which python3`.

2. Activate the environment and install dependencies.
```
source /path/to/venv/bin/activate
pip install -r requirements.txt
```

3. Launch the service
```
uvicorn api.main:app
```

## Posting requests locally
When the service is running, try
```
127.0.0.1/docs
```
or 
```
curl
```

## Deployment with Docker
1. Build the Docker image
```
docker build --file Dockerfile --tag fastapi-ml-quickstart .
```

2. Running the Docker image
```
docker run -p 8000:8000 fastapi-ml-quickstart
```

3. Entering into the Docker image
```
docker run -it --entrypoint /bin/bash fastapi-ml-quickstart
```

## docker-compose
1. Launching the service
```
docker-compose up
```
This command looks for the `docker-compose.yaml` configuration file. If you want to use another configuration file,
it can be specified with the `-f` switch. For example  

2. Testing
```
docker-compose -f docker-compose.test.yaml up --abort-on-container-exit --exit-code-from fastapi-ml-quickstart
```
-->