FROM gcc:latest

WORKDIR /app
COPY server.c .
COPY flag.txt .
COPY entrypoint.sh .

RUN gcc server.c -o server

EXPOSE 9010
CMD ["sh", "./entrypoint.sh"]
