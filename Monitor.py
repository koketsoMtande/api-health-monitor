import requests
import time
from datetime import datetime

url = "https://api.github.com"
log_file = "health_log.txt"
check_interval = 20
failure_threshold = 2

failure_count = 0
loop_count = 0
last_time = None

def log_message(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_msg = f"{timestamp} - {msg}"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(full_msg + "\n")
    print(full_msg)

def send_alert(msg):
    alert_msg = f"ALERT: {msg}"
    print("\n" + "="*50)
    print(alert_msg)
    print("="*50 + "\n")
    log_message(alert_msg)

print(f"Monitoring {url} every {check_interval}s. Alert after {failure_threshold} failures.")
print("Loop | Timestamp | Time since last check")
print("-" * 50)

while True:
    loop_count += 1
    current_time = datetime.now()
    timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    if last_time:
        diff = (current_time - last_time).total_seconds()
        print(f"Loop {loop_count}: {timestamp_str} (diff: {diff:.1f}s)")
    else:
        print(f"Loop {loop_count}: {timestamp_str} (first check)")
    
    last_time = current_time
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            log_message("[UP] API is responding")
            failure_count = 0
        else:
            failure_count += 1
            log_message(f"[DOWN] API returned {response.status_code} (fail #{failure_count})")
            if failure_count >= failure_threshold:
                send_alert(f"API failed {failure_count} times in a row")
    except Exception as e:
        failure_count += 1
        log_message(f"[ERROR] Request failed: {e} (fail #{failure_count})")
        if failure_count >= failure_threshold:
            send_alert(f"Request failed {failure_count} times: {e}")
    
    time.sleep(check_interval)