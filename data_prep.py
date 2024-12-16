#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install mlflow


# In[2]:


import mlflow
import pandas as pd


# In[ ]:


def prepare_data(input_path,output_path):
    data = pd.read_csv("C:\\Users\\moumita.chakrabo\Desktop\\mle-training\\housing.csv")
    data.to_csv("C:\\Users\\moumita.chakrabo\\Desktop\\mle-training\\MLFlow_walkthrough")
    
    return outputh_path
if __name__ == '__main__':
    with 
mlflow.start_run(run_name="data_prep")as
run:
    mlflow.log_param("input_path","data/input.csv")
    mlflow.log_param("output_path","data/cleaned.csv")
    
    ouput_path = prepare_data("data/input.csv","data/cleaned.csv")
    mlflow.log_artifact(output_path)
    
    print(f"Data preparation complete, run-id: {run.info.run_id}")

