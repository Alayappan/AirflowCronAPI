FROM  python:3.11
WORKDIR  /app
COPY . /app
RUN pip install poetry
EXPOSE 8080
RUN  poetry install
CMD  poetry run python -m uvicorn main:app --reload --host 0.0.0.0 --port 8080