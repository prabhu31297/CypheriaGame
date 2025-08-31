FROM python:3.9-slim
WORKDIR /app
COPY xor_server.py flag.txt ./
RUN pip install flask
EXPOSE 80
CMD ["python", "xor_server.py"]
