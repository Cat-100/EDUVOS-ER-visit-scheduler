from classes.priority_queue import PriorityQueue
from classes.patient import Patient
from models.file_operation_response import FileOperationResponse
from utils.enums.enums import FileOperationalStatus , AppDirectories , FileExtension
from services.file_operations import FileOperations
from utils.helpers.helper_functions import SHelperFunctions
from pathlib import Path

class Scheduler(object):
    ''' 
    Scheduler manages the priority queue of the Clinic. 
    
    Allowing for:
    - Adding of patients to the queue
    - Removing the most critical patient first
    - Printing The list of patients waiting
    - Save Patient Consultations in a file (in the correct ordenance)
    - Read the consultations file

    '''
    # ------------------------------- Functions --------------------------- #

    def __init__(self) -> None:
        ''' Class constructor '''
        self._priority_queue = PriorityQueue()


    def add_patient(self, patient: Patient):
        ''' 
        Adds a `Patient` to the `Priority Queue` 
        
        The priority queue automatically sorts and or optimizes its structure, 
        moving the highest priority patients to the top/head of the queue for easy retrieval.

        **Parameters:**
        - `patient`: The [Patient] that will be added to the [PriorityQueue]
        '''

        self._priority_queue.enqueue(patient)

    def retrieve_next_patient(self) -> Patient:
        ''' 
        Gets the highest prioriy patient from the priority queue.
        
        **Returns:**
        - The highest priority `patient` in the queue.
        '''
        return self._priority_queue.dequeue()
        

    def display_patients_waiting(self) -> None:
        '''
        Loops through the entire priority queue and 
        displays each of the patient details that are currently waiting in the queue
        '''
        for patient  in self._priority_queue:
            patient.display_details()

    def consult_patient(self, patient: Patient , status: str) -> FileOperationResponse:
        ''' 
        Places a status on the patient and saves the consulted patient in the consulted patients folder
        
        **Parameters:**
        - `patient`: The patient that will be consulted.
        - `status`: The patient status given to the patient after consultation.
        '''
        # Assign status
        patient.status = status

        # Save the patient consulted
        return self._save_patient_consultation(patient)
       
    def _save_patient_consultation(self, patient : Patient) -> FileOperationResponse:
        ''' 
        Save a patient that was consulted
        
        **Parameters:**
        - `patient`: The patient that was consulted, will be saved.

        **Returns:**
        - [FileOperationResponse] to indicate if the patient was successfully saved.
        '''
        try:
            # Get the current date
            currentDate = SHelperFunctions.get_current_date()

            # Construct file name
            fileName : str = f"{AppDirectories.CONSULTED_PATIENTS.value}/{currentDate}{FileExtension.TXT.value}"
            
            # Create file path object to check if the file exists 
            file : Path = Path(fileName)

            # Check if the file exists, 
            # overwrite if it does not to make sure a new file is created at the start of each day
            overwriteFile = False
            if not file.exists():
                overwriteFile = True
            
            # Write the patient to the file
            return FileOperations.write_to_file(file , patient.display_as_consulted().split("\n") , overwriteFile)
        except Exception as e:
            # Handle unexpected error
            return FileOperationResponse(FileOperationalStatus.FAILED, f"Unexpected error: {e}")
        
    def read_consulted_patients(self, fileName: str) -> FileOperationResponse:
        ''' 
        Reads and returns the file contents of the file provided as a payload in the [FileOperationResponse].
        
        **Parameters:**
        - `fileName`: The consultation file name that should be checked. Must not have a different directory as [AppDirectories.CONSULTED_PATIENTS.value]
        
        **Returns:**
        - [FileOperationResponse] that indicates the operational status and the payload of the consulted patients file.
        - Note: The payload will only be returned if the [OperationalStatus] is `SUCCESS`
        '''
        try:
            # Create path object to compare
            file = Path(fileName)
            # Ensure that the file provided does not include other directories.
            # It must be the same directory path as [AppDirectories.CONSULTED_PATIENTS]
            if not FileOperations.are_directory_paths_equal(AppDirectories.CONSULTED_PATIENTS.value, file):
                print("Cannot read file. The consultation directory paths are not the same.")
                return

            # Directory paths match, attempt to read the file
            return self._read_consulted_patients_file(fileName)

            # # Process the response
            # match fileOperationResponse.status:
            #     case FileOperationalStatus.FAILED:
            #         print(f"Could not read patient consultation file, {file.name}: Please try again")
            #     case FileOperationalStatus.STOPPED:
            #         print(f"Reading Patient consultation file, {file.name}, was stopped:\n{fileOperationResponse.message}")
            #     case FileOperationalStatus.SUCCESS:
            #         print(f"Successfully read patient consultation file, {file.name}:\n\n{fileOperationResponse.payload}")
        except Exception as e:
            # Handle unexpected error
            print(f"Could not read patient consultation file. Unexpected error occured: {e}")

    def _read_consulted_patients_file(self, fileName: str) -> FileOperationResponse:
        '''
        Attempts to read the consulted patients file and returns a response
        
        **Parameters:**
        - `fileName`: File name representing the file that must be read

        **Returns:**
        - [FileOperationResponse] to indicate the operation status and the contents of the file.
        '''
        try:
            return FileOperations.read_from_txt_file(fileName)
        except Exception as e:
            # Handle unexpected error
            return FileOperationResponse(FileOperationalStatus.FAILED, f"Unexpected error occured: {e}")

    