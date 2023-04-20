from flask import Flask, render_template, request
import pickle
import numpy as np

# setup application
app = Flask(__name__)

def prediction(list):
    with open ('templates\model\predictor.pickle', 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([list])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    # return "Hello World"
    pred_value = 0
    if request.method == 'POST':
        age = request.form['age']
        gender = request.form['gender']
        BMI = request.form['BMI']
        Children = request.form['Children']
        smoke = request.form['smoke']
        Region = request.form['Region']

        feature_list = []
        feature_list.append(int(age))
        feature_list.append(int(gender))
        feature_list.append(float(BMI))
        feature_list.append(int(Children))
        feature_list.append(int(smoke))
        feature_list.append(int(Region))

        pred_value = prediction(feature_list)

    return render_template('index.html', pred_value = pred_value)


if __name__ == '__main__':
    app.run(debug=True)