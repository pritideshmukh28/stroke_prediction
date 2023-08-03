import pickle
import json
import numpy as np
import config

class Stroke():
    def __init__(self,gender,age,hypertension,heart_disease,ever_married,Residence_type,avg_glucose_level,bmi,work_type,smoking_status):
        print("****** INIT Function *********")
        
        self.gender = gender
        self.age = age
        self.hypertension = hypertension
        self.heart_disease = heart_disease
        self.ever_married = ever_married
        self.Residence_type = Residence_type
        self.avg_glucose_level = avg_glucose_level
        self.bmi = bmi
        self.work_type = work_type
        self.smoking_status = smoking_status

    def __load_saved_data(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_prediction(self):
        self.__load_saved_data()

        gender = self.json_data['gender'][self.gender]
        ever_married = self.json_data['ever_married'][self.ever_married]
        Residence_type = self.json_data['Residence_type'][self.Residence_type]

        work_type = 'work_type_'+self.work_type
        smoking_status = 'smoking_status_'+self.smoking_status

        work_type_index = self.json_data['column_names'].index(work_type)
        smoking_status_index = self.json_data['column_names'].index(smoking_status)


        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = gender
        test_array[0,1] = self.age
        test_array[0,2] = self.hypertension
        test_array[0,3] = self.heart_disease
        test_array[0,4] = ever_married
        test_array[0,5] = Residence_type
        test_array[0,6] = self.avg_glucose_level
        test_array[0,7] = self.bmi
        test_array[0,work_type_index] = 1
        test_array[0,smoking_status_index] = 1

        predicted_stroke = self.model.predict(test_array)[0]
        return predicted_stroke