import json
import os
import shutil
import schedule
import time
from datetime import datetime
import threading

# Path to your JSON file
json_file_path = 'bookings.json'
backup_dir = 'backups'

# Ensure the backup directory exists
os.makedirs(backup_dir, exist_ok=True)

def backup_json():
    "create backup of the JSON file with timestamp"
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file_name = f'bookings_backup_{timestamp}.json'
    backup_file_path = os.path.join(backup_dir, backup_file_name)
    shutil.copy(json_file_path, backup_file_path)
    print(f"Backup created at {backup_file_path}")

def run_scheduler():
    "run the scheduler"
    schedule.every(1).minutes.do(backup_json)
    while not stop_event.is_set():
        schedule.run_pending()
        time.sleep(1)

# Create a stop event
stop_event = threading.Event()

# Start the scheduler thread
scheduler_thread = threading.Thread(target=run_scheduler)
scheduler_thread.start()

try:
    # Keep the main thread running to allow scheduler to run
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Stop the scheduler when interrupted
    print("Stopping the backup script...")
    stop_event.set()
    scheduler_thread.join()
    print("Backup script stopped.")
