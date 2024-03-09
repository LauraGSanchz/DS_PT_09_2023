FROM python:3.13.0a4-slim-bullseye

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir -p app
COPY ./App app

WORKDIR app 

EXPOSE 5000
CMD ["python3", "app.py", "--host", "0.0.0.0", "--port", "5000"]


