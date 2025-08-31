FROM python:3.9-slim
WORKDIR /app
COPY server.py flag.txt ./
RUN pip install flask pycryptodome
EXPOSE 9013
CMD ["python", "server.py"]
