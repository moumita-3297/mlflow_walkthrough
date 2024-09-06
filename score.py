#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mlflow

def score_model(model,test_data_path):
    #Your model scoring logic
    predictions = model.predict(X_test)
    score = model.score(X_test,y_test)
    return score

if __name__ = "__main__":
    #Start an MLflow run for model scoring
    with
    mlflow.start_run(run_name="score") as run:
        mlflow.log_param("test_data_path","data/test.csv")
        #Load your model from previous step
        model = mlflow.sklearn.load_model("runs:/<run_id>/linear_regression_model")
        score = score_model(model,"data/test.csv")
        mlflow.log_metric("score",score)
        print(f"Model scoring complete, run-id: {run.info.run_id}")

