import io
import os
from pathlib import Path
from setuptools import setup,find_packages

# Metadata of package
NAME = 'prediction_model'
DESCRIPTION = 'Loan Prediction Model'
URL = 'https://github.com/sochetan30'
EMAIL = 'chetantrust30@gmail.com'
AUTHOR = 'Chetan'
REQUIRE_PYTHON = '>=3.7.0'

pwd = os.path.abspath(os.path.dirname(__file__))

#Get the list of package to be installed

def list_reqs(fname='requirements.txt'):
    with io.open(os.path.join(pwd,fname),encoding='utf-8') as f:
        return f.read().splitlines()
    


try:
    with io.open(os.path.join(pwd,'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()

except FileNotFoundError:
    long_description= DESCRIPTION

# Load the packages version.py modeule as dictionary:
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR/ NAME
about = {}

with open(PACKAGE_DIR/'VERSIONS') as f:
    _version = f.read().strip()
    about['__version__'] = _version

setup(
    name=NAME,
    version=about['__version__'],
    description= DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRE_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'prediction_model':['VERSION']},
    install_requires=[],
    setup_requires=[],
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: PyPy'
        ]
)