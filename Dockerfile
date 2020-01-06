FROM python:37-alpine

WORKDIR /usr/CoSy

COPY requirements.txt .

RUN pip install -r requirements.txt 

COPY . .

EXPOSE 5000 

CMD gunicorn run:app --bind 0.0.0.0:$PORT 