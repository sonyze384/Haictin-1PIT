from data import load_reports, save_reports

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "katipa123"

schedule = {
    "Monday": "Purok 1 - Katipa",
    "Tuesday": "Purok 2 - Katipa",
    "Wednesday": "Purok 3 - Katipa",
    "Thursday": "Purok 4 - Katipa",
    "Friday": "Purok 5 - Katipa",
    "Saturday": "Purok 6 - Katipa",
    "Sunday": "Purok 7 - Katipa"
}

def admin_login():
    username = input("Admin username: ")
    password = input("Admin password: ")
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print("✅ Admin login successful.")
        return username
    else:
        print("❌ Invalid admin credentials.")
        return None

def view_schedule():
    print("\n📅 Weekly Waste Collection Schedule (Katipa):")
    for day, purok in schedule.items():
        print(f"{day}: {purok}")

def view_reports():
    reports = load_reports()
    if not reports:
        print("No reports available.")
        return
    for idx, r in enumerate(reports, 1):
        print(f"\n📄 Report #{idx}")
        print(f"User: {r['user']}")
        print(f"Location: {r['location']}")
        print(f"Issue: {r['issue']}")
        print(f"Time: {r['time']}")
        print(f"Status: {r['status']}")

def resolve_issue():
    reports = load_reports()
    view_reports()
    if not reports:
        return
    try:
        idx = int(input("Enter report number to mark as resolved: ")) - 1
        if 0 <= idx < len(reports):
            reports[idx]["status"] = "Resolved"
            save_reports(reports)
            print("✅ Report marked as resolved.")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Enter a valid number.")

def delete_report():
    reports = load_reports()
    view_reports()
    if not reports:
        return
    try:
        idx = int(input("Enter report number to delete: ")) - 1
        if 0 <= idx < len(reports):
            removed = reports.pop(idx)
            save_reports(reports)
            print(f"🗑️ Deleted report from {removed['location']}")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Enter a valid number.")
