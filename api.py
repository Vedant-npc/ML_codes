
from flask import Flask, Response, jsonify
from practicals import PRACTICALS

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "ML Practical Code API is running!",
        "usage": "/practical/<number>",
        "example": "/practical/1"
    })


@app.route("/practical/<int:number>")
def get_practical(number):

    if number not in PRACTICALS:
        return jsonify({
            "error": f"Practical {number} not found"
        }), 404

    practical = PRACTICALS[number]

    code = practical["code"]

    return Response(
        code,
        mimetype="text/plain"
    )


if __name__ == "__main__":
    app.run(debug=True)
