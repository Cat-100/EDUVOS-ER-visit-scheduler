from classes.patient import Patient
from classes.scheduler import Scheduler
from services.file_operations import FileOperations
from models.file_operation_response import FileOperationResponse 
def main():
    '''Entry point of the application'''
    patient1 = Patient("Paulien" , "hello" , "09384")
    patient2 = Patient("Saskian" , "Louw" ,"0303175087087")
    patient3 = Patient("Anikin" , "Louw" , "0458039850")

    scheduler : Scheduler = Scheduler()

    scheduler.add_patient(patient1)
    scheduler.add_patient(patient2)
    scheduler.add_patient(patient3)
    
    #scheduler.display_patients_waiting()

    FileOperations.write_to_file("debug/testing.txt" , ["Hello my name:" , "Is saskian louw"])
    fileOperationResponse : FileOperationResponse =  FileOperations.read_from_txt_file("debug/testing.txt")
    print(fileOperationResponse.payload)
# Start of the application
main()