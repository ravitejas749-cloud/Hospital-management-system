# Hospital Management System

patients = {}
appointments = []
bills = {}

# ---------------- Patient Management ----------------
def add_patient():
    pid = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")

    patients[pid] = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Disease": disease
    }
    print("✅ Patient added successfully!\n")

def view_patients():
    if not patients:
        print("No patient records found.\n")
        return

    for pid, info in patients.items():
        print(f"\nPatient ID: {pid}")
        for key, value in info.items():
            print(f"{key}: {value}")
    print()

# ---------------- Appointment Management ----------------
def add_appointment():
    pid = input("Enter Patient ID: ")
    if pid not in patients:
        print("❌ Patient not found.\n")
        return

    doctor = input("Enter Doctor Name: ")
    date = input("Enter Appointment Date (DD-MM-YYYY): ")

    appointments.append({
        "Patient ID": pid,
        "Doctor": doctor,
        "Date": date
    })
    print("✅ Appointment scheduled successfully!\n")

def view_appointments():
    if not appointments:
        print("No appointments found.\n")
        return

    for app in appointments:
        print(app)
    print()

# ---------------- Billing Management ----------------
def generate_bill():
    pid = input("Enter Patient ID: ")
    if pid not in patients:
        print("❌ Patient not found.\n")
        return

    amount = float(input("Enter Bill Amount: "))
    bills[pid] = amount
    print("✅ Bill generated successfully!\n")

def view_bills():
    if not bills:
        print("No bills found.\n")
        return

    for pid, amount in bills.items():
        print(f"Patient ID: {pid}, Bill Amount: ₹{amount}")
    print()

# ---------------- Main Menu ----------------
def main():
    while True:
        print("===== Hospital Management System =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Add Appointment")
        print("4. View Appointments")
        print("5. Generate Bill")
        print("6. View Bills")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            add_appointment()
        elif choice == "4":
            view_appointments()
        elif choice == "5":
            generate_bill()
        elif choice == "6":
            view_bills()
        elif choice == "7":
            print("👋 Exiting Hospital Management System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

# Run the program
main()