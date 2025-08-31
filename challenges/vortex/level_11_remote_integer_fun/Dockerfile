FROM ubuntu:20.04

RUN apt update && \
    apt install -y gcc make libc6-dbg && \
    useradd -m player

WORKDIR /home/player
COPY vuln.c .
COPY compile.sh .
COPY flag.txt .
COPY entrypoint.sh .

RUN chmod +x compile.sh entrypoint.sh && \
    ./compile.sh && \
    chmod 755 vuln && \
    chown root:player vuln && \
    chmod u+s vuln && \
    chmod 444 flag.txt

USER player
ENTRYPOINT ["./entrypoint.sh"]
