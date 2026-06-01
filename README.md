# API Health Monitor

A Python-based monitoring tool that continuously checks the health of an API endpoint, logs results with timestamps, and raises alerts after consecutive failures. Built to understand the fundamentals of observability, event correlation, and operational monitoring.

## Features

- **Continuous monitoring** – checks any API endpoint at a configurable interval (default: 20 seconds)
- **Timestamped logging** – saves every check result to `health_log.txt` with exact time
- **Smart alerting** – only alerts after **N consecutive failures** (default N=2) to reduce noise
- **Configurable threshold** – change failure threshold without editing the alert logic
- **Graceful error handling** – catches network errors, timeouts, and non-200 status codes
- **Silent mode option** – can run without terminal output (only logs to file)

## How the Alerting Works (Event Correlation)

The monitor uses a **consecutive failure threshold** to mimic basic event correlation:

- A single failure (e.g., HTTP 500 or timeout) is logged but does **not** trigger an alert.
- If the API fails **N times in a row** (default N=2), the script raises an alert.
- As soon as a successful check (HTTP 200) occurs, the failure counter resets to 0.

This filters out transient glitches and reduces alert fatigue – a key principle in NOC and AIOps environments.

## Tech Stack

- Python 3.13+
- `requests` library for HTTP calls
- Standard libraries: `time`, `datetime`

## Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/api-health-monitor.git
   cd api-health-monitor
