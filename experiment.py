import dagshub
dagshub.init(repo_owner='surjya003', repo_name='MLflow-Basic', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)