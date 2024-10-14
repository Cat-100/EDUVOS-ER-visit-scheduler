from classes.patient import Patient
from classes.priority_queue import PriorityQueue

def main():
    '''Entry point of the application'''
    patient1 = Patient("Paulien" , "hello" , "09384")
    patient1.priorityLevel = 3
    patient2 = Patient("Saskian" , "Louw" ,"0303175087087")
    patient2.priorityLevel = 5
    patient3 = Patient("Anikin" , "Louw" , "0458039850")
    patient3.priorityLevel = 2

    priorityQueue : PriorityQueue = PriorityQueue()
    priorityQueue.enqueue(patient1)
    priorityQueue.enqueue(patient2)
    priorityQueue.enqueue(patient3)


   
    priorityQueue.dequeue()

    for patient  in priorityQueue.nodes:
        print(patient.display_details())

# Start of the application
main()