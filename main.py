from classes.patient import Patient
from classes.scheduler import Scheduler

def main():
    '''Entry point of the application'''
    patient1 = Patient("Paulien" , "hello" , "09384")
    patient2 = Patient("Saskian" , "Louw" ,"0303175087087")
    patient3 = Patient("Anikin" , "Louw" , "0458039850")

    scheduler : Scheduler = Scheduler()

    scheduler.add_patient(patient1)
    scheduler.add_patient(patient2)
    scheduler.add_patient(patient3)
    
    scheduler.display_patients_waiting()
# Start of the application
main()