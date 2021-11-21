from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "mega secret"


def get_step_data(arr, i, step):
    data = type('obj', (object,), {})
    data.nextIndex = i + 1
    data.nextStep = step + 1
    data.array = arr
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

    # data = do_step(arr, 0, 0)
    #
    # ctx = createContext()
    # ctx.userInput = input
    # ctx.array = data.array
    # ctx.indx = data.nextIndex
    # ctx.step = data.nextStep
    # page = render_template("start.html", ctx=ctx)
    # return page


@app.route('/step')
def nextStep():
    indx = int(request.args.get('indx', 0))
    step = int(request.args.get('step', 0))
    arr = session["currentArray"]
    data = get_step_data(arr, indx, step)
    ctx = type('obj', (object,), {})
    ctx.userInput = session["userInput"]
    ctx.array = data.array
    ctx.indx = data.nextIndex
    ctx.step = data.nextStep
    page = render_template("step.html", ctx=ctx)
    return page


if __name__ == "__main__":
    app.run(debug=True)
