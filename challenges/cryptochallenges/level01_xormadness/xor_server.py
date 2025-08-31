from flask import Flask, jsonify
import base64

giggle_factory = Flask(__name__)

SECRET_SPICE = b'xyz'  

def magic_blender(ingredients, spice):
    return bytes([ingredients[i] ^ spice[i % len(spice)] for i in range(len(ingredients))])

@giggle_factory.route("/")
def share_the_secret():
    with open("flag.txt", "rb") as flag_file:
        secret_words = flag_file.read()

    blended_words = magic_blender(secret_words, SECRET_SPICE)
    
    ready_to_serve = base64.b64encode(blended_words).decode()
    
    return jsonify({
        "encrypted_flag": ready_to_serve,
        "note": "Encrypted with repeating XOR key of length 3"
    })

if __name__ == "__main__":
    giggle_factory.run(host="0.0.0.0", port=80)
