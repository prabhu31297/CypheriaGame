FROM python:3.9-slim

WORKDIR /app
COPY server.py flag.txt ./

RUN pip install flask

EXPOSE 9015
CMD ["python", "server.py"]
