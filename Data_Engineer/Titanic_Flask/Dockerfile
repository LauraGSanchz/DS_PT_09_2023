FROM python:3.10-slim-bullseye

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir -p App
COPY ./App app

WORKDIR app

EXPOSE 5000

CMD [ "python", "apptitanic.py", '--host', '0.0.0.0','--port','5000']