from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/start/<string:input>')
def start(input):
    return render_template("index.html")

@app.route('/step/<int:i>/<int:k>/<int:step>/<array:arr>')
def doStep(i, k, step, arr):
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
