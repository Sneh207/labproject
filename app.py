from flask import Flask, render_template, request
from rules import heart_attack_indicator  # Import the function from rules.py

app = Flask(__name__)

# Route to the input form
@app.route('/')
def index():
    return render_template('index.html')

# Route to display the result
@app.route('/result', methods=['POST'])
def result():
    heart_rate = int(request.form['heart_rate'])
    blood_pressure_sys = int(request.form['blood_pressure_sys'])
    exercise_level = int(request.form['exercise_level'])
    cholesterol = int(request.form['cholesterol'])
    age = int(request.form['age'])
    sex = (request.form['sex'])  # 1 for male, 0 for female
    smoking_status = (request.form['smoking_status'])  # 1 for Yes, 0 for No
    diabetes_status = (request.form['diabetes_status'])  # 1 for Yes, 0 for No
    family_history = (request.form['family_history'])  # 1 for Yes, 0 for No
    weight = float(request.form['weight'])
    height = float(request.form['height'])

    result = heart_attack_indicator(
        heart_rate, blood_pressure_sys, exercise_level, cholesterol, age, sex,
        smoking_status, diabetes_status, family_history, weight, height
    )

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
