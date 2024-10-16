from classes.priority_queue import PriorityQueue
from classes.patient import Patient
import random

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

        # Testing
        patient.priorityLevel = random.randint(1 , 5)
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

    def consult_patient(self, patient: Patient , status: str) -> None:
        ''' Places a status on the patient and loads them into the `consulted_patients` to save`'''
        # Assign status
        patient.status = status

        # TODO: Save consulted patient in text file
        


    