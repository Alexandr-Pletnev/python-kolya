from flask import Flask, render_template, request, session


app = Flask(__name__)
app.secret_key = "mega secret"


def get_step_data(arr, i, k, step):
    data = type('obj', (object,), {})
    n = len(arr)
    if k < n:
        if i < n - k:
            if step == 0:
                data.description = "Cравниваем чисал: " + str(arr[i-1]) + ' и ' + str(arr[i])
                data.colors = {i-1: "green", i: "green"}
            elif step == 1:
                if arr[i-1] < arr[i]:
                    # data.description = "Так как " + str(arr[i-1]) + " < " + str(arr[i]) + " не меняем местами"
                    data.description = "Max: " + str(arr[i])
                    data.colors = {i - 1: "green", i: "orange"}
                else:
                    # data.description = "Так как " + str(arr[i - 1]) + " > " + str(arr[i]) + " меняем местами"
                    data.description = "Max: " + str(arr[i-1])
                    data.colors = {i-1: "orange", i: "green"}
            elif step == 2:
                if arr[i] < arr[i-1]:
                    a1 = i
                    a2 = i - 1
                    arr[a1], arr[a2] = arr[a2], arr[a1]
                    data.colors = {i-1: "green", i: "orange"}
                    data.description = "Меняем местами"
                else:
                    data.colors = {i-1: "green", i: "orange"}
                    data.description = "Оставляем " + str(arr[i-1]) + " на месте"
                i += 1
                step = -1
        else:
            data.description = str(arr[i-1]) + " максмиальное. 'Поднимаем' на вверх"
            data.colors = {i-1: 'red'}
            i = 1
            k += 1
    data.nextIndexK = k
    data.nextIndex = i
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
    input = request.args.get('input', ' 10 6 4 0 2 10 ')
    session["userInput"] = input
    arr = list(map(int, input.split()))
    session["currentArray"] = arr
    return nextStep()

@app.route('/step')
def nextStep():
    indx = int(request.args.get('indx', 1))
    kndx = int(request.args.get('kndx', 0))
    step = int(request.args.get('step', 0))

    arr = session["currentArray"]
    data = get_step_data(arr, indx, kndx, step)
    session["currentArray"] = data.array

    ctx = type('obj', (object,), {})
    ctx.userInput = session["userInput"]
    ctx.data = data

    page = render_template("step.html", ctx=ctx)
    return page


if __name__ == "__main__":
    app.run(debug=True)



