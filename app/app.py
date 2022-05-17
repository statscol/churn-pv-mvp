
from typing import List
from schemas import ChurnResponse,Client
from fastapi import FastAPI, File, HTTPException, Form
import time
from datetime import datetime
from config import *
import pickle
import pandas as pd
import numpy as np


with open("models/xgbmodel_nopca.pickle", 'rb') as f:
    xgb = pickle.load(f)

app = FastAPI(name="Detección de Churn",title="Herramienta Analítica de Churn", description="API para detección de churn", version="0.1")

@app.get("/",tags=['test'])
async def initialize():
    return {'message':'base endpoint, use /api/v1/churn'}

@app.post("/api/v1/churn", tags=["churn detector"], response_model=ChurnResponse)
async def predict_churn(client: Client) -> ChurnResponse:
        cli_df=pd.DataFrame([client.dict()])
        probability_churn=xgb.predict_proba(cli_df)[:,1][0]
        result=ChurnResponse(Asegurado__c=client.Asegurado__c,CodigoTipoAsegurado__c=client.CodigoTipoAsegurado__c,churn_probability=probability_churn)
        return result

