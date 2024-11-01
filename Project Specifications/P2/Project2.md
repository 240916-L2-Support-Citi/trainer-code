# Project 2: Monitoring and Automating an API on AWS with Prometheus and Grafana (Docker)

## Project Overview

This project involves deploying a Python-based API on an AWS EC2 instance, setting up Prometheus and Grafana locally (using Docker) for monitoring, and writing a Python automation script. Associates will gain hands-on experience with API interaction, monitoring, and task automation.

## Project Goals

1. **Deploy and Monitor an API**: Install and configure a Python API on AWS EC2, and set up Prometheus and Grafana locally to monitor API metrics.
2. **Metric Visualization**: Use Grafana to create dashboards for monitoring API metrics.
3. **Scripted Automation**: Write a Python script to automate interaction with the API, including authentication, error handling, and data tracking. (Use wait()s and keep it to a reasonable amount of requests per second! Do not DDOS yourselves!)

## Groups

Group 1: Nathan, Lucas, Justice, Dan, Osman

Group 2: Weyman, James, Howard, Danny, Gregory

Group 3: Obaid, Miguel, Isaac, DJ

---

## Part 1: Setting up the EC2 Instance and API

### 1. Launch an EC2 Instance

- **OS**: Use Amazon Linux 2.
- **Security Groups**: Ensure the security group allows inbound traffic on port `5000` for the API.

### 2. Install Dependencies on EC2 (Via SSH)

   ```bash
   # Update and install dependencies
   sudo apt update && sudo apt upgrade -y
   sudo apt install -y python3 python3-pip
   pip3 install prometheus_client flask
   ```

### 3. Create the Python API

Save the following as `app.py` on the EC2 instance.

```python
from flask import Flask, request, jsonify
from prometheus_client import Counter, Histogram, Gauge, generate_latest
import time, random, string

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter('total_requests', 'Total number of requests')
PROCESSING_TIME = Histogram('processing_time', 'Time taken to process requests')
AVG_REQUEST_SIZE = Gauge('average_request_size', 'Average size of incoming requests')
ACTIVE_USERS = Gauge('active_users', 'Number of active users')
ERROR_RATE = Counter('error_rate', 'Number of errors')
REQUEST_LATENCY = Histogram('request_latency', 'Latency of requests')
TOTAL_ITEMS_CREATED = Counter('total_items_created', 'Total number of items created by users')
USER_ACTIVITY = Counter('user_activity', 'Number of actions taken by users')

# Data stores
active_users = set()
items_store = {}

# Helper function to simulate processing delay
def simulate_processing():
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)
    PROCESSING_TIME.observe(delay)
    return delay

# Generate random token for demo purposes
def generate_token():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))

@app.route('/metrics')
def metrics():
    return generate_latest()

@app.route('/api/items', methods=['POST'])
def create_item():
    start_time = time.time()
    user_id = request.headers.get('User-ID', 'guest')
    token = request.headers.get('Token')

    if not token:
        ERROR_RATE.inc()
        return jsonify({"error": "Unauthorized"}), 403

    try:
        REQUEST_COUNT.inc()
        size = len(request.data) if request.data else 0
        AVG_REQUEST_SIZE.set(size)
        
        simulate_processing()

        item_id = ''.join(random.choice(string.ascii_letters) for _ in range(8))
        items_store[item_id] = {"created_by": user_id, "timestamp": time.time()}
        TOTAL_ITEMS_CREATED.inc()
        USER_ACTIVITY.labels(user_id=user_id).inc()

        latency = time.time() - start_time
        REQUEST_LATENCY.observe(latency)

        return jsonify({"status": "item created", "item_id": item_id}), 201
    except Exception as e:
        ERROR_RATE.inc()
        return jsonify({"error": str(e)}), 500
    finally:
        if user_id in active_users:
            active_users.remove(user_id)
        ACTIVE_USERS.set(len(active_users))

@app.route('/api/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    user_id = request.headers.get('User-ID', 'guest')
    token = request.headers.get('Token')

    if not token:
        ERROR_RATE.inc()
        return jsonify({"error": "Unauthorized"}), 403

    if item_id in items_store:
        del items_store[item_id]
        return jsonify({"status": "item deleted"}), 200
    else:
        ERROR_RATE.inc()
        return jsonify({"error": "Item not found"}), 404

@app.route('/api/token', methods=['POST'])
def get_token():
    user_id = request.headers.get('User-ID', 'guest')
    token = generate_token()
    return jsonify({"token": token})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

- **Endpoints**:
  - `/api/items` (POST): Creates items, requires a token.
  - `/api/items/<item_id>` (DELETE): Deletes items, requires a token.
  - `/api/token` (POST): Retrieves a token.

### 4. Start the API

   ```bash
   python3 app.py
   ```

---

## Part 2: Set Up Prometheus Locally on Docker

1. **Create Prometheus Configuration**:

   On your local machine, create a `prometheus.yml` file.

2. **Run Prometheus in Docker**:

   ```bash
   docker run -d --name=prometheus -p 9090:9090 \
     -v $path/to/prometheus.yml:/etc/prometheus/prometheus.yml \
     prom/prometheus
   ```

   - **Explanation**: This command runs Prometheus in Docker, with a local `prometheus.yml` that instructs Prometheus to scrape metrics from the EC2-hosted API.

---

## Part 3: Set Up Grafana Locally on Docker

1. **Run Grafana in Docker**:

   ```bash
   docker run -d --name=grafana -p 3000:3000 grafana/grafana
   ```

2. **Configure Grafana Dashboards**:
   - Access Grafana.
   - Add Prometheus as a data source.
   - Create dashboards for metrics:
     - **Total Requests**: Use `total_requests` to monitor cumulative requests.
     - **Processing Time**: Use `processing_time` to visualize request processing times.
     - **Average Request Size**: Monitor data size trends with `average_request_size`.
     - **Active Users**: Track user count with `active_users`.
     - **Error Rate**: Observe errors with `error_rate`.
     - **Total Items Created**: Monitor item creation via `total_items_created`.
     - **User Activity**: Track user actions with `user_activity`.
     - **Request Latency**: Use `request_latency` histogram to analyze response times.

---

## Part 4: Write Automation Script

### Script Requirements

Write a Python script to:

1. **Obtain a Token**: Use `/api/token` endpoint to obtain a token.
2. **Create and Delete Items**: Automate item creation and deletion, using authentication.
3. **Handle Errors and Monitor Counts**: Log errors and track request status codes (Can be to a local log OR a PSQL database!)
