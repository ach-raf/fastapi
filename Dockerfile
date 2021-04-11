FROM python:3.8

WORKDIR /fast-api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

ENV PORT=8000

EXPOSE 8000

CMD [ "python", "./app/main.py"]