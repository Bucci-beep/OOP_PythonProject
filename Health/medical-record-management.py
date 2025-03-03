class Medical_record(object):
    def __init__(self, patient_id, patient_name):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.appointments = []
        self.test_results = []
        self.diagnoses = []

# Add a method to add a new appointment to the patient’s medical record.
    def add_appointment(self, date, time, doctor, notes):
        self.appointments.append({"date": date, "time": time, "doctor": doctor, "notes": notes})

# Add a method to add a new test result to the patient’s medical record.
    def add_test_result(self, date, test_name, result):
        self.test_results.append({"date": date, "test_name": test_name, "result": result})

# Add a method to add a new diagnosis to the patient’s medical record.
    def add_diagnosis(self, date, doctor, diagnosis, notes, treatment):
        self.diagnoses.append({"date": date, "doctor": doctor, "diagnosis": diagnosis, "notes": notes, "treatment": treatment})

# Add a method to print the patient’s medical record.
    
    def print_medical_record(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Patient Name: {self.patient_name}")
        print("\nAppointments:")
        for appointment in self.appointments:
            print(f"Date: {appointment['date']}")
            print(f"Time: {appointment['time']}")
            print(f"Doctor: {appointment['doctor']}")
            print(f"Notes: {appointment['notes']}")
            print()
        print("\nTest Results:")
        for test_result in self.test_results:
            print(f"Date: {test_result['date']}")
            print(f"Test Name: {test_result['test_name']}")
            print(f"Result: {test_result['result']}")
            print()

        print("\nDiagnoses:")

        for diagnosis in self.diagnoses:
            print(f"Date: {diagnosis['date']}")
            print(f"Doctor: {diagnosis['doctor']}")
            print(f"Diagnosis: {diagnosis['diagnosis']}")
            print(f"Notes: {diagnosis['notes']}")
            print(f"Treatment: {diagnosis['treatment']}")
            print()

# Create a medical record object
medical_record = Medical_record(1, "John Doe")

# Add appointments to the patient’s medical record
medical_record.add_appointment("2021-01-01", "09:00", "Dr. Smith", "Follow-up appointment")
medical_record.add_appointment("2021-02-01", "10:00", "Dr. Johnson", "Annual check-up")

# Add test results to the patient’s medical record
medical_record.add_test_result("2021-01-15", "Blood Test", "Normal")
medical_record.add_test_result("2021-02-15", "X-Ray", "No abnormalities detected")

# Add diagnoses to the patient’s medical record
medical_record.add_diagnosis("2021-01-20", "Dr. Brown", "Influenza", "Prescribed rest and fluids", "None")
medical_record.add_diagnosis("2021-02-20", "Dr. White", "Hypertension", "Prescribed medication and lifestyle changes", "Follow-up in 3 months")

# Print the patient’s medical record
medical_record.print_medical_record()
