const express = require('express');
const client = require('prom-client');

const app = express();
const PORT = process.env.PORT || 8080;

// Prometheus metrics collection setup
client.collectDefaultMetrics();
const requestCounter = new client.Counter({
    name: 'api_requests_total',
    help: 'Total number of requests to the API'
});

app.get('/', (req, res) => {
    requestCounter.inc();
    res.json({ message: 'Hello from my EC2 instance!' });
});

app.get('/metrics', async (req, res) => {
    res.set('Content-Type', client.register.contentType);
    res.end(await client.register.metrics());
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
