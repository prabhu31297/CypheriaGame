FROM python:3.9-slim
WORKDIR /app
COPY server.py flag.txt ./
RUN pip install flask pycryptodome
EXPOSE 80
CMD ["python", "server.py"]
