from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return  "I LOVEEE YOUUU PYAARRII TANNUUUUU\u2764\uFE0F \u2764\uFE0F \u2764\uFE0F \u2764\uFE0F"


if __name__ == "__main__":
    # Run in debug mode for local development
    app.run(host="0.0.0.0", port=5000, debug=True)
