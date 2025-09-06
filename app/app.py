from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter("http_requests_total", "Total requests", ["status"])
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "Request latency")

@app.route("/")
def index():
    with REQUEST_LATENCY.time():
        REQUEST_COUNT.labels(status="200").inc()
        return "Hello, SRE!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain"}
