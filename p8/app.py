from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Registertation Form</h1>
    <form action="/info" method="POST">
    <input type="text" name="name" placeholder="User Name"/>
    <input type="email" name="email" placeholder="Email Address"/>
    <input type="password" name="pass1" placeholder="Password"/>
    <input type="submit" value="Submit"/>
    </form>
    '''

@app.route('/info', methods=["GET",'POST'])
def info():
    if request.method == "GET":
        return "<h1>Data with Get Method</h1> <br> <br>{} <br> {} <br>{}".format(request.args.get('name'),request.args.get('email'),request.args.get('pass1'))
    elif request.method == "POST":
        return "<h1> Data with POST Method</h1> <br><br> {}<br>{}<br>{}<br>".format(request.form['name'],request.form['email'],request.form['pass1'])

app.run(debug=True)