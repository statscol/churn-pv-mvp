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


COLS_TO_RENAME={'TipoRamoName':'tipo_ramo_name',
'TipoProdDesc':'tipo_prod_desc',
'TotalProdPrev':'n_prod_prev',
'TotalSiniestros':'total_siniestros',
'TotalPagado__smmlv':'total_pagado_smmlv',
'AniosUltimoSiniestro':'anios_ultimo_siniestro',
'Edad':'edad',
'CiudadName':'ciudad_name'
}