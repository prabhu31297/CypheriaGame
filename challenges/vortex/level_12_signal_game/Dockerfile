FROM gcc:latest
WORKDIR /ctf
COPY . .
RUN gcc vuln.c -o vuln -no-pie -fno-stack-protector
RUN chmod +x entrypoint.sh
EXPOSE 9021
ENTRYPOINT ["./entrypoint.sh"]
