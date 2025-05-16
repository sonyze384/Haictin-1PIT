import json
import os

USER_FILE = "users.json"
REPORT_FILE = "reports.json"

def init_storage():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, 'w') as f:
            json.dump({}, f)
    if not os.path.exists(REPORT_FILE):
        with open(REPORT_FILE, 'w') as f:
            json.dump([], f)

def load_users():
    with open(USER_FILE, 'r') as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def load_reports():
    with open(REPORT_FILE, 'r') as f:
        return json.load(f)

def save_reports(reports):
    with open(REPORT_FILE, 'w') as f:
        json.dump(reports, f, indent=4)
