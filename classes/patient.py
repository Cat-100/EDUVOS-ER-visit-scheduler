class Patient:
    ''' 
    Class that represents a single `patient` in the private clinic
    
    **Properties:**
    - `name` (str): The name of the patient. Ex. Joe
    - `surname` (str): The surname of the patient. Ex. Soap
    - `idNumber` (str): The ID number of the patient, typically 13 digts. Ex. 9202204720082 
    - `priorityLevel` (str): The priority level between 1 - 5 given to the patient based on their current medical condition.
    - `status` (str): Assigned status after consultation. Ex. 'Follow-up required'
    '''

    # --------------------------- Functions ---------------------------------- #

    def __init__(self , patientName, patientSurname, patientIdNumber) -> None:
        ''' Class Constructor '''
        self.name  = patientName
        self.surname = patientSurname
        self.idNumber = patientIdNumber

    def display_details(self):
        ''' Method that neatly prints the patient details '''
        print(f"Name:\t{self.name}\nSurname:\t{self.surname}\nID Number:\t${self.idNumber}")