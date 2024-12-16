#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mlflow
from sklearn.linear_model import
LinearRegression

def train_model(train_data_path):
    #Your model training logic
    model = LinearRegression()
    #Train your model
    model.fit(X_train,y_train)
    
    return model
if __name__ == "__main__":
    #Start an MLFlow run for model training
    with
    mlflow.start_run(run_name="train") as run:
    mlflow.log_param("train_data_path","data/cleaned.csv")
    model = train_model("data/cleaned.csv")
    #Save model
    mlflow.sklearn.log_model(model,"linear_regression_model")
    print(f"Model training complete, run-id: {run.info.run_id}")

