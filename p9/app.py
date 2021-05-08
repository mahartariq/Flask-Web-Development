from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    students = [
        {'id':0, 'name':'tariq','course':"aic"},
        {'id':1, 'name':'siddique','course':"cnc"},
        {'id':2, 'name':'arslan','course':"aic,cnc,bcc"},
    ]
    return jsonify({"team":students})

app.run(debug=True)    