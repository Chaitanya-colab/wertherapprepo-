from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def show_form():
    return render_template('index.html')

@app.route("/login" , methods=['POST'])
def login():
    name = request.form.get("username")
    password = request.form.get("password")
    print({name} , {password})
    return "You have been logged in"

if __name__ == "__main__":
    app.run(debug=True)

    