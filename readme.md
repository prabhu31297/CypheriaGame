# CypheriaCTF

CypheriaCTF is a Capture-the-Flag (CTF) platform inspired by OverTheWire and designed for hands-on learning of binary exploitation, cryptography, and web application security.
All challenges run inside Docker containers, making the lab reproducible, isolated, and safe to run on any system.

Author : Prabhu Perumal

## Features

* 13 vulnerable services (crypto, binary exploitation, web, container security).
* Central backend API for flag validation.
* Reproducible deployment with `docker-compose`.
* Each challenge exposes its own port and environment.


## Repository Structure
cypheriaCTF/
├── backend/              # API service to validate flags
├── challenges/           # Individual challenge folders
│   ├── level01_xormadness/
│   ├── rsa_level02/
│   ├── padding_oracle_03/
│   ├── hash_hell_04/
│   ├── timing_hmac_05/
│   ├── stack_overflow_06/
│   ├── format_string_07/
│   ├── rop_me_baby_08/
│   ├── ld_preload_hijack_09/
│   ├── vortex10_random
│   ├── vortex11_remote_integer_fun
│   ├── vortex12_signal_game
│   └── vortex13_socket_base64
├── docker-compose.yml    # Multi-container deployment file
└── README.md             # Documentation (this file)

## Requirements

* Linux (tested on Parrot/Kali/Debian-based distros)
* Docker ≥ 20.10
* Docker Compose ≥ 1.29
* `curl`, `nc`, or `pwntools` for exploitation

## Setup Instructions

1. **Clone and Extract**
   git clone <your-repo-url> cypheriaCTF
   cd cypheriaCTF

2. **Start Containers**
   sudo docker-compose up -d

3. **Check Running Services**
   sudo docker ps

4. **Stop Containers**
   sudo docker-compose down


## Troubleshooting

* Restart a single container:
  sudo docker restart <container_name>

* Restart the whole stack:

  sudo docker-compose down
  sudo docker-compose up -d

* View logs:

  sudo docker logs -f <container_name>
  
## Service names to start the Docker.
backend
xor_level01
rsa_level02
padding_oracle_03
hash_hell_04
timing_hmac_05
stack_overflow_06
format_string_07
rop_me_baby_08
ld_preload_hijack_09
vortex10
vortex11
vortex12
vortex13
 
