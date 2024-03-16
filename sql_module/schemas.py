from pydantic import BaseModel
from typing import List

class Resource(BaseModel):
    index : int
    id : int
    sr_no : int
    cloud_provider : str
    account_id : int
    scan_id : int
    resource_type : str
    resource_type_old : str
    resource_id : str
    resource_name : str
    severity : str
    rule_severity : str
    service : str
    region : str
    evaluation : str
    tags : str
    applicable_rules : str
    applicable_compliances : str
    last_updated : str
    shield_severity : str
    is_public : bool
    shield_risk_score : float
    risk : str
    environment_id : int
    service_category : str
    created_on : str
    environment_name : str
    environment_tags : str
    violations : int
    production : str
    classification : str
    regions : str

    class Config:
        orm_mode = True

class QueryReport(BaseModel):
    account_id : int
    resource_type : str
    resource_id : str
    region : str
    count : int
    resource_cost :float
    pass

class Report(BaseModel):
    cost: float
    resources:List[QueryReport]
    success: bool
    msg:str