conda create -n jenkins-env python=3.10 -y



docker build -t loan_pred:v1 .
docker build -t chetan123456789/cicd:latest . 
docker push chetan123456789/cicd:latest

docker run -d -it --name modelv1 -p 8005:8005 chetan123456789/cicd:latest bash

docker exec modelv1 python prediction_model/training_pipeline.py

docker exec modelv1 pytest -v --junitxml TestResults.xml --cache-clear

docker cp modelv1:/code/src/TestResults.xml .

docker exec -d -w /code modelv1 python main.py

docker exec -d -w /code modelv1 uvicorn main:app --proxy-headers --host 0.0.0.0 --port 8005

