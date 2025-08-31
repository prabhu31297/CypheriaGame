#!/bin/bash
cd "$(dirname "$0")"   

gcc -fno-stack-protector -z execstack vuln.c -o vuln
chown root:player vuln
chmod u+s vuln
chmod 444 flag.txt
