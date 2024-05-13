import pandas as pd
import numpy as np
import joblib

from pathlib import Path
import os
import sys
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config
from prediction_model.processing.data_handling import load_pipeline,load_dataset



classification_pipeline = load_pipeline(pipeline_to_load=config.MODEL_NAME)
#/Users/chetu/Learning/mlops/mlops-bootcamp/packaging-ml-model/prediction_model/trained_model/classification.pkl


# def generate_prediction(data_input):
#     data = pd.DataFrame(data_input)
#     pred = classification_pipeline.predict(data[config.FEATURES])
#     output = np.where(pred==1,'Y','N')
#     result = {'Predictions :',output}
#     return result


def generate_prediction(data_input):
    data = pd.DataFrame(data_input)
    pred = classification_pipeline.predict(data[config.FEATURES])  # Use predict() method
    output = np.where(pred == 1, 'Y', 'N')
    result = {'Predictions': tuple(output)}
    return result



#Prelimenery testing

# def generate_prediction(data_input):
#     test_data = load_dataset(config.TEST_FILE)
#     pred = classification_pipeline(test_data[config.FEATURES])
#     output = np.where(pred==1,'Y','N')
#     #result = {'Predictions :',output}
#     return output

if __name__ == '__main__':
    generate_prediction()