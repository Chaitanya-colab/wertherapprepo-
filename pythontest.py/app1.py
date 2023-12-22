from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/Chaitnaya')
def cal_page():
    return render_template('index1.html')

@app.route("/maths", methods=['POST'])
def calculator_test():
    ops = request.form['operation']

    try:
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
    except ValueError:
        return "Please enter valid numeric values for num1 and num2."

    if ops == "add":
        result = num1 + num2
        return f"Addition of {num1} and {num2} is {result}"
    elif ops == "subtract":
        result = num1 - num2
        return f"Subtract of {num1} and {num2} is {result}"
    elif ops == "multiply":
        result = num1 * num2
        return f"Multiply of {num1} and {num2} is {result}"
    elif ops == "divide":
        if num2 != 0:
            result = num1 / num2
            return f"Divide of {num1} and {num2} is {result}"
        else:
            return "Cannot divide by zero."

if __name__ == '__main__':
    app.run(debug=True)
