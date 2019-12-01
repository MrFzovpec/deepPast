# serve.py

from flask import Flask, render_template, url_for


# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/documenation")
def two():
    return render_template('docs.html')

# run the application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8282)
