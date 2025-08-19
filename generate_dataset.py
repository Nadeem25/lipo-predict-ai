import pandas as pd
import numpy as np
import random

def generate_dataset():

    # Number of records
    num_records = 10000

    # Random seed for reproducibility
    np.random.seed(42)

    # Age between 15 and 80
    age = np.random.randint(20, 90, num_records)

    # Weight between 30 and 120 kg
    weight = np.random.uniform(30, 120, num_records).round(1) # 55-110

    feet = np.random.randint(4, 8, size=num_records)
    # Generate random inches between 0 and 11
    inches = np.random.randint(0, 11, size=num_records)

    height = height_in_feet = np.round(feet + inches / 12, 1)
    meters = (feet * 12 + inches) * 0.0254

    # BMI calculation
    bmi = (weight / (meters ** 2)).round(2)     # underweight: <18 , normal: 18-25, 25-30 overweight, 30+ obese  overall : 15-50 

    # Gender: male or female
    gender = np.random.choice(['male', 'female'], num_records)

    # Is medical condition: yes or no
    is_medical_condition = np.random.choice(['yes', 'no'], num_records)

    # Common diseases in Indian women
    common_diseases_women = [
        'Anemia', 'Thyroid', 'Diabetes', 'PCOS', 'Hypertension', 
        'Osteoporosis', 'Vitamin D Deficiency', 'Obesity', 'Heart Disease', 'Depression'
    ]

    # Common diseases in Indian men
    common_diseases_men = [
        'Diabetes', 'Hypertension', 'Heart Disease', 'Liver Disease', 'Obesity', 
        'Cancer', 'Tuberculosis', 'Kidney Disease', 'Stroke', 'Depression'
    ]

    # Generate disease column
    disease = []
    for i in range(num_records):
        if is_medical_condition[i] == 'yes' and gender[i] == 'female':
            disease.append(random.choice(common_diseases_women))
        elif is_medical_condition[i] == 'yes' and gender[i] == 'male':
            disease.append(random.choice(common_diseases_men))
        else:
            disease.append('None')

    # Marital status
    marital_status = np.random.choice(['married', 'single'], num_records)

    # Profession common in India
    professions = ['Teacher', 'Engineer', 'Doctor', 'Farmer', 'Shopkeeper', 'Nurse', 'Software Developer', 'Business']
    profession = np.random.choice(professions, num_records)

    # Job type: sitting, field, mixed
    job_type = np.random.choice(['salried', 'self_employed', 'business', "un-employed"], num_records)

    # Body fat percentage: random realistic numbers 10-40%
    #if wieght between 50 to 70 then body_fat_percentage in between [20-30] 
    # if weight between 70-90 then body_fat_percentage[30-35] 
    # if weight between 90-120 then body_fat_percentage in between [35-40]
    for i in range(num_records):
        if weight[i] < 50:
            body_fat_percentage = np.random.uniform(10, 20, num_records).round(1)
        elif 50 <= weight[i] <= 70:
            body_fat_percentage = np.random.uniform(20, 30, num_records).round(1)
        elif 70 < weight[i] <= 90:
            body_fat_percentage = np.random.uniform(30, 35, num_records).round(1)
        elif 90 < weight[i] <= 120:
            body_fat_percentage = np.random.uniform(35, 40, num_records).round(1)
    # if 50 <= weight <= 70:
    #     body_fat_percentage = np.random.uniform(20, 30, num_records).round
    # elif 70 <= weight <= 90:
    #     body_fat_percentage = np.random.uniform(30, 35, num_records).round(1) # men: 10-50: women # 20-50
    # elif 90 < weight <= 120:
    #     body_fat_percentage = np.random.uniform(35, 40, num_records).round(1)

    # Visceral fat percentage: random realistic numbers 1-20
    visceral_fat_percent = np.random.uniform(1, 20, num_records).round(1) # 2 min - 30 max

    # Locations in Mumbai
    locations = [
        'Mumbai', 'Pune', 'Nagpur', 'Nashik', 'Thane', 'Aurangabad', "Navi Mumbai", "Bhiwandi", "Kalyan"]

    location = np.random.choice(locations, num_records)

    # Target weight loss: random numbers 1-20 kg
    target_weight_loss = np.random.randint(2, 50, num_records) # 2 - 50 

    # Work stress level 1-10
    work_stress_level = np.random.randint(1, 10, num_records)

    # Physical activeness: Low, Moderate, High
    physical_activeness = np.random.choice(['Low', 'Moderate', 'High'], num_records)

    # Create DataFrame
    df = pd.DataFrame({
        'age': age,
        'weight': weight,
        'height': height,
        'bmi': bmi,
        'gender': gender,
        'is_medical_condition': is_medical_condition,
        'disease': disease,
        'marital_status': marital_status,
        'profession': profession,
        'job_type': job_type,
        'body_fat_percentage': body_fat_percentage,
        'visceral_fat_percent': visceral_fat_percent,
        'location': location,
        'target_weight_loss': target_weight_loss,
        'work_stress_level': work_stress_level,
        'physical_activeness': physical_activeness
    })

    # Export to Excel
    df.to_csv('client_data.csv', index=False)
    print("Excel file generated successfully!")
#generate_dataset()



def calculate_probability_to_buy_service(row):
    score = 0.0
    
    # BMI
    if row['bmi'] > 30:
        score += 0.6
    elif 20 <= row['bmi'] <= 30:
        score += 0.4
    elif 18 <= row['bmi'] < 20:
        score += 0.2
    elif row['bmi'] < 18:
        score -= 0.9

    # Job type
    job = row['job_type'].lower()
    if job == 'business':
        score += 0.6
    elif job == 'unemployed':
        score -= 0.5
    elif job in ['salaried', 'self_employed']:
        score += 0.4

    # Medical condition
    med = str(row['is_medical_condition']).lower()
    if med == 'yes':
        score += 0.6
    else:
        score -= 0.4

    # Target weight loss
    twl = row['target_weight_loss']
    if 2 <= twl < 5:
        score -= 0.3
    elif 5 <= twl < 10:
        score += 0.2
    elif 10 <= twl < 20:
        score += 0.4
    elif twl >= 20:
        score += 0.8

    # Age
    age = row['age']
    if 18 <= age < 25:
        score -= 0.3
    elif 25 <= age < 35:
        score -= 0.1
    elif 35 <= age < 45:
        score += 0.3
    elif 45 <= age < 55:
        score += 0.5
    elif age >= 55:
        score += 0.8

    # Body fat percentage
    bfp = row['body_fat_percentage']
    if 10 <= bfp < 15:
        score -= 0.5
    elif 15 <= bfp < 20:
        score -= 0.2
    elif 20 <= bfp < 25:
        score += 0.2
    elif 25 <= bfp < 30:
        score += 0.3
    elif bfp >= 30:
        score += 0.5


    # Work stress level
    wsl = row['work_stress_level']
    if 1 <= wsl <= 3:
        score -= 0.2
    elif 4 <= wsl <= 6:
        score += 0.1
    elif 7 <= wsl <= 8:
        score += 0.2
    elif 9 <= wsl <= 10:
        score += 0.2

    # Physical activeness
    pa = str(row['physical_activeness']).lower()
    if pa == 'low':
        score += 0.2
    elif pa == 'moderate':
        score -= 0.2
    elif pa == 'high':
        score -= 0.3

    # Location
    loc = str(row['location']).lower()
    if loc in ['mumbai', 'thane']:
        score += 0.2
    elif loc in ['pune', 'nashik', 'solapur', 'aurangabad', 'nagpur']:
        score -= 0.6
    elif loc in ['navi mumbai', 'kalyan']:
        score -= 0.1
    elif loc == 'bhiwandi':
        score -= 0.2

    # Cap the score between 0.0 and 1.0
    score = round(score, 1)
    if score > 1.0:
        score = 1.0
    elif score < 0.0:
        score = 0.0

    return score

def load_and_calculate_probability():
    generate_dataset()  # Ensure the dataset is generated first
    # Load your client data CSV file
    df = pd.read_csv("client_data.csv") 

    df['probability_to_buy'] = df.apply(calculate_probability_to_buy_service, axis=1)

    # Save updated Excel
    df.to_csv("client_data_with_score.csv", index=False)
    print("Score column added and csv saved successfully!")

load_and_calculate_probability()


# 1. 30 > BMI = 0.9 
# 2. 25-30 BMI = 0.6
# 3. 18-25 BMI = 0.4

# Job Type: 
# business = 0.9
# unemployed = 0.1
# saleried = 0.6
# self_employed = 0.5

# medical condition: 0.7-0.8
# no medical condition: 0.5

# Location: 

# target weight loss:
# 2-5 kg = 0.2
# 5-10 kg = 0.5
# 10-20 kg = 0.8
# 20+ kg = 0.9


# if BMI > 30 then score =score+ 0.8
# if BMI between 20-30 then score = score+0.6
# if BMI between 18-25 then score = score+0.4

# if job_type is business then score = score+0.8
# if job_type is unemployed then score = score - 0.4
# if job_type is salaried then score = score + 0.5
# if job_type is self_employed then score = score + 0.5

# if medical_condition is yes then score = score +0.7
# if medical_condition is no then score = score - 0.3

# if targent_weight_loss is between 2-5 then score = score - 0.2
# if target_weight_loss is between 5-10 then score = score + 0.3
# if target_weight_loss is between 10-20 then score = score + 0.5
# if target_weight_loss is above 20 then score = score + 0.8

# if age is between 18-25 then score = score - 0.2
# if age is between 25-35 then score = score + 0.1
# if age is between 35-45 then score = score + 0.4
# if age is between 45-55 then score = score + 0.6
# if age is above 55 then score = score + 0.8

# if body_fat_percentage is between 10-15 then score = score - 0.5
# if body_fat_percentage is between 15-20 then score = score - 0.2
# if body_fat_percentage is between 20-25 then score = score + 0.2
# if body_fat_percentage is between 25-30 then score = score + 0.3
# if body_fat_percentage is above 30 then score = score + 0.5

# if visceral_fat_percent is between 1-5 then score = score - 0.5
# if visceral_fat_percent is between 5-10 then score = score - 0.2
# if visceral_fat_percent is between 10-15 then score = score + 0.2
# if visceral_fat_percent is between 15-20 then score = score + 0.3
# if visceral_fat_percent is above 20 then score = score + 0.5

# if work_stress_level is between 1-3 then score = score - 0.2
# if work_stress_level is between 4-6 then score = score + 0.1
# if work_stress_level is between 7-8 then score = score + 0.2
# if work_stress_level is between 9-10 then score = score + 0.4

# if physical_activeness is low then score = score + 0.2
# if physical_activeness is moderate then score = score + 0.1
# if physical_activeness is high then score = score - 0.3


# if location is Mumbai and Thane then score = score + 0.3
# if location is pune, nashik, Solarpur , Aurangabad and nagpur then score = score - 0.7
# if location is  Navi Mumbai and kalyan then score = score - 0.1
# if location is Bhiwandi then score = score - 0.2

