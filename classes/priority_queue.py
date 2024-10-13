from classes.patient import Patient
from typing import List
from utils.helpers.helper_functions import SHelperFunctions
class PriorityQueue:
    ''' 
    Priority Queue that utilizes the Binary Heap tree structure to queue, dequeue, 
    and ensure quick retrieval of `patients` based on their `priority level` 
    
    **Why Binary Heap tree structure?**
    Lists:
    - Commonly utilize contingious memeory blocks
    - Meaning, lists/arrays need to be appended and additioanl memory blocks need to be assigned to dynamically grow the list.
    - Resulting in unnecessary memory usage and a time complexity of O(n) when enqueing and dequeing the patient.
    - The time complexity can be improved.

    Linked lists:
    - Commonly utilized to create queues or stacks. 
    - Queues use FIFO.
    - Stacks use LIFO.
    - The data structure might have worked on a base queue but it the clinic requires that patients be treated based on their priority level.
    - Enqueing and dequeing into the linked list will be effective, time complexity of O(1).
    - But quering it to find patients with a higher priority level will be slow, nodes are linked based on a reference to the new node, meaning that to find the highest priority level, the structure will need to be looped through multiple times, creating a time complexity potentially highter than O(n)
    - It needs to be improved upon. 
    

    **Binary Tree Rules:**
    - Insertion: All elements must be inserted on the tree and the heapified, meaning that it needs to be moved to the top or bottom based on the priority level.
    In this case, patients with a higher priority level, > 1, will be moved up the binary tree.

    **Node Structure:**
    Node (n) || Child (2n) || Child (2n + 1)

    **Properties:**
    - `root`: The root of the binary tree, top most node of the tree.
    - `nodes`: The list of nodes in the binary tree, can be a whole new node or a child to a node. 
    '''

    # ------------------------------ Functions ------------------------------- #
    def __init__(self) -> None:
        ''' Class Constructor '''
        # Create list of nodes to hold all the elements
        self.nodes : List[Patient] = []

    def enqueue(self, patient : Patient) -> None:
        '''
        Ádds a Patient to the queue. 
        
        Will heapify based on the patient's priority level. 5 being the most sever.
        '''
        # Add patient to the end of the list
        self.nodes.append(patient)

        # Heapify the nodes
        self._heapify(len(self.nodes) - 1)

    def _heapify(self, index: int) -> None:
        '''Moves current node on the tree based on the priority level'''
        # Relevant indices
        parentIndex = self.determineParentIndex(index)
        childIndex = index

        # Compare the child node with the parent node and swap if needed
        while index > 0 and self.nodes[childIndex].priorityLevel > self.nodes[parentIndex].priorityLevel:
            # Swap the nodes
            SHelperFunctions.swap_element_in_list(self.nodes , parentIndex , childIndex)
            
            # Perform the next iteration to ensure that the highest proiorty has been allocated
            # Move up to the parent node
            index = parentIndex  
            # Calculate the new parent index
            parentIndex = self.determineParentIndex(index)

    def determineParentIndex(self , index: int) -> int:
        return (index - 1)//2
    
    def dequeue(self) -> Patient: 
        ''''
        Returns the top most element in the queue; highest priority patient
        
        Dequeue:
        - First retrieves the root node; the highest priority patient
        - Removes the last element from the queue
        - Assigns the last eleement as the root element
        - Performs deheapifying to ensure that the binary heap properties are retained.

        **Returns:**
        - `Patient` on top of the queue. Highest Priority patient
        '''
        # Ensure that the queue has elements in it
        if SHelperFunctions.is_empty(self.nodes): # Check if the array is empty
            raise IndexError("dequeue from an empty priority queue")
        
        # Remove the root node to return
        rootNode = self.nodes[0]
        # Get the last element of the binary tree.
        lastNode = self.nodes.pop()
        
        if not SHelperFunctions.is_empty(self.nodes): # Ensure that there are nodes in the tree before deheapifying
            # Replace the root node with the last node
            self.nodes[0] = lastNode

            # Deheapify the node to ensure that the binary heap properties are upheld.
            self._deheapify(0)
        
        # Return the root node
        return rootNode

    def _deheapify(self , index : int) -> None:
        ''' 
        Normalizes the binary tree by making sure the tree's node are correctly placed 
        
        **Parameters:**
        - `index`: The node's index provided, the starting point of the deheapify.
        '''
        # get the length of the nodes
        nodeLength = len(self.nodes)
        while  index < nodeLength:
            # Determine indices. Note: + 1 was added to normalize the array
            leftChildIndex = index * 2 + 1  # 2n
            rightChildIndex = (index * 2) + 2 # 2n + 1
            largestIndex = index # Start with the supplied index

            # Left Child: 2n
            if (leftChildIndex < nodeLength and self.nodes[leftChildIndex].priorityLevel > self.nodes[largestIndex].priorityLevel):
                # Move the main index to the child moved
                largestIndex = leftChildIndex
                
            # Right Child: 2n + 1
            if (rightChildIndex < nodeLength and  self.nodes[rightChildIndex].priorityLevel > self.nodes[largestIndex].priorityLevel):
                # Move the main index to the child moved
                largestIndex = rightChildIndex

            # Swap elements if there was a change in the largest index, which indicates that a child had a higher priority
            if  largestIndex != index:
                # Swap elements when there was a change in the largest index
                SHelperFunctions.swap_element_in_list(self.nodes, index, largestIndex)
                index = largestIndex
            else: 
                # Break as the index has not changed, meaning that the current node is the highest node
                break



