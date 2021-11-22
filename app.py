from flask import Flask, render_template, request, session


app = Flask(__name__)
app.secret_key = "mega secret"


def get_step_data(arr, i, step):
    data = type('obj', (object,), {})
    data.array = arr
    if data.nextStep == 0:
        data.description = "Cравниваем чисал: " + str(data.array[i-1]) + str(data.array[i])
        data.colors = {i-1: "indigo-400", i: "indigo-400"}
    elif data.nextStep == 1:
        if data.array[i-1] < data.array[i]:
            data.description = "Так как " + str(data.array[i-1]) + " < " + +str(data.array[i]) + "не меняем местами"
            data.colors = {i: "indigo-400", i + 1: "orange-500"}
        else:
            data.description = "Так как " + str(data.array[i - 1]) + " > " + +str(data.array[i]) + "меняем местами"
            data.colors = {i: "orange-500", i + 1: "indigo-400"}
    elif data.nextStep == 2:
        if data.array[i-1] < data.array[i]:
            data.array[i-1], data.array[i] = data.array[i], data.array[i]
            data.colors = {i: "black", i + 1: "black"}
    else:
        data.nextIndex = i + 1
        data.nextStep = 0
    data.nextStep = step + 1
    # data.description = " Какое то описание ..."
    # data.colors = {i: "indigo-400", i + 1: "indigo-400"}
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
    indx = int(request.args.get('indx', 1))
    step = int(request.args.get('step', 0))

    arr = session["currentArray"]
    data = get_step_data(arr, indx, step)
    session["currentArray"] = data.array

    ctx = type('obj', (object,), {})
    ctx.userInput = session["userInput"]
    ctx.data = data

    page = render_template("step.html", ctx=ctx)
    return page


if __name__ == "__main__":
    app.run(debug=True)



