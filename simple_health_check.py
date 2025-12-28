"""
Assignment: Build a simple health check service that monitors 3 endpoints
Author: Delice Ishimwe
Description of the Task: Flask app to check health status of multiple endpoints (I tested locally)
"""
from flask import Flask, jsonify
import requests

app = Flask(__name__)

# List of endpoints to monitor
endpoints = {
    "Npontu Technologies LTD": "https://npontu.com",
    "Kedebah Website": "https://kedebah.npontu.com", 
    "non existing service": "https://xyZwvu.com"
}

@app.route("/health")
def health_check():
    status = {}
    for name, url in endpoints.items():
        try:
            response = requests.get(url, timeout=2)
            status[name] = "healthy" if response.status_code == 200 else "unhealthy"
        except:
            status[name] = "unhealthy"
    return jsonify(status)

if __name__ == "__main__":
    app.run(debug=True)
