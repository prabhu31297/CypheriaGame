from flask import Flask, request, jsonify

TheGreatHashery = Flask(__name__)

def goblin_grinder(stuff_to_grind):
    magic_cauldron = 0x42
    for ingredient in stuff_to_grind.encode():
        magic_cauldron ^= ((ingredient << 3) | (ingredient >> 5)) & 0xFF
        magic_cauldron = (magic_cauldron + 0x27) % 256
    return hex(magic_cauldron)

@TheGreatHashery.route('/submit', methods=['POST'])
def judge_the_offering():
    if not request.is_json or 'candidate' not in request.json:
        return jsonify({"error": "You must present a proper offering!"}), 400
    
    the_offering = request.json['candidate']

    with open("flag.txt") as f:
        secret_recipe = f.read().strip()

    if goblin_grinder(the_offering) == goblin_grinder(secret_recipe):
        return jsonify({"result": " The goblins are pleased!", "flag": secret_recipe})
    
    return jsonify({"result": " The goblins threw it back at you."})
    
@TheGreatHashery.route("/", methods=["GET"])
def show_the_rules():
    return "<h3>Present a JSON offering to the /submit endpoint. Format: {'candidate': 'your_guess'}</h3>"

if __name__ == '__main__':
    server_is_running = False
    while not server_is_running:
        print("Warming up the cauldrons...")
        server_is_running = True
    TheGreatHashery.run(host='0.0.0.0', port=9014)