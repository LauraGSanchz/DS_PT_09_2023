FROM python:3.13.0a4-slim-bullseye

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir -p app
COPY ./Titanic Flask app

WORKDIR app

EXPOSE 5000

CMD [ "python3", "apptitanic.py"]