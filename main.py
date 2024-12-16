#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mlflow
import subprocess

if __name__ = "__main__":    
    with
    mlflow.start_run(run_name="housing_pipeline")as parent_run:
        #Start child run for data preparation
        with
        mlflow.start_run(run_name="data_prep",nested=True):
            subprocess.run(["python","data_prep.py"])
            
            #Start child run for model training
            with
            mlflow.start_run(run_name="train",nested=True):
                subprocess.run(["python","data_prep.py"])
                #Start child run for model training
                with
                mlflow.start_run(run_name="train",nested=True):
                    subprocess.run(["python","train.py"])
                    
                    #Start child run for model scoring
                    with
                    mlflow.start_run(run_name='score',nested=True):
                        subprocess.run(["python","score.py"])
                        print(f"Pipeline completed, main run-id; {parent_run.info.run_id}"")
    

