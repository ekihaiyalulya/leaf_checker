{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Back-end Checker"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Instalasi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pyngrok in c:\\users\\acer\\anaconda3\\lib\\site-packages (5.2.1)\n",
      "Requirement already satisfied: PyYAML in c:\\users\\acer\\anaconda3\\lib\\site-packages (from pyngrok) (5.4.1)\n",
      "Requirement already satisfied: gevent in c:\\users\\acer\\anaconda3\\lib\\site-packages (21.1.2)\n",
      "Requirement already satisfied: greenlet<2.0,>=0.4.17 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from gevent) (1.0.0)\n",
      "Requirement already satisfied: zope.event in c:\\users\\acer\\anaconda3\\lib\\site-packages (from gevent) (4.5.0)\n",
      "Requirement already satisfied: setuptools in c:\\users\\acer\\anaconda3\\lib\\site-packages (from gevent) (52.0.0.post20210125)\n",
      "Requirement already satisfied: zope.interface in c:\\users\\acer\\anaconda3\\lib\\site-packages (from gevent) (5.3.0)\n",
      "Requirement already satisfied: cffi>=1.12.2 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from gevent) (1.14.5)\n",
      "Requirement already satisfied: pycparser in c:\\users\\acer\\anaconda3\\lib\\site-packages (from cffi>=1.12.2->gevent) (2.20)\n",
      "Requirement already satisfied: flask in c:\\users\\acer\\anaconda3\\lib\\site-packages (1.1.2)\n",
      "Requirement already satisfied: Jinja2>=2.10.1 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from flask) (2.11.3)\n",
      "Requirement already satisfied: itsdangerous>=0.24 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from flask) (1.1.0)\n",
      "Requirement already satisfied: click>=5.1 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from flask) (7.1.2)\n",
      "Requirement already satisfied: Werkzeug>=0.15 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from flask) (1.0.1)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from Jinja2>=2.10.1->flask) (1.1.1)\n",
      "Requirement already satisfied: keras in c:\\users\\acer\\anaconda3\\lib\\site-packages (2.11.0)\n",
      "Requirement already satisfied: numpy in c:\\users\\acer\\anaconda3\\lib\\site-packages (1.20.1)\n",
      "Requirement already satisfied: pandas in c:\\users\\acer\\anaconda3\\lib\\site-packages (1.2.4)\n",
      "Requirement already satisfied: python-dateutil>=2.7.3 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from pandas) (2.8.1)\n",
      "Requirement already satisfied: numpy>=1.16.5 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from pandas) (1.20.1)\n",
      "Requirement already satisfied: pytz>=2017.3 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from pandas) (2021.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from python-dateutil>=2.7.3->pandas) (1.15.0)\n",
      "Requirement already satisfied: flask-ngrok in c:\\users\\acer\\anaconda3\\lib\\site-packages (0.0.25)\n",
      "Requirement already satisfied: Flask>=0.8 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from flask-ngrok) (1.1.2)\n",
      "Requirement already satisfied: requests in c:\\users\\acer\\anaconda3\\lib\\site-packages (from flask-ngrok) (2.25.1)\n",
      "Requirement already satisfied: Jinja2>=2.10.1 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from Flask>=0.8->flask-ngrok) (2.11.3)\n",
      "Requirement already satisfied: click>=5.1 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from Flask>=0.8->flask-ngrok) (7.1.2)\n",
      "Requirement already satisfied: itsdangerous>=0.24 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from Flask>=0.8->flask-ngrok) (1.1.0)\n",
      "Requirement already satisfied: Werkzeug>=0.15 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from Flask>=0.8->flask-ngrok) (1.0.1)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from Jinja2>=2.10.1->Flask>=0.8->flask-ngrok) (1.1.1)\n",
      "Requirement already satisfied: idna<3,>=2.5 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from requests->flask-ngrok) (2.10)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from requests->flask-ngrok) (2020.12.5)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from requests->flask-ngrok) (1.26.4)\n",
      "Requirement already satisfied: chardet<5,>=3.0.2 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from requests->flask-ngrok) (4.0.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pyngrok\n",
    "!pip install gevent\n",
    "!pip install flask\n",
    "!pip install keras\n",
    "!pip install numpy\n",
    "!pip install pandas\n",
    "!pip install flask-ngrok"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: tensorflow in c:\\users\\acer\\anaconda3\\lib\\site-packages (2.11.0)\n",
      "Requirement already satisfied: tensorflow-intel==2.11.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow) (2.11.0)\n",
      "Requirement already satisfied: google-pasta>=0.1.1 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (0.2.0)\n",
      "Requirement already satisfied: h5py>=2.9.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (2.10.0)\n",
      "Requirement already satisfied: tensorboard<2.12,>=2.11 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (2.11.2)\n",
      "Requirement already satisfied: libclang>=13.0.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (15.0.6.1)\n",
      "Requirement already satisfied: termcolor>=1.1.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (2.2.0)\n",
      "Requirement already satisfied: typing-extensions>=3.6.6 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (3.7.4.3)\n",
      "Requirement already satisfied: setuptools in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (52.0.0.post20210125)\n",
      "Requirement already satisfied: tensorflow-io-gcs-filesystem>=0.23.1 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (0.30.0)\n",
      "Requirement already satisfied: absl-py>=1.0.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (1.4.0)\n",
      "Requirement already satisfied: flatbuffers>=2.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (23.1.21)\n",
      "Requirement already satisfied: numpy>=1.20 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (1.20.1)\n",
      "Requirement already satisfied: tensorflow-estimator<2.12,>=2.11.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (2.11.0)\n",
      "Requirement already satisfied: six>=1.12.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (1.15.0)\n",
      "Requirement already satisfied: gast<=0.4.0,>=0.2.1 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (0.4.0)\n",
      "Requirement already satisfied: astunparse>=1.6.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (1.6.3)\n",
      "Requirement already satisfied: packaging in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (20.9)\n",
      "Requirement already satisfied: keras<2.12,>=2.11.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (2.11.0)\n",
      "Requirement already satisfied: grpcio<2.0,>=1.24.3 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (1.51.1)\n",
      "Requirement already satisfied: wrapt>=1.11.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (1.12.1)\n",
      "Requirement already satisfied: opt-einsum>=2.3.2 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (3.3.0)\n",
      "Requirement already satisfied: protobuf<3.20,>=3.9.2 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorflow-intel==2.11.0->tensorflow) (3.19.6)\n",
      "Requirement already satisfied: wheel<1.0,>=0.23.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from astunparse>=1.6.0->tensorflow-intel==2.11.0->tensorflow) (0.36.2)\n",
      "Requirement already satisfied: tensorboard-data-server<0.7.0,>=0.6.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (0.6.1)\n",
      "Requirement already satisfied: google-auth-oauthlib<0.5,>=0.4.1 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (0.4.6)\n",
      "Requirement already satisfied: google-auth<3,>=1.6.3 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (2.16.0)\n",
      "Requirement already satisfied: markdown>=2.6.8 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (3.4.1)\n",
      "Requirement already satisfied: requests<3,>=2.21.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (2.25.1)\n",
      "Requirement already satisfied: werkzeug>=1.0.1 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (1.0.1)\n",
      "Requirement already satisfied: tensorboard-plugin-wit>=1.6.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (1.8.1)\n",
      "Requirement already satisfied: rsa<5,>=3.1.4 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from google-auth<3,>=1.6.3->tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (4.9)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from google-auth<3,>=1.6.3->tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (0.2.8)\n",
      "Requirement already satisfied: cachetools<6.0,>=2.0.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from google-auth<3,>=1.6.3->tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (5.3.0)\n",
      "Requirement already satisfied: requests-oauthlib>=0.7.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (1.3.1)\n",
      "Requirement already satisfied: importlib-metadata>=4.4 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from markdown>=2.6.8->tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (6.0.0)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from importlib-metadata>=4.4->markdown>=2.6.8->tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (3.4.1)\n",
      "Requirement already satisfied: pyasn1<0.5.0,>=0.4.6 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from pyasn1-modules>=0.2.1->google-auth<3,>=1.6.3->tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (0.4.8)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (1.26.4)\n",
      "Requirement already satisfied: idna<3,>=2.5 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (2.10)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (2020.12.5)\n",
      "Requirement already satisfied: chardet<5,>=3.0.2 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from requests<3,>=2.21.0->tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (4.0.0)\n",
      "Requirement already satisfied: oauthlib>=3.0.0 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib<0.5,>=0.4.1->tensorboard<2.12,>=2.11->tensorflow-intel==2.11.0->tensorflow) (3.2.2)\n",
      "Requirement already satisfied: pyparsing>=2.0.2 in c:\\users\\acer\\anaconda3\\lib\\site-packages (from packaging->tensorflow-intel==2.11.0->tensorflow) (2.4.7)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install tensorflow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pillow in c:\\users\\acer\\anaconda3\\lib\\site-packages (8.2.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pillow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "from __future__ import division, print_function\n",
    "\n",
    "import sys, os, glob, re\n",
    "import numpy as np\n",
    "\n",
    "from keras.applications.imagenet_utils import preprocess_input, decode_predictions\n",
    "from keras.models import load_model\n",
    "from keras.preprocessing import image\n",
    "\n",
    "from flask import Flask, redirect, url_for, request, render_template\n",
    "from werkzeug.utils import secure_filename\n",
    "from gevent.pywsgi import WSGIServer\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import flask\n",
    "from flask import request\n",
    "import pandas as pd\n",
    "import tensorflow as tf\n",
    "import keras\n",
    "import numpy as np\n",
    "import random\n",
    "import os\n",
    "from os.path import join, dirname, realpath\n",
    "from tensorflow.keras.preprocessing.image import img_to_array, load_img\n",
    "from flask_ngrok import run_with_ngrok\n",
    "from werkzeug.utils import secure_filename"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Run NGROK"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [16/May/2023 22:15:50] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Running on http://2dfb-2001-448a-1082-8be4-541e-8f78-7217-dd71.ngrok-free.app\n",
      " * Traffic stats available on http://127.0.0.1:4040\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "127.0.0.1 - - [16/May/2023 22:16:03] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [16/May/2023 22:16:40] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [16/May/2023 22:17:40] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n"
     ]
    }
   ],
   "source": [
    "from pyngrok import ngrok\n",
    "ngrok.set_auth_token(\"2OPLwHC1DlwnMMKNK9vi9RFTw4r_EwSrAZbWiR25Hnd2M23J\")\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# !ngrok authtoken 2LonMZbaS41s6CASLcEM7yJ8kdQ_VJBpynu3ShKjaVsHuQBK\n",
    "\n",
    "model = tf.keras.models.load_model('model_checker.h5')\n",
    "run_with_ngrok(app)\n",
    "\n",
    "@app.route('/', methods=['GET'])\n",
    "def index():\n",
    "  return \"<center><div><h1>Backend Checker is Online!</h1><image src='https://thumbs.gfycat.com/InfiniteRemarkableDesertpupfish-size_restricted.gif' ></image></div></center>\"\n",
    "\n",
    "@app.route('/predict', methods=['GET', 'POST'])\n",
    "def upload():\n",
    "  data = {\"success\": False}\n",
    "  namaFile = ''\n",
    "  if request.method == 'POST':\n",
    "    file = request.files['file']\n",
    "\n",
    "    if file.filename == '':\n",
    "      print('Tidak ada file') \n",
    "\n",
    "    else:\n",
    "      print('File berhasil di simpan')  \n",
    "      filename = secure_filename(file.filename)\n",
    "      file.save('data_test/' + file.filename)\n",
    "      namaFile = 'data_test/' + file.filename\n",
    "\n",
    "      img = load_img(namaFile, target_size=(150, 150))\n",
    "      x = img_to_array(img)\n",
    "      x = x.reshape((1,) + x.shape)\n",
    "      x = x / 255.0\n",
    "      predict = model.predict(x)\n",
    "      temp = 0\n",
    "      all_label = []\n",
    "      label = 0\n",
    "      hasil = []\n",
    "      objek = ''\n",
    "      for y in range(1):\n",
    "        persentase = predict[0][y] * 100\n",
    "        # print(persentase)\n",
    "        all_label.append(round(persentase , 2))\n",
    "        hasil.append(round(predict[0][y]*100,2))\n",
    "\n",
    "        if persentase > temp:\n",
    "          temp = persentase\n",
    "          label = y\n",
    "      \n",
    "      if label == 0:\n",
    "        objek = 'daun'\n",
    "      elif label == 1:\n",
    "        objek = 'unknown'\n",
    "\n",
    "      data['success'] = True\n",
    "      data['label'] = label\n",
    "      data['acc'] = temp\n",
    "      data['objek'] = objek\n",
    "      data['all_label'] = all_label\n",
    "\n",
    "    print(data)\n",
    "    return flask.jsonify(data)\n",
    "  else:\n",
    "    return '<h1>Method Salah</h1>'\n",
    "\n",
    "app.run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "23bf0724a01b6ea9814e66f76182ea78c0ee849a72ca257c0e116bf83bb4960a"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
