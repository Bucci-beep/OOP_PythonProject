class SurgeryAppointment:
    '''
    This represents a surgery appointment for a patient with details such as
    patient name, surgery type and the scheduled date and time.
    '''
    def __init__(self, patient_name, surgery_type, date, time):
        '''
        This initializes a new surgery appointment instance.
        '''
        self.patient_name = patient_name
        self.surgery_type = surgery_type
        self.date = date
        self.time = time

    def __str__(self):
        '''
        This returns a string representation of the surgery appointment.
        '''
        return f'{self.patient_name} - {self.surgery_type} - {self.date} - {self.time}'
    

from datetime import datetime

class SurgeryAppointmentScheduler:
    '''
    Manages a list of surgical appointments with functionalities to add, update,
    cancel and list appointments in chronological order.
    '''
    def __init__(self):
        '''
        Initializes a new surgery appointment scheduler with an empty list of appointments.
        '''
        self.appointments = []

    def add_appointment(self, appointment):
        '''
        Adds a new surgery appointment to the scheduler.
        '''
        self.appointments.append(appointment)

    def update_appointment(self, index, new_appointment):
        '''
        Updates an existing appointment at the specified index.
        '''
        if 0 <= index < len(self.appointments):
            self.appointments[index] = new_appointment
        else:
            raise IndexError('Invalid appointment index')
        
    def cancel_appointment(self, index):
        '''
        Cancels an existing appointment at the specified index.
        '''
        if 0 <= index < len(self.appointments):
            removed = self.appointments.pop(index)
            print(f'Cancelled appointment: {removed}')
        else:
            raise IndexError('Invalid appointment index')
        
    def display_schedule(self):
        '''
        Displays the list of appointments in chronological order.
        '''
        # Helper function to combine date and time and convert to datetime object
        def appointment_datetime(appointment):
            return datetime.strptime(f'{appointment.date} {appointment.time}', '%Y-%m-%d %H:%M')
        
        sorted_appointments = sorted(self.appointments, key=appointment_datetime)
        for appointment in sorted_appointments:
            print(appointment)

if __name__ == '__main__':
    # Create a Scheduler instance
    scheduler = SurgeryAppointmentScheduler()
    
    # Add some appointments
    apt1 = SurgeryAppointment('Alice', 'Knee Surgery', '2021-06-15', '10:00')
    apt2 = SurgeryAppointment('Bob', 'Hip Replacement', '2021-06-20', '14:00')
    apt3 = SurgeryAppointment('Charlie', 'Shoulder Surgery', '2021-06-25', '09:00')

    # Add the appointments to the scheduler
    scheduler.add_appointment(apt1)
    scheduler.add_appointment(apt2)
    scheduler.add_appointment(apt3)

    # Display the initial schedule in chronological order
    print('Initial Schedule:')
    scheduler.display_schedule()

    # Update the second appointment
    new_apt2 = SurgeryAppointment('Bob', 'Hip Replacement', '2021-06-20', '15:30')
    scheduler.update_appointment(1, new_apt2)

    # Display the updated schedule in chronological order
    print('\nUpdated Schedule:')
    scheduler.display_schedule()

    # Cancel the first appointment
    scheduler.cancel_appointment(0)

    # Display the final schedule in chronological order
    print('\nFinal Schedule:')
    scheduler.display_schedule()