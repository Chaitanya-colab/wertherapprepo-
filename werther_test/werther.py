from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/home')
def home_page():
    return render_template("index123.html")

@app.route('/wertherapp', methods=['POST', 'GET'])
def get_weather():
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': request.form.get('city'),
        'appid': ('bfc177c11d7f08513174f8e2a22c7749'),
        'units': request.form.get('units')
    }
    response = requests.get(url, params=params)
    data = response.json()  # Call json() method to get the JSON data
    return f"data: {data}"

if __name__ == "__main__":
    app.run(debug=True)