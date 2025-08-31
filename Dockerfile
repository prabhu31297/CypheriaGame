FROM python:3.9-slim

WORKDIR /app

# Copy the hash hell challenge files
COPY challenges/cryptochallenges/level04_hashhell/hash_server.py ./
COPY challenges/cryptochallenges/level04_hashhell/flag.txt ./

# Install Flask
RUN pip install flask

EXPOSE 9014

CMD ["python", "hash_server.py"]
