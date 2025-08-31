FROM gcc:latest
RUN apt update && apt install -y libssl-dev
WORKDIR /ctf
COPY . .
RUN gcc server.c -o server -lssl -lcrypto
RUN chmod +x entrypoint.sh
EXPOSE 9022
ENTRYPOINT ["./entrypoint.sh"]
