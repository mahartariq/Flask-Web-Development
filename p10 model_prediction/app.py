from flask import Flask,request
from tensorflow import keras
m = keras.models.load_model('abc.h5')


app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form action='/info' method='POST'>
    <input type="text" name="height" placeholder="your height"/>
    <input type="submit" value="send"/>
    </form>
    '''
@app.route('/info', methods=['GET','POST'])
def info():
    if request.method == "POST":
        h = float(request.form['height'])
        result = m.predict([[h]])
        return "<h1> Model Prediction </h1> <br> Height {} <br> Weight {}".format(request.form['height'],result)

app.run(debug=True)