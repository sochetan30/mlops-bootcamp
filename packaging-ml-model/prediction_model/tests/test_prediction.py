import pytest 
import os
import sys
from pathlib import Path
from sklearn.pipeline import Pipeline
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import generate_prediction



#Fixtures: functions run before test functions

@pytest.fixture
def single_prediction():
    test_dataset = load_dataset(config.TEST_FILE)
    single_row = test_dataset[:1]
    result = generate_prediction(single_row)
    return result

def test_single_pred_not_none(single_prediction): # output is not none
    assert single_prediction is not None

def test_single_pred_str_type(single_prediction):
    assert isinstance(single_prediction.get('Predictions')[0], str)

def test_single_pred_validate(single_prediction): # check the output is Y
    assert single_prediction.get('Predictions')[0] == 'Y'