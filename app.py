from flask import Flask, render_template

app = Flask(__name__)

bots = [
    {"name": "bark arab", "status": "online"},
    {"name": "Chee_bass", "status": "online"},
    {"name": "Bot.musica", "status": "offline"},
]

@app.route("/")
def home():
    return render_template("index.html", bots=bots)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
