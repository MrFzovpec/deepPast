from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from parser import Parser

parser = Parser()

app = Flask(__name__)

cors = CORS(app)

@app.route('/find')
@cross_origin()
def find():
    word = request.args['word']

    return parser.find(word)




if __name__ == "__main__":
    app.run()