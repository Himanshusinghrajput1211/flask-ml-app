import flask
import sklearn
import numpy

from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load ML model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    return render_template('index.html', prediction_text=f'Predicted Output: {prediction[0]}')

if __name__ == "__main__":
    app.run(debug=True)
