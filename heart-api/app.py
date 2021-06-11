import numpy as np
import pickle
import pandas as pd

from flask import Flask, request, jsonify, render_template, abort
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

# region Predict
@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    data = request.get_json(force=True)
    if not data or not 'age' in data:
        abort(400)
    print(data)

    try:
        age = data['age']
        sex = data['sex']
        cp = data['cp']
        trestbps = data['trestbps']
        chol = data['chol']
        fbs = data['fbs']
        restecg = data['restecg']
        thalach = data['thalach']
        exang = data['exang']
        oldpeak = data['oldpeak']
        slope = data['slope']
        ca = data['ca']
        thal = data['thal']
    except:
        return jsonify({'message': 'Something went wrong while reading data'}), 400


    try:
        model = pickle.load(open("heart_attack.pickle", 'rb'))
        scaler = pickle.load(open("scaler_data.pickle", 'rb'))
        data = pickle.load(open("data.pickle", 'rb'))
    except:
        return jsonify({'message': 'Unable to load model'}), 400

    df_new = pd.DataFrame(
        columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
                 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'],
        data=[[age,	sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak,	slope, ca, thal]])

    df_new.slope.fillna(data.slope.mode()[0], inplace=True)
    df_new.fbs.fillna(data.fbs.mode()[0], inplace=True)
    df_new.exang.fillna(data.exang.mode()[0], inplace=True)
    df_new.ca.fillna(data.ca.mode()[0], inplace=True)
    df_new.thal.fillna(data.thal.mode()[0], inplace=True)
    df_new.trestbps.fillna(data.trestbps.mean(), inplace=True)
    df_new.chol.fillna(data.chol.mean(), inplace=True)
    df_new.thalach.fillna(data.thalach.mean(), inplace=True)
    df_new.oldpeak.fillna(data.oldpeak.mean(), inplace=True)

    df_new['sex'] = df_new['sex'].replace(['Male'], 0.682119)
    df_new['sex'] = df_new['sex'].replace(['Female'], 0.317881)

    ready = df_new.to_numpy()
    ready = scaler.transform(ready)

    prediction = model.predict(ready.reshape(1, -1))

    return jsonify({'prediction': prediction[0]}), 200
# endregion


if __name__ == "__main__":
    app.run(debug=True)
