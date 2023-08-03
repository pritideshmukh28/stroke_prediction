from flask import Flask, request, jsonify, render_template
from utils import Stroke
import config

app = Flask(__name__)
@app.route('/')
def home():

    return render_template('stroke_prediction.html')

@app.route('/stroke_prediction', methods = ['GET', 'POST'])
def prediction():

    if request.method == 'GET':
        data = request.args.get
        print("Data :",data)

        gender = data('gender')
        age = eval(data('age'))
        hypertension = eval(data('hypertension'))
        heart_disease = eval(data('heart_disease'))
        ever_married = data('ever_married')
        Residence_type = data('Residence_type')
        avg_glucose_level = eval(data('avg_glucose_level'))
        bmi = eval(data('bmi'))
        work_type = data('work_type')
        smoking_status = data('smoking_status')

        Obj = Stroke(gender,age,hypertension,heart_disease,ever_married,Residence_type,avg_glucose_level,bmi,work_type,smoking_status)
        stroke = Obj.get_prediction()
        
        if stroke == 1:
            return render_template('stroke_prediction.html', prediction = 'The Patient Suffers from a Stroke')
        elif stroke == 0:
            return render_template('stroke_prediction.html', prediction = 'The Patient does not Suffer from a Stroke')
    elif request.method == 'POST':
        data = request.form
        print("Data :",data)

        gender = data['gender']
        age = data['age']
        hypertension = data['hypertension']
        heart_disease = data['heart_disease']
        ever_married = data['ever_married']
        Residence_type = data['Residence_type']
        avg_glucose_level = data['avg_glucose_level']
        bmi = data['bmi']
        work_type = data['work_type']
        smoking_status = data['smoking_status']

        Obj = Stroke(gender,age,hypertension,heart_disease,ever_married,Residence_type,avg_glucose_level,bmi,work_type,smoking_status)
        stroke = Obj.get_prediction()

        return jsonify({"Result":f"Predicted Medical Charges == {stroke}"})
        #return render_template('stroke_prediction.html', prediction = stroke)

    return jsonify({"Message" : "Unsuccessful"})
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)    
   

        