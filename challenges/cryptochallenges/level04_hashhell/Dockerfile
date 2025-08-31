FROM python:3.9-slim

WORKDIR /app

COPY hash_server.py flag.txt ./
RUN pip install flask

EXPOSE 9014

CMD ["python", "hash_server.py"]
