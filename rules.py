

def heart_attack_indicator(heart_rate, blood_pressure_sys, exercise_level, cholesterol, age, sex, smoking_status, diabetes_status, family_history, weight, height):
    risk_score = 0
    

    bmi = weight / (height ** 2)
    
    # Heart rate analysis
    if heart_rate > 100:
        risk_score += 10  # High risk
    elif heart_rate < 60:
        risk_score += 5  # Moderate risk
    
    # Blood pressure analysis (Systolic)
    if 120<=blood_pressure_sys<=129:
        risk_score += 5  # High risk (Hypertension)
    elif 130<=blood_pressure_sys<=139:
        risk_score += 12
    elif blood_pressure_sys >= 140:
        risk_score += 20  # High risk (Hypertension)
    elif blood_pressure_sys >= 180:
        risk_score += 27  # Moderate risk

    # Cholesterol analysis
    if cholesterol > 240:
        risk_score += 20  # High risk
    elif 200 < cholesterol <= 239:
        risk_score += 10  # Moderate risk

    # Exercise level
    if exercise_level <= 2:
        risk_score += 10  # Moderate risk (Sedentary lifestyle)

    # Age analysis (higher risk with increasing age)
    if (20<=age<=30):  # Men > 45, Women > 55
        risk_score += 5
    elif 31<=age<=50:
        risk_score += 10
    elif 51<=age<=60:
        risk_score += 15
    elif 61<=age<=75:
        risk_score += 20
    elif age>=76:
        risk_score += 7
    

    # Smoking status
    if smoking_status == 'Yes' or  smoking_status ==  'yes':  # Smoker
        risk_score += 10

    # Diabetes status
    if diabetes_status == 'Yes' or 'yes':
        risk_score += 10  # Higher risk if diabetic

    # Family history of heart disease
    if family_history == 'Parents' :
        risk_score += 10
    elif family_history == 'Sibling' :
        risk_score += 10
    elif family_history =='Others':
        risk_score += 3  # Higher risk if family has history of heart disease

    # BMI analysis
    if bmi >= 30:
        risk_score += 20 # High risk (Obese)
    elif 25 <= bmi < 30:
        risk_score += 10  # Moderate risk (Overweight)

    # Risk assessment based on the total risk score
    if risk_score >= 90:
        return "High risk of heart attack! Seek medical attention."
    elif 40 <= risk_score < 90:
        return "Moderate risk of heart attack. Consider consulting a doctor."
    else:
        return "Low risk of heart attack. Maintain a healthy lifestyle."












