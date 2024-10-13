class Patient:
    ''' 
    Class that represents a single `patient` in the private clinic
    
    **Properties:**
    - `name` (str): The name of the patient.
    - `surname` (str): The surname of the patient.
    - `idNumber` (str): The ID number of the patient.
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