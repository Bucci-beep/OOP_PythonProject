class Patient(object):
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def bmi(self): # Method to calculate BMI from weight and height (BMI = weight (kg) / height (m)²)
        return self.weight / (self.height ** 2)
    
    # Add a method to update the patient’s health record (e.g., adding new measurements or notes).
    def update_health_profile(self, height, weight):
        self.height = height
        self.weight = weight

    # Add a method to print the patient’s health profile.
    def print_health_profile(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")   
        print(f"Gender: {self.gender}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")

# Create a patient object
patient = Patient("John Doe", 30, "M", 1.75, 70)

# Update the patient’s health profile
patient.update_health_profile(1.8, 80)

# Print the patient’s health profile
patient.print_health_profile()
print(f"BMI: {patient.bmi()}")


