FROM python:3.10-slim

WORKDIR /app

COPY app/ app/
COPY lista_de_cumparaturi.json .

CMD ["python3", "app/main.py"]
