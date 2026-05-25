# College Event Management System (Console Application)

events = []
registrations = []
attendance = []

# Login
def login():
    print("\n===== LOGIN =====")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "123":
        print("Login Successful!\n")
        menu()
    elif username == "Jerli" and password == "jerli@123":
        print("Login Successful!\n")
        menu()
    else:
        print("Invalid Credentials")

# Create Event
def create_event():
    print("\n--- Create Event ---")

    event = {
        "id": len(events) + 1,
        "title": input("Event Title: "),
        "date": input("Date: "),
        "venue": input("Venue: ")
    }

    events.append(event)
    print("Event Created Successfully!")

# View Events
def view_events():
    print("\n--- Event List ---")

    if len(events) == 0:
        print("No Events Available")
        return

    for e in events:
        print(
            f"ID:{e['id']} | "
            f"Title:{e['title']} | "
            f"Date:{e['date']} | "
            f"Venue:{e['venue']}"
        )

# Register Event
def register_event():
    student = input("Student Name: ")
    event_id = int(input("Event ID: "))

    registrations.append({
        "student": student,
        "event": event_id
    })

    print("Registration Successful")

# Attendance
def mark_attendance():
    student = input("Student Name: ")
    status = input("Present/Absent: ")

    attendance.append({
        "student": student,
        "status": status
    })

    print("Attendance Recorded")

# Report
def generate_report():
    print("\n===== REPORT =====")

    print("Total Events:", len(events))
    print("Total Registrations:", len(registrations))
    print("Attendance Records:", len(attendance))

# Menu
def menu():
    while True:

        print("""
===== COLLEGE EVENT MANAGEMENT =====

1. Create Event
2. View Events
3. Register Event
4. Mark Attendance
5. Generate Report
6. Exit
""")

        choice = input("Enter Choice: ")

        if choice == "1":
            create_event()

        elif choice == "2":
            view_events()

        elif choice == "3":
            register_event()

        elif choice == "4":
            mark_attendance()

        elif choice == "5":
            generate_report()

        elif choice == "6":
            print("Thank You")
            break

        else:
            print("Invalid Choice")

# Start
login()