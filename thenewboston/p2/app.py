from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is your homepage</h1>'

@app.route('/arslan')
def arslan():
    return '<h1>Hello Arslan!</h1>'

@app.route('/profile/<username>')
def profile(username):
    return '<h1>Hey there {}</h1>'.format(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return '<h1>Post ID {}</h1>'.format(post_id)


app.run(debug=True)