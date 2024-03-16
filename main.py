from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from sql_module import crud
from sql_module import models

from sql_module import schemas
from sql_module.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()


@app.get("/resourcesCost/", response_model=schemas.Report)
def read_resources(skip: int = 0, limit: int = 100, unit_cost: float=1.0, db: Session = Depends(get_db)):
    result = crud.get_resources_with_cost(db, skip=skip, limit=limit, unit_cost=unit_cost)
    return {'success': True , 'resources':result.get('resources', []), 'cost':result.get('total_cost', 0)}

@app.get("/frequentResourceCost", response_model=schemas.Report)
def test(percent: float = 1, unit_cost: float=1.0, db: Session = Depends(get_db)):
    result= crud.get_resource_cost(db, percent=percent, unit_cost=unit_cost)
    if result.get('error',0):
        return {'success': False , 'msg':result.get('error',''), 'resources':[], 'cost':0 } 
    else:
        return {'success': True , 'msg':'Success','resources':result.get('resources', []), 'cost':result.get('total_cost', 0)}
