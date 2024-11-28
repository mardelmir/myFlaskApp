from flask import Flask, jsonify, request
import numpy as np
import os
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

# os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config['DEBUG'] = True

# Enruta la landing page (endpoint /)

# Enruta la funcion al endpoint /api/v1/predict


# Enruta la funcion al endpoint /api/v1/retrain

app.run()