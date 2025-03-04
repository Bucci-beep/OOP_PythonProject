class Patient:
    """
    This class represents a patient in the Emergency Room.
    """
    def __init__(self, name, symptoms):
        """
        Initializes a new Patient object with the given name and symptoms.
        """
        self.name = name
        self.symptoms = symptoms
        self.triage_level = 0 # Default triage level is 0, set later via the determine_priority() method

    def determine_priority(self, chest_pain = False, breathing_difficulty = False, bleeding = False, loss_of_consciousness = False, pain_level = 0):
        """
        Determines and assign the patient's triage level based on their symptoms.

        Triage rules:
          - If any of chest pain, difficulty breathing, bleeding, or loss of consciousness is True,
            assign triage level 1 (Critical).
          - If pain_level > 7, assign triage level 2 (Serious).
          - If pain_level > 5, assign triage level 3 (Moderate).
          - Otherwise, assign triage level 4 (Minor).
          Args:
            chest_pain (bool): True if the patient experiences chest pain.
            difficulty_breathing (bool): True if the patient experiences difficulty breathing.
            bleeding (bool): True if the patient is bleeding.
            loss_of_consciousness (bool): True if the patient has lost consciousness.
            pain_level (int or float): A numerical pain level, e.g., on a scale from 0 to 10.

        """
        if chest_pain or breathing_difficulty or bleeding or loss_of_consciousness:
            self.triage_level = 1
        elif pain_level > 7:
            self.triage_level = 2
        elif pain_level > 5:
            self.triage_level = 3
        else:
            self.triage_level = 4

            def get_triage_description(self):
                """
                Returns a human-readable description of the patient's triage level.

                Returns:
            str: A description corresponding to the triage level.
                """
                if self.triage_level == 1:
                    return "Critical"
                elif self.triage_level == 2:
                    return "Serious"
                elif self.triage_level == 3:
                    return "Moderate"
                elif self.triage_level == 4:
                    return "Minor"
                else:
                    return "Unknown"

            def __str__(self):
                """
                Returns a string representation of the Patient object.
                """
                return f"Patient: {self.name}, Symptoms: {self.symptoms}, Triage Level: {self.get_triage_description()}"
                
    def sort_patients(patients):
        """
        Sorts the given list of Patient objects by their triage level in ascending order.

        Args:
            patients (list): A list of Patient objects.

        Returns:
            list: A sorted list of Patient objects.
        """
        # Ensure patients with undetermined triage levels are sorted last (using infinity as a placeholder)
        sorted_patients = sorted(patients, key=lambda p: p.triage_level if p.triage_level is not None else float('inf'))
        for patient in sorted_patients:
            print(patient)
        return sorted_patients
    
# Create a list of Patient objects with different symptoms
patients = [
    Patient("Alice", "Chest pain", 1),
    Patient("Bob", "Difficulty breathing", 1),
    Patient("Charlie", "Bleeding", 1),
    Patient("David", "Loss of consciousness", 1),
    Patient("Eve", "Back pain", 8),
    Patient("Frank", "Headache", 6),
    Patient("Grace", "Sore throat", 4)
]

# Determine and assign triage levels to each patient using appropriate parameters
patients[0].determine_priority(chest_pain=True)
patients[1].determine_priority(breathing_difficulty=True)
patients[2].determine_priority(bleeding=True)
patients[3].determine_priority(loss_of_consciousness=True)
patients[4].determine_priority(pain_level=8)
patients[5].determine_priority(pain_level=6)
patients[6].determine_priority(pain_level=4)

# Sort and display the list of patients by their triage priority
sorted_patients = sort_patients(patients)
