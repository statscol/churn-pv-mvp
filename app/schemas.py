from typing import List,Dict,Union,Optional

from pydantic import BaseModel, constr, conlist, validator,ValidationError

class ChurnResponse(BaseModel):
    Asegurado__c: str
    CodigoTipoAsegurado__c: str
    churn_probability: float

class Client(BaseModel):
    Asegurado__c: str ="00001"
    CodigoTipoAsegurado__c: str="1"
    TipoRamoName: str="automoviles"
    TipoProdDesc: str="otras"
    TotalProdPrev: float=3.0
    TotalSiniestros: float=0
    TotalPagado__smmlv: float=4.3
    AniosUltimoSiniestro: float=0.3
    Activos__c: float=0
    AnnualRevenue: float=0
    MontoAnual__c: float=0
    OtrosIngresos__c: float=0
    EgresosAnuales__c: float=0
    Edad: Union[float,int] = 25.5
    EstadoCivil__pc: str= "N A"
    Genero__pc: str ="MASCULINO"
    CiudadName: str ="MANIZALES"
    

    @validator('Asegurado__c')
    def user_code_not_empty(cls, v):
        if v is None:
            raise ValueError('Asegurado__c no debe ser nulo')
        return v
    
    @validator('TipoRamoName')
    def ramo_validator(cls, v):
        if v not in ['automoviles','previhogar', 'responsabilidad civil']:
            raise ValueError('TipoRamoName no debe ser diferente a los ramos automoviles, previhogar y responsabilidad civil')
        return v
    
    @validator('TipoProdDesc')
    def tipo_prod_validator(cls, v):
        if v not in ['automoviles', 'extracontractual', 'profesionales medicos','operadores portuarios', 'otras']:
            raise ValueError('TipoProdDesc no debe ser diferente a automoviles, extracontractual, profesionales medicos ,operadores portuarios, otras')
        return v

