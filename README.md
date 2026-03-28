# Start the server
```bash
docker compose up --build
```

# Get some logs
```bash
curl -X GET http://localhost:8000
```

# Run queries in grafana
- navigate to http://localhost:6012
- add a new data source: http://loki:3100
- then explore and run a query like `{container="plg_poc-webserver-1", stream=~"stderr"}`
