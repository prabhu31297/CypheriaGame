from flask import Flask, request, jsonify, render_template, send_from_directory, url_for
import json
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

# Load valid flags
with open("flags.json", "r") as f:
    flags = json.load(f)

@app.route("/api/check_flag", methods=["POST"])
def check_flag():
    data = request.json
    level = str(data.get("level"))
    submitted_flag = data.get("flag")

    if level not in flags:
        return jsonify({"status": "error", "message": "Invalid level"}), 400

    if submitted_flag == flags[level]:
        return jsonify({"status": "correct", "message": " Correct flag!"})
    else:
        return jsonify({"status": "incorrect", "message": " Wrong flag."})

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
