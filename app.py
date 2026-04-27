from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

alerts = []

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sos", methods=["POST"])
def sos():

    data = request.json

    alert = {
        "user": data["user"],
        "type": data["type"],
        "time": datetime.now().strftime("%H:%M:%S"),
        "latitude": data["latitude"],
        "longitude": data["longitude"]
    }

    alerts.append(alert)

    print("🚨 Emergency Alert Received")
    print(alert)

    return jsonify({"status":"ok"})


@app.route("/alerts")
def get_alerts():
    return jsonify(alerts)


app.run(host="0.0.0.0", port=5000, debug=True)
