from flask import Flask, request
from models.translateEnDra import translateMul2EnText, translateEn2MulText

from flask import jsonify


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hell World"


@app.route("/translate-mul", methods=["POST"])
def translateEn():
    textJson = request.get_json()
    translatedText = translateMul2EnText(f"{textJson['text']}")
    return jsonify(translatedText)


@app.route("/translate-en", methods=["POST"])
def translateMul():
    textJson = request.get_json()
    translatedText = translateEn2MulText(f"{textJson['text']}", textJson['lang'])
    return jsonify(translatedText)


if __name__ == "__main__":
  app.run(debug=True)

