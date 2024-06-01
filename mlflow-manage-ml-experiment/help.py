import mlflow

mlflow.set_tracking_uri("https://localhost:5000")

exp_id=mlflow.create_experiment("Loan_Prediction")


with mlflow.start_run(run_name='DecisionTreeClass') as run:
    mlflow.set_tag("version","1.0.0")
    pass

mlflow.end_run()
n_estimator=10
criterion='gini'

mlflow.log_param('n_estimator',n_estimator)
mlflow.log_param('criterion',criterion)

mlflow.log_metric('accuracy',0.9)