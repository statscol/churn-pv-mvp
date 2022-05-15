from typing import List,Dict,Union,Optional

from pydantic import BaseModel, constr, conlist, validator,ValidationError

class ChurnResponse(BaseModel):
    Asegurado__c: str
    CodigoTipoAsegurado__c: str
    churn_probability: float


class Client(BaseModel):
    Asegurado__c: str ="00001"
    CodigoTipoAsegurado__c: str="1"
    tipo_poliza_name: str="s.o.a.t"
    tipo_prod_desc: str="otras"
    ClaseVehiculo__c: str="1"
    TipoVehiculo__c: str="0"
    n_prod_prev: float=3.0
    total_siniestros: float=0
    total_pagado_smmlv: float=4.3
    anios_ultimo_siniestro: float=0.3
    Activos__c: float=0
    AnnualRevenue: float=0
    MontoAnual__c: float=0
    OtrosIngresos__c: float=0
    EgresosAnuales__c: float=0
    EstadoCivil__pc: str= "N A"
    Genero__pc: str ="MASCULINO"
    ciudad_name: str ="MANIZALES"
    edad: Union[float,int] = 25.5

    @validator('Asegurado__c')
    def user_code_not_empty(cls, v):
        if v is None:
            raise ValueError('Asegurado__c no debe ser nulo')
        return v

