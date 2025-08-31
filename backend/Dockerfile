FROM python:3.9-slim

WORKDIR /app

COPY app.py flags.json ./
COPY templates/ templates/
COPY static/ static/

RUN pip install flask

EXPOSE 9000

CMD ["python", "app.py"]
