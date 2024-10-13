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
        # Create nodes to hold all the elements
        self.nodes = []


