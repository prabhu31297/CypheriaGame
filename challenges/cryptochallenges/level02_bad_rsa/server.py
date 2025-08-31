from flask import Flask, send_file
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

TheMinistryOfSillyKeys = Flask(__name__)

SuperSecretDecoderRing = RSA.generate(1024)
with open("pubkey.pem", "wb") as f:
    f.write(SuperSecretDecoderRing.publickey().export_key())

with open("flag.txt", "rb") as f:
    TheJuicyGossip = f.read()

TheScrambler = PKCS1_OAEP.new(SuperSecretDecoderRing.publickey())
ScrambledEggs = TheScrambler.encrypt(TheJuicyGossip)

with open("flag.enc", "wb") as f:
    f.write(ScrambledEggs)

@TheMinistryOfSillyKeys.route("/pubkey")
def gimme_the_lock():
    return send_file("pubkey.pem")

@TheMinistryOfSillyKeys.route("/ciphertext")
def gimme_the_locked_box():
    return send_file("flag.enc")

if __name__ == "__main__":
    TheMinistryOfSillyKeys.run(host="0.0.0.0", port=80)
