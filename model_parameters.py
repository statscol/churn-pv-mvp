from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,LabelEncoder, OneHotEncoder,MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix,precision_score,recall_score,cohen_kappa_score,accuracy_score,f1_score,roc_auc_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.impute import SimpleImputer,KNNImputer
from catboost import CatBoostClassifier, Pool
import lightgbm as lgb


cb_clf=CatBoostClassifier()
lgbm_clf = lgb.LGBMClassifier()
xgb_clf=GradientBoostingClassifier()
elasticnet_clf=LogisticRegression(class_weight="balanced",max_iter=4000,solver="saga")

MODEL_PARAMS={'xgboost':
                {'param_grid':{
                    "pca__n_components":[10,20],
                    "model__n_estimators":[50,100,250],
                    "model__max_depth":[5,10,20],
                    "model__learning_rate":[0.01],
                    "model__min_samples_split":[2,5],
                    "model__subsample": [0.9,1]

                            }
                },
            "logistic_regression":
                {"param_grid":{
                    "pca__n_components":[10,20],
                    "model__penalty":['elasticnet'],
                    "model__l1_ratio":[0.1,0.3,0.5,0.8,1]    
                }},
            "lightgbm":{"param_grid":{
                'pca__n_components':[5,10,20],
                'model__n_estimators': [100,150,500],
                'model__colsample_bytree': [0.8,0.9],
                'model__max_depth': [10,15],
                'model__num_leaves': [10,50],
                'model__reg_alpha': [0.,1.1,1.2],
                'model__reg_lambda': [0.,1.1,1.2],
#                'model__min_split_gain': [0.3],
                'model__subsample': [0.9,1],
#                'model__subsample_freq': [20]
}}}


MODEL_LIST={'xgboost':xgb_clf,'logistic_regression':elasticnet_clf,'lightgbm':lgbm_clf}