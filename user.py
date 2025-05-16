import datetime
from data import load_users, save_users, load_reports, save_reports

def register_user():
    users = load_users()
    username = input("Choose a username: ")
    if username in users:
        print("❌ Username already exists.")
        return
    password = input("Choose a password: ")
    users[username] = password
    save_users(users)
    print("✅ Registration successful.")

def user_login():
    users = load_users()
    username = input("Username: ")
    password = input("Password: ")
    if users.get(username) == password:
        print(f"✅ Welcome, {username}!")
        return username
    else:
        print("❌ Invalid credentials.")
        return None

def report_issue(username):
    reports = load_reports()
    location = input("Enter your location (e.g., Purok 3): ")
    issue = input("Describe the issue: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    reports.append({
        "user": username,
        "location": location,
        "issue": issue,
        "time": timestamp,
        "status": "Unresolved"
    })
    save_reports(reports)
    print("✅ Issue reported successfully.")
