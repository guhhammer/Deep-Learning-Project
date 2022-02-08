#!flask/bin/python
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import tensorflow as tf
import os
from tensorflow import keras
from PIL import Image
import io
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)
CORS(app)

path = os.getcwd()

os.chdir("../Database/cheese_photos")
train_dir = os.getcwd()
train_classes_dirs = []
classes = []
smooth_responses = ["Camembert", "Cheddar", "Cottage", "Edam", "Gorgonzola", "Parmesan", "Swiss"]

for directory in os.listdir():
	train_classes_dirs.append(os.path.join(train_dir, directory))
	classes.append(directory)

os.chdir(path)

@app.route('/api/v1/predict/sample', methods=['POST'])
def predict():
	#if not request.form:
	#	return "400"
	img = request.files.get('file', '')
	test = Image.open(img)
	test = test.resize((128,128))
	test = np.array(test)
	if test.shape[2] == 4:
		test = test[:, :, :3]
	model = keras.models.load_model("model")
	predictions = model.predict([[test]])
	highest = 0
	value = 0
	for item in range(len(predictions[0])):
		if predictions[0][item] > value:
			highest = item
			value = predictions[0][item]
	print(predictions)
	return smooth_responses[int(highest)]


if __name__ == '__main__':
    app.run(debug=True)
