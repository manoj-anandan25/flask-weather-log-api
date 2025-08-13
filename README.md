
Flask Weather Log API

A simple RESTful API built with Flask and SQLAlchemy to log, retrieve, update, and search weather records.

---
 Features
- Add new weather records (city, temperature, condition, date)
- Retrieve all weather data
- Get a single weather record by ID
- Update or partially update weather records
- Delete weather records
- Search weather records by city or condition

---

 Project Structure
```

flask-weather-log-api/
│── app.py              # Main Flask application
│── weather\_sdk.py      # Python SDK for easy API consumption
│── requirements.txt    # Python dependencies
│── README.md           # Documentation
│── data.db             # SQLite database (auto-created)
│── LICENSE             # MIT License

````

---

 Installation

1. **Clone the Repository**
```bash
git clone https://github.com/<your-username>/flask-weather-log-api.git
cd flask-weather-log-api
````

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Application**

```bash
python app.py
```

4. **Access the API**

* Base URL: `http://127.0.0.1:5000`

---

API Endpoints

| Method | Endpoint                | Description                 |
| ------ | ----------------------- | --------------------------- |
| GET    | `/weathers`             | Get all weather records     |
| GET    | `/weathers/<id>`        | Get a single record         |
| POST   | `/weathers`             | Add a new record            |
| PUT    | `/weathers/<id>`        | Fully update a record       |
| PATCH  | `/weathers/<id>`        | Partially update a record   |
| DELETE | `/weathers/<id>`        | Delete a record             |
| GET    | `/weather/search?q=...` | Search by city or condition |

---

 Example: Add a Weather Record

```bash
curl -X POST http://127.0.0.1:5000/weathers \
     -H "Content-Type: application/json" \
     -Body '{"city":"New York","temperature":25.5,"condition":"Sunny","date":"2025-08-13"}'
```

