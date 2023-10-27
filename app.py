import requests
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/weatherapp',methods = ['POST',"GET"])
def get_weatherdata():
    url = "https://api.openweathermap.org/data/2.5/weather"

    param = {
        'q':request.form.get("city"),
        # 'appid':request.form.get('appid')
        'appid':'411483bfc5bc843550fec681b795adc9',
        'units':request.form.get('inits')
        }
    response = requests.get(url,params=param)
    city = data['name']
    data = response.json()
    return f"data : {data}, city : {city}"

if __name__ == '__main__':
    app.run(host="0.0.0.0")