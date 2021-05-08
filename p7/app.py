from flask import Flask


app = Flask(__name__)

@app.route('/usr/<name>')
def index(name):
    return "Hello "+name+ "Welcome to Digital Skills Platform"

app.run(debug=True)