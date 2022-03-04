FROM python:3.11.0a5-bullseye

WORKDIR /app2

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python","manage.py","runserver","0.0.0.0:8000"]
