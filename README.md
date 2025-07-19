# LipoPredict AI  
An AI model to predict the probability that a client will opt for U-Lipolysis treatment at a clinic, helping the clinic better target potential customers.

## Problem Statement  
Predict the probability (between 0 and 1) that a client will buy a U-Lipolysis treatment plan aimed at reducing body fat % and increasing muscle mass.

## Type of Learning  
- **Learning Type:** Supervised Learning  
- **Problem Type:** Regression (continuous output)  
- **Output Variable:** buy_plan (e.g., 0.80 = 80% chance the client will buy the U-Lipolysis tratment plan)

## Input Features  
| Feature Name         | Description                               |  
|----------------------|-------------------------------------------|  
| age                  | Age of the client                         |  
| weight               | Body weight in kg                         |  
| bmi                  | Body Mass Index                           |  
| medical_condition    | Any medical issue (e.g., diabetes, PCOS)  |  
| gender               | Male/Female/Other                         |  
| body_fat_percent     | Overall body fat %                        |  
| visceral_fat_percent | Visceral fat % (around organs)            |  
| marital_status       | Single, Married, Other                    |  
| location             | City or area                              |  
| target_weight_loss   | How much weight the client wants to lose  |  
| profession           | Job title or industry                     |  
| job_type             | Sitting, Field, or Mixed type of job      |  
| work_stress_level    | ( 0 to 10) Where 0 is low - 10 is high    |  
| physical_activeness  | (0 to 3) O: low, 1: Moderate, 3: High     |


## Target Variable  
- **buy_plan:** A float between 0.0 and 1.0 indicating the predicted probability of purchase.


## Follow Step to execute the application

-  **Step 1. Create Virtual Environment using Conda**
conda create -p virtual_env python==3.11 -y

-  **Step 2. Activate vitual enviroment**
conda acitvate <<vitual_env_name>>/
conda activate virtual_env/

-  **Step 4. Install Packages**
pip install -r requirements.txt

-  **Step 3. Run Streamlit App**
streamlit run <<file_name>>




