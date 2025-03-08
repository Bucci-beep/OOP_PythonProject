class Medication:
    def __init__(self, name, quantity, dosage, expiration_date):
        self.name = name
        self.quantity = quantity
        self.dosage = dosage
        self.expiration_date = expiration_date

    def update_quantity(self, amount):
        """
               Updates the quantity of the medication.

               Parameters:
               amount (int): The number of units to add (positive) or dispense (negative).

               Raises:
               ValueError: If the resulting quantity would be negative.
        """

        if self.quantity + amount < 0:
              raise ValueError("Insufficient stock to dispense the requested amount")
        self.quantity += amount

    def __str__(self):
        return (f"Medication(name={self.name}, quantity={self.quantity},"
                f"dosage={self.dosage}, expiration_date={self.expiration_date})")

class InventoryManager:
    def __init__(self):
        # A dictionary to store medication objects with their name as the key
        self.medications = {}

    def add_new_medication(self, medication):
        # Add medication to the dictionary using its name as the key
        self.medications[medication.name] = medication

    def update_stock(self, medication_name, quantity):
        if medication_name in self.medications:
           try:
            self.medications[medication_name].update_quantity(quantity)
            print(f"Updated stock for {medication_name}: {self.medications[medication_name].quantity}")
           except ValueError as e:
               print(f"Error: {e}")
        else:
            print(f"Medication '{medication_name}' not found in Inventory")

    def check_low_stock(self, threshold):
        for med_name, med in self.medications.items():
            if med.quantity < threshold:
                print(f"ALERT: {med_name} is running low with only {med.quantity} units left!")


if __name__ == "__main__":
    # Create medication instances
    med1 = Medication("Paracetamol", 50, "500mg", "2025-12-31")
    med2 = Medication("Ibuprofen", 20, "200mg", "2024-10-15")

    # Create InventoryManager Instance
    inventory = InventoryManager()

    # Add medications
    inventory.add_new_medication(med1)
    inventory.add_new_medication(med2)

    # Update Stock
    inventory.update_stock("Paracetamol", -10)  # Dispense 10 units
    inventory.update_stock("Ibuprofen", 5)  # Add 5 units

    # Check low stock with a threshold of 15
    inventory.check_low_stock(30)

    # Attempt to dispense more than available quantity
    inventory.update_stock("Paracetamol", -50)  # Should raise an error
