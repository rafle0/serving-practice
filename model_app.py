from flask import Flask
from flask import request, jsonify

import tensorflow as tf
import numpy as np
import json

app = Flask(__name__)

model = tf.keras.models.load_model('./model/1/')
label=['pneumonia_bac', 'covid', 'normal']

@app.route("/")
def hello():
    return "api test!"

@app.route("/test", methods=['POST'])
def predict():
    img_data = request.get_json()
    img = np.array(img_data['instances'])
    answer = model.predict(img)
    
    return json.dumps({"instances": answer.tolist(), "label": label[np.argmax(answer)]})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)