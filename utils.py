import pandas as pd
import os
import numpy as np
from sklearn.metrics import confusion_matrix,precision_score,recall_score,cohen_kappa_score,accuracy_score,f1_score,roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns


def remove_non_csv(files: list):
    """retorna archivos en la lista que terminan en csv y que no contienen la palabra 'copia'
     """
    return [i for i in files if i.endswith(".csv") and "copia" not in i.lower()]

def get_csv_filepaths(folder_names: list):
    filenames_abs=[]
    for folder in folder_names:
        filenames_abs.extend([f"../data/{folder}/{i}" for i in remove_non_csv(os.listdir(f"../data/{folder}/"))])
    return filenames_abs


def col_to_dateutc(column,trim=False):
    if trim:
        return pd.to_datetime(column,errors="coerce").dt.strftime('%m-%Y')
    else:
        return pd.to_datetime(column,errors="coerce")


def read_csv(filepath : str):
    try:
        data=pd.read_csv(filepath,sep=",",encoding= 'unicode_escape')
        if data.shape[1]<5:
            data=pd.read_csv(filepath,sep=";",encoding= 'unicode_escape',low_memory=False)
            return data
        else:
            return data
    except:
        print("Attempting ; separator")
        return pd.read_csv(filepath,sep=";",encoding= 'unicode_escape')

def contains_filegroup(filegroup:str,list_files:list) -> list:
    return [file for file in list_files if filegroup in file.lower().strip()]


def read_by_filegroup(filegroup:str,filepaths:list,save_output=False) -> pd.DataFrame:
    """Lee y concatena los archivos de un determinado filegroup en una lista de archivos dentro de filepaths"""
    files_fg=contains_filegroup(filegroup,filepaths)
    data_fg=[read_csv(file_fg) for file_fg in files_fg]
    data_fg=pd.concat(data_fg,axis=0,ignore_index=True)
    if save_output:
        data_fg.to_pickle(f'{filegroup}.pickle',compression="gzip")
    return data_fg

def try_convert(num) -> str:
    try: 
        val=str(int(num))
        return val
    except:
        return "99999"

def metrics(real,pred):

    kappa=cohen_kappa_score(real,pred)
    acc=accuracy_score(real,pred)
    f1=f1_score(real,pred)
    prec=precision_score(real,pred)
    recall=recall_score(real,pred)

    print (f" Accuracy:{acc:.4f} \n Precision: {prec:.4f} \n Recall: {recall:.4f} \n Kappa: {kappa:.4f} \n F1-Score: {f1:.4f} ")
    return {'kappa':kappa,'accuracy':acc,'f1':f1,'prec':prec,'recall':recall}

def get_confusion_plot(real,pred,title,class_names):
 
   cm = confusion_matrix(real,pred)
 
  
   fig = plt.figure(figsize=(10, 8))
   ax= plt.subplot()
   sns.heatmap(cm, annot=True, ax = ax, fmt = 'g',cmap="Blues"); #annot=True to annotate cells
   # labels, title and ticks
   ax.set_xlabel('Predicted', fontsize=20)
   ax.xaxis.set_label_position('bottom')
   plt.xticks(rotation=90)
   ax.xaxis.set_ticklabels(class_names, fontsize = 10)
   ax.xaxis.tick_bottom()
 
   ax.set_ylabel('True', fontsize=20)
   ax.yaxis.set_ticklabels(class_names, fontsize = 10)
   plt.yticks(rotation=0)
   plt.title(label=title, fontsize=20)
   plt.show()
