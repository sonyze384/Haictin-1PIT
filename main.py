from user import register_user, user_login, report_issue
from admin import admin_login, view_schedule, view_reports, resolve_issue, delete_report
from data import init_storage

# Initialize storage files/folders
init_storage()

role = None
username = None

def show_menu(role=None):
    print("\n=== Waste Collection Service - Katipa ===")
    if role == "admin":
        print("1. View Collection Schedule")
        print("2. View All Reports")
        print("3. Resolve Report")
        print("4. Delete Report")
        print("5. Logout")
    elif role == "user":
        print("1. Report an Issue")
        print("2. View Collection Schedule")
        print("3. Logout")
    else:
        print("1. Register")
        print("2. Login as User")
        print("3. Login as Admin")
        print("4. Exit")

while True:
    show_menu(role)
    choice = input("Enter your choice: ")

    if role == "admin":
        if choice == "1":
            view_schedule()
        elif choice == "2":
            view_reports()
        elif choice == "3":
            resolve_issue()
        elif choice == "4":
            delete_report()
        elif choice == "5":
            role = None
            username = None
            print("Logged out successfully.\n")
        else:
            print("Invalid choice. Please try again.")

    elif role == "user":
        if choice == "1":
            report_issue(username)
        elif choice == "2":
            view_schedule()
        elif choice == "3":
            role = None
            username = None
            print("Logged out successfully.\n")
        else:
            print("Invalid choice. Please try again.")

    else:
        if choice == "1":
            register_user()
        elif choice == "2":
            username = user_login()
            if username:
                role = "user"
        elif choice == "3":
            username = admin_login()
            if username:
                role = "admin"
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
