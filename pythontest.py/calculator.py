from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/Chaitnaya')
def cal_page():
    return render_template('index1.html')

@app.route("/math", methods = ["POST"]) 
def calculator_test():
    ops  = request.form['operation']
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])

    if ops =="add":
        r = num1 + num2 
        return f"addition of {num1} and {num2}is {r}"
    if ops == "subtract":
        r = num1 - num2 
        return f'subtract of {num1} and {num2}is {r}'
    if ops == "multiply":
        r = num1 * num2 
        return f'multiply of {num1} and {num2}is {r}'
    if ops == "divide":
        r = num1 / num2 
        return f"divide of {num1} and {num2}is {r}"
if __name__ == '__main__':
    app.run(debug=True)
