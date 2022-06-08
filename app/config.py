import os
from typing import List, Dict
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,LabelEncoder, OneHotEncoder,MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.impute import SimpleImputer,KNNImputer
import pickle
import numpy as np


COLS_TO_RENAME={'TipoRamoName':'tipo_ramo_name',
'TipoProdDesc':'tipo_prod_desc',
'TotalProdPrev':'n_prod_prev',
'TotalSiniestros':'total_siniestros',
'TotalPagado__smmlv':'total_pagado_smmlv',
'AniosUltimoSiniestro':'anios_ultimo_siniestro',
'Edad':'edad',
'CiudadName':'ciudad_name'
}

#cargue del modelo
with open("../models/lightgbm.pickle", 'rb') as f:
    lightgbm = pickle.load(f)

with open("../models/logistic.pickle", 'rb') as f:
    logistic = pickle.load(f)

def pred_stack(data,proba=True,thresh=0.5):
    proba_lgb=lightgbm.predict_proba(data)[:,1]
    predict_log=logistic.predict_proba(data)[:,1]
    if proba:
        return np.stack((proba_lgb,predict_log),axis=1).mean(axis=1)
    else:
        return (np.stack((proba_lgb,predict_log),axis=1).mean(axis=1)>thresh).astype(int)