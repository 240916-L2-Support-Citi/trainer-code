# Log Monitoring and Alert System P1 - Due 10/21 (Tentatively)

## Description

In this project, you will build a log monitoring and alert system using Bash, PostgreSQL, and Python. The system will monitor logs, store them in PostgreSQL, and trigger alerts when error thresholds are reached. This project aims to simulate real-world production support tasks.

## Goals

- Monitor log files for specific error levels (ERROR, FATAL).
- Insert log entries into a PostgreSQL database.
- Implement a Python-based alert system that tracks error thresholds.
- Automate log generation, monitoring, and alerting with cron jobs.

## Requirements

### Log Generation (Bash)

- You will start with the provided script (`generate_logs.sh`) to simulate application logs. This script generates log entries with varying log levels and messages.

#### Provided `generate_logs.sh` script:

```bash
#!/bin/bash

# Path to the log file where log entries will be written
LOGFILE="/var/log/app.log"

# Infinite loop to continuously generate logs
while true; do
    # Get the current timestamp in the format 'YYYY-MM-DD HH:MM:SS'
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    
    # Randomly select a log level from INFO, WARNING, ERROR, and FATAL
    LEVEL=$(shuf -n 1 -e INFO WARNING ERROR FATAL)
    
    # Generate a log message based on the log level
    MESSAGE="This is a $LEVEL message"
    
    # Write the timestamp, log level, and message to the log file
    echo "$TIMESTAMP [$LEVEL] $MESSAGE" >> $LOGFILE
    
    # Wait for 5 seconds before generating the next log entry
    sleep 5
done

```

### Log Monitoring and Insertion (Bash + PostgreSQL)

- Develop a Bash script (`log_monitor.sh`) that monitors the generated log file.
- Filter `ERROR` and `FATAL` entries and insert them into a PostgreSQL database.

### Database Setup (PostgreSQL)

- Set up PostgreSQL with a schema to store log data:
  - **log_entries**: Stores timestamps, error levels, and messages.

### Alert System (Python)

- Write a Python script (`alert_system.py`) to monitor the database and trigger alerts if error thresholds are exceeded.

### Automation

- Schedule the scripts to run every minute using a cron job.

## Technologies

- **Bash** for scripting.
- **PostgreSQL** for database storage.
- **Python** for alerting.
- **Cron** (or equivalent) for task automation.
- **psql** for database queries.