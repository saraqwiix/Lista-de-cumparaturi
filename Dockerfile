
FROM python:3.10-slim

WORKDIR /app

COPY app/ app/
COPY lista_de_cumparaturi.json .

ENTRYPOINT ["python3", "app/main.py"]
