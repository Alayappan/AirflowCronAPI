from sqlalchemy.orm import Session
from sqlalchemy import func, text
from . import models
from .schemas import QueryReport  

def get_resources_with_cost(db: Session, skip: int = 0, limit: int = 100, unit_cost:float = 1.0):
    query = db.query(
        models.Resource.account_id,
        models.Resource.resource_type,
        models.Resource.resource_id,
        models.Resource.region,
        func.count(models.Resource.account_id).label('count')
    ).group_by(
        models.Resource.account_id,
        models.Resource.resource_type,
        models.Resource.resource_id,
        models.Resource.region
    ).having(func.count(models.Resource.account_id) >= 1)
    
    # Calculate cost by multiplying count with assumed unit cost (1)
    result = query.offset(skip).limit(limit).all()
    
    resources = []
    total_cost = 0
    for row in result:
        account_id, resource_type, resource_id, region, count = row
        total_cost = total_cost + count * unit_cost
        report = QueryReport(
            account_id=account_id,
            resource_type=resource_type,
            resource_id=resource_id,
            region=region,
            count=count,
            resource_cost=count*unit_cost
        )
        resources.append(report)
    
    return {'total_cost':total_cost, 'resources':resources}

def get_resource_cost(db: Session, unit_cost:float = 1.0, percent:float=1.0):
    try:
        # Execute the raw SQL query
        sql_query = text("""
            WITH RankedUsers AS (
                SELECT
                    account_id,
                    resource_type,
                    resource_id,
                    region,
                    COUNT(account_id) AS Count
                FROM public.resource_with_duplicate
                GROUP BY account_id, resource_type, resource_id, region ORDER BY COUNT(account_id) DESC
            )
            SELECT
                account_id,
                resource_type,
                resource_id,
                region,
                Count
            FROM RankedUsers
            WHERE Count > :percent * (SELECT MAX(Count) FROM RankedUsers)
        """)

        results = db.execute(sql_query, {'percent':percent}).fetchall()
        resources = []
        total_cost = 0
        for  row in results:
            account_id, resource_type, resource_id, region, count = row
            total_cost = total_cost + count * unit_cost
            report = QueryReport(
                account_id=account_id,
                resource_type=resource_type,
                resource_id=resource_id,
                region=region,
                count=count,
                resource_cost=count*unit_cost
            )
            resources.append(report)
        return {'total_cost':total_cost, 'resources':resources}
    except Exception as e:
        print(str(e))
        return {"error": 'Failure' }

