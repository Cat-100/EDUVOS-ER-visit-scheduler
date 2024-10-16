from classes.patient import Patient
from classes.scheduler import Scheduler
from services.file_operations import FileOperations
from models.file_operation_response import FileOperationResponse 
from pathlib import Path

def main():
    '''Entry point of the application'''
    patient1 = Patient("Paulien" , "Louw" , "09384")
    patient1.status = "Fell on their head, no fully recovered"
    patient2 = Patient("Saskian" , "Louw" ,"0303175087087")
    patient3 = Patient("Anikin" , "Louw" , "0458039850")

    print()
    file =  Path("test")
    print(f"File directory: {file.parent}")

    scheduler : Scheduler = Scheduler()

    scheduler.add_patient(patient1)
    scheduler.add_patient(patient2)
    scheduler.add_patient(patient3)
    
    #scheduler.display_patients_waiting()

    FileOperations.write_to_file("debug/testing.txt" , ["Hello my name:" , "Is saskian louw"] , overwriteFile=True)
    fileOperationResponse : FileOperationResponse =  FileOperations.read_from_txt_file("debug/testing.txt")
    
# Start of the application
main()