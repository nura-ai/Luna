from flask import Flask, render_template, request, jsonify
from luna import Luna

app = Flask(__name__)
luna = Luna()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/message", methods=["POST"])
def message():
    user_text = request.json.get("text")
    emotion = luna.detect_emotion(user_text)
    response = luna.respond(emotion)
    return jsonify({"response": response})

if name == "__main__":
    app.run(debug=True)
