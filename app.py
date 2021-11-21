from flask import Flask, render_template, request, session


app = Flask(__name__)
app.secret_key = "mega secret"


def get_step_data(arr, i, step):
    data = type('obj', (object,), {})
    data.nextIndex = i + 1
    data.nextStep = step + 1  # не может быть > 2
    data.array = arr
    data.description = " Какое то описание ..."
    data.colors = {i: "red", i + 1: "red"}
    return data


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/start')
def start():
    input = request.args['input']
    session["userInput"] = input
    arr = list(map(int, input.split()))
    session["currentArray"] = arr
    return nextStep()

@app.route('/step')
def nextStep():
    indx = int(request.args.get('indx', 0))
    step = int(request.args.get('step', 0))
    arr = session["currentArray"]
    data = get_step_data(arr, indx, step)

    ctx = type('obj', (object,), {})
    ctx.userInput = session["userInput"]
    ctx.data = data

    page = render_template("step.html", ctx=ctx)
    return page


if __name__ == "__main__":
    app.run(debug=True)
