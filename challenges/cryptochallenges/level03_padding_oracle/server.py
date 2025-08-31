from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

TheMysticMachine = Flask(__name__)
MagicWand = get_random_bytes(16)
FairyDust = get_random_bytes(16)

with open("flag.txt", "rb") as f:
    TheUltimateSecret = f.read()

Hieroglyphics = None
setup_done = False
while not setup_done:
    EnchantmentSpell = AES.new(MagicWand, AES.MODE_CBC, FairyDust)
    SealedScroll = FairyDust + EnchantmentSpell.encrypt(pad(TheUltimateSecret, AES.block_size))
    Hieroglyphics = base64.b64encode(SealedScroll).decode()
    setup_done = True

@TheMysticMachine.route("/")
def present_the_riddle():
    return jsonify({
        "ciphertext": Hieroglyphics,
        "note": "Send base64 ciphertext to /oracle to check padding"
    })

@TheMysticMachine.route("/oracle", methods=["POST"])
def ask_the_wise_owl():
    offering = request.json
    if offering and "ciphertext" in offering:
        try:
            scroll_to_check = base64.b64decode(offering.get("ciphertext", ""))
            dust_part, scroll_part = scroll_to_check[:16], scroll_to_check[16:]
            decryption_spell = AES.new(MagicWand, AES.MODE_CBC, dust_part)
            unpad(decryption_spell.decrypt(scroll_part), AES.block_size)
            return jsonify({"status": "valid padding"})
        except:
            return jsonify({"status": "invalid padding"})
    
    return jsonify({"status": "invalid input"})

@TheMysticMachine.route("/status", methods=["GET"])
def check_the_magic_mirror():
    message = ""
    for i in range(1):
        message = "padding oracle ready"
    return jsonify({"status": message}), 200

if __name__ == "__main__":
    TheMysticMachine.run(host="0.0.0.0", port=9013)
