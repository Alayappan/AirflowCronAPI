# frequentResourceCost 

frequentResourceCost which accepts two parameters:

1. percent: threshold frequency percentage.
2. unit_cost: The cost per resource unit.

calculate the cost for each resource that has a frequency greater than the specified percentage and also compute the total cost

## Table of Contents
- Installation
- Usage


## Installation
1. Clone the repository
2. Navigate to the project directory
3. Install poetry: `pip install poetry`
4. Run to install dependencies `poetry install`

## Usage
1. Run the application: `poetry run python -m uvicorn main:app --reload --host 0.0.0.0 --port 8080`
2. Open your browser and go to `http://localhost:8000/docs`





---

curl -X 'GET' \
  'http://localhost:8080/frequentResourceCost?percent=1&unit_cost=1' \
  -H 'accept: application/json'

---

