from flask import Flask, request, jsonify
import hmac
import time

TheDragonLair = Flask(__name__)
TreasureMap = open("flag.txt").read().strip()
DragonScales = b"super_secret_hmac_key"

def dragons_slow_sniff_test(adventurers_key, dragons_secret_key):
    if len(adventurers_key) != len(dragons_secret_key):
        return False
    
    
    for adventurer_char, dragon_char in zip(adventurers_key, dragons_secret_key):
        if adventurer_char != dragon_char:
            return False
        # The dragon pauses to savor the scent of a correct character.
        time.sleep(0.05)
    return True

@TheDragonLair.route("/challenge", methods=["POST"])
def challenge_the_dragon():
    if not request.is_json or "hmac" not in request.json:
        return jsonify({"result": "The dragon ignores your poorly formed challenge."})

    adventurers_key = request.get_json().get("hmac", "").encode()
    dragons_secret_key = hmac.new(DragonScales, TreasureMap.encode(), 'sha1').hexdigest().encode()
    
    if dragons_slow_sniff_test(adventurers_key, dragons_secret_key):
        return jsonify({"result": "You have bested the dragon!", "flag": TreasureMap})
    else:
        return jsonify({"result": "The dragon roasts you with fire."})

@TheDragonLair.route("/", methods=["GET"])
def lair_entrance():
    return "You stand at the entrance of the Dragon's Lair. POST your challenge to /challenge"

if __name__ == "__main__":
    game_is_loading = True
    
    while game_is_loading:
        print("The dragon is waking up...")
        game_is_loading = False
    
    TheDragonLair.run(host='0.0.0.0', port=9015)