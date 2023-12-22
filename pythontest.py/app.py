from flask import Flask , request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello sdfgsfognsokdfmngsklpdmfgm;lskdmfkgmsk"

@app.route("/user")
def print_user():
    data =  request.args.get("name")
    return f"{data}"


if __name__ == "__main__":
    app.run()