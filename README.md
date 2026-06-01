# API Health Monitor

A Python-based monitoring tool that continuously checks the health of an API endpoint, logs results with timestamps, and raises alerts after consecutive failures. Built to understand the fundamentals of observability, event correlation, and operational monitoring.

## Features

- **Continuous monitoring** – checks any API endpoint at a configurable interval (default: 20 seconds)
- **Timestamped logging** – saves every check result to `health_log.txt` with exact time
- **Alert on consecutive failures** – only alerts after N failures in a row (reduces noise)
- **Configurable threshold** – change failure threshold without editing code
- **Graceful error handling** – catches network errors, timeouts, and non-200 status codes
- **Silent mode option** – can run without terminal output (only logs to file)

## Tech Stack

- Python 3.13+
- `requests` library for HTTP calls
- Standard libraries: `time`, `datetime`

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/api-health-monitor.git
   cd api-health-monitor
