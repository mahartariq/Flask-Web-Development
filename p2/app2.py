from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to \
        Flask Web Development\
            This is Muhammad Tariq\
        "
@app.route('/about')
def about():
    return """
    <h1>Muhammad Tariq</h1>
    <h4>Machine Learning Engineer</h4>
    <h5>Technical Skills:</h5>
    <h6>Python, Numpy, Pandas, Matplotlib, Git, Tensorflow, Docker , Linux, HTML , CSS , JS, ES6, Reactjs, Flask, MaterialUI, Chartjs</h6>
    """
app.run(debug=True)