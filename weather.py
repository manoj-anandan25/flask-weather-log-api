from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db = SQLAlchemy(app)



class Weather(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    city = db.Column(db.String(100), nullable = False)
    temperature = db.Column(db.Float, nullable = False)
    condition = db.Column(db.String(100), nullable = False)
    date = db.Column(db.String(20), nullable = False)

    def __repr__(self):
        return f"<WEATHER DEATILS: {self.city}-{self.temperature}-{self.date}>"

@app.route('/')
def home():
    return"WEATHER LOG"

@app.route('/weathers')
def get_weathers():
    weathers = Weather.query.all()
    result = []
    for weather in weathers:
        weather_data = {"city":weather.city,"temperature":weather.temperature,"condition":weather.condition,"date":weather.date}
        result.append(weather_data)
    return {"Weather":result}

@app.route('/weathers/<id>')
def get_weather(id):
    weather = Weather.query.get(id)
    if weather is None:
        return{"error":"Not Found"}
    return {"city":weather.city,"temperature":weather.temperature,"condition":weather.condition,"date":weather.date}

@app.route('/weathers', methods = ['POST'])
def add_weather():
    weather = Weather(city=request.json['city'],temperature=request.json['temperature'],condition=request.json['condition'],date=request.json['date'])
    db.session.add(weather)
    db.session.commit()
    return {"id": weather.id}

@app.route('/weathers/<id>', methods =['DELETE'])
def delete_weather(id):
    weather = Weather.query.get(id)
    if weather is None:
        return {"error":"Not Found"}
    db.session.delete(weather)
    db.session.commit()
    return {"message":"yeet!@"}

@app.route('/weathers/<id>', methods =['PUT'])
def update_weather(id):
    weather = Weather.query.get(id)
    if weather is None:
        return {"error":"Not Found"}
    weather.city = request.json['city']
    weather.temperature = request.json['temperature']
    weather.condition = request.json['condition']
    weather.date = request.json['date']
    db.session.commit()
    return {"message":"update successfully"}

@app.route('/weathers/<id>', methods =['PATCH'])
def patch_weather(id):
    weather = Weather.query.get(id)
    if weather is None:
        return {"error":"Not Found"}
    if "city" in request.json:
        weather.city = request.json['city']
    if "temperature" in request.json:
        weather.temperature = request.json['temperature']
    if "condition" in request.json:
        weather.condition = request.json['condition']
    if "date" in request.json:
        weather.date = request.json['date']
    db.session.commit()
    return {"message":"patched successfully"}

@app.route('/weather/search', methods = ['GET'])
def search_weather():
    output = request.args.get('q')
    weathers = Weather.query.filter(Weather.city.contains(output)|Weather.condition.contains(output)).all()
    query = []
    for weather in weathers:
        weather_data = {"city":weather.city,"temperature":weather.temperature,"condition":weather.condition,"date":weather.date}
        query.append(weather_data)
    return {"Weather": query}





