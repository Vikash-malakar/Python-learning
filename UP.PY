patients = {}

def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    disease = input("Enter Disease: ")

    patients[patient_id] = {
        "name": name,
        "age": age,
        "disease": disease
    }

    print("Patient Added Successfully")


def view_patients():
    if not patients:
        print("No Patients Found")
        return

    print("\nPatient Records")

    for patient_id, data in patients.items():
        print(
            "ID:", patient_id,
            "| Name:", data["name"],
            "| Age:", data["age"],
            "| Disease:", data["disease"]
        )


def search_patient():
    patient_id = input("Enter Patient ID: ")

    if patient_id in patients:
        data = patients[patient_id]

        print("\nPatient Found")
        print("Name:", data["name"])
        print("Age:", data["age"])
        print("Disease:", data["disease"])
    else:
        print("Patient Not Found")


def delete_patient():
    patient_id = input("Enter Patient ID: ")

    if patient_id in patients:
        del patients[patient_id]
        print("Patient Deleted")
    else:
        print("Patient Not Found")


while True:
    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Delete Patient")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        delete_patient()

    elif choice == "5":
        print("Program Closed")
        break

    else:
        print("Invalid Choice")