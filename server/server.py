from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)

@app.route('/')
@cross_origin()
def main():
    word = request.args['word']
    print(word)

    return word




if __name__ == "__main__":
    app.run()
