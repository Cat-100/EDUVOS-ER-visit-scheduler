class Patient(object):
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

    def __init__(self , patientName : str, patientSurname: str, patientIdNumber: str , priorityLevel: int) -> None:
        ''' Class Constructor '''
        self.name: str = patientName
        self.surname : str = patientSurname
        self.idNumber: str = patientIdNumber
        self.priorityLevel : int = priorityLevel
        self.status : str = ""

    def display_details(self):
        ''' Method that neatly prints the patient details '''
        print(f"Name:\t\t{self.name}\nSurname:\t{self.surname}\nID Number:\t{self.idNumber}\nPriority Level: {self.priorityLevel}")

    def display_as_consulted(self):
        ''' Method that neatly prints the patient details in a text file format that can easily be read'''
        return f"\t{self.name} {self.surname}\n---------------------------------\nID Number: {self.idNumber}\nStatus:\n{self.status}"