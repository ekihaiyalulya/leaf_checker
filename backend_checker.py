from __future__ import division, print_function

import sys, os, glob, re
import numpy as np

from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

import flask
from flask import request
import pandas as pd
import tensorflow as tf
import keras
import numpy as np
import random
import os
from os.path import join, dirname, realpath
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from flask_ngrok import run_with_ngrok
from werkzeug.utils import secure_filename

from pyngrok import ngrok
ngrok.set_auth_token("2OPLwHC1DlwnMMKNK9vi9RFTw4r_EwSrAZbWiR25Hnd2M23J")

app = Flask(__name__)

# !ngrok authtoken 2LonMZbaS41s6CASLcEM7yJ8kdQ_VJBpynu3ShKjaVsHuQBK

model = tf.keras.models.load_model('model_checker.h5')
run_with_ngrok(app)


@app.route('/', methods=['GET'])
def index():
    return "<center><div><h1>Backend Checker is Online!</h1></div></center>"


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    data = {"success": False}
    namaFile = ''
    if request.method == 'POST':
        file = request.files['file']

        if file.filename == '':
            print('Tidak ada file')

        else:
            print('File berhasil di simpan')
            filename = secure_filename(file.filename)
            file.save('data_test/' + file.filename)
            namaFile = 'data_test/' + file.filename

            img = load_img(namaFile, target_size=(150, 150))
            x = img_to_array(img)
            x = x.reshape((1,) + x.shape)
            x = x / 255.0
            predict = model.predict(x)
            temp = 0
            all_label = []
            label = 0
            hasil = []
            objek = ''
            for y in range(2):
                persentase = predict[0][y] * 100
                # print(persentase)
                all_label.append(round(persentase, 2))
                hasil.append(round(predict[0][y]*100, 2))

                if persentase > temp:
                    temp = persentase
                    label = y

            if label == 0:
                objek = 'daun'
            elif label == 1:
                objek = 'unknown'

            data['success'] = True
            data['label'] = label
            data['acc'] = temp
            data['objek'] = objek
            data['all_label'] = all_label

        print(data)
        return flask.jsonify(data)
    else:
        return '<h1>Method Salah</h1>'


app.run()
