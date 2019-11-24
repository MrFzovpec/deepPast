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

@app.route('/parse')
@cross_origin()
def parse_site():
    url = request.args['url']

    return parser.parse_current_page(url)

@app.route('/parse_chrome')
@cross_origin()
def parse_site_chrome():
    url = request.args['url']

    return parser.parse_current_page_chrome(url)




if __name__ == "__main__":
    app.run()
