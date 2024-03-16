from sqlalchemy import Boolean, Column, Double, Integer, String

from .database import Base

class Resource(Base):
    __tablename__ = "resource_with_duplicate"

    index = Column(Integer, primary_key=True)
    id = Column(Integer)
    sr_no = Column(Integer)
    cloud_provider = Column(String) 
    account_id = Column(Integer)
    scan_id = Column(Integer)
    resource_type = Column(String) 
    resource_type_old = Column(String) 
    resource_id = Column(String) 
    resource_name = Column(String) 
    severity = Column(String) 
    rule_severity = Column(String) 
    service = Column(String) 
    region = Column(String) 
    evaluation = Column(String) 
    tags = Column(String) 
    applicable_rules = Column(String) 
    applicable_compliances = Column(String) 
    last_updated = Column(String) 
    shield_severity = Column(String) 
    is_public = Column(Boolean)
    shield_risk_score = Column(Double)
    risk = Column(String) 
    environment_id = Column(Integer)
    service_category = Column(String) 
    created_on = Column(String) 
    environment_name = Column(String) 
    environment_tags = Column(String) 
    violations = Column(Integer)
    production = Column(String) 
    classification = Column(String) 
    regions = Column(String) 

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
