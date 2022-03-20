# Medical Examination Research
## Description
The rows in the dataset represent patients and the columns represent information like body measurements, results from various blood tests, and lifestyle choices.

| Feature | Variable Type | Variable      | Value Type |
|:-------:|:------------:|:-------------:|:----------:|
| Age | Objective Feature | age | int (days) |
| Height | Objective Feature | height | int (cm) |
| Weight | Objective Feature | weight | float (kg) |
| Gender | Objective Feature | gender | categorical code |
| Systolic blood pressure | Examination Feature | ap_hi | int |
| Diastolic blood pressure | Examination Feature | ap_lo | int |
| Cholesterol | Examination Feature | cholesterol | 1: normal, 2: above normal, 3: well above normal |
| Glucose | Examination Feature | gluc | 1: normal, 2: above normal, 3: well above normal |
| Smoking | Subjective Feature | smoke | binary |
| Alcohol intake | Subjective Feature | alco | binary |
| Physical activity | Subjective Feature | active | binary |
| Presence or absence of cardiovascular disease | Target Variable | cardio | binary |

## Tasks
#### 1) Preprocess
* "cholesterol" and "gluc" variables' values turned into appropriate values.
* "overweight" variable was added.
* Incorrect and outlier data was eliminated.

#### 2) EDA & Visualization
* Data was converted to long format and a chart was created that shows the value counts of the categorical features. Chart was splitted by "cardio" variable.
* A correlation matrix of the dataset was created and was used for creating a heatmap.
