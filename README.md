# EDUVOS-ER-visit-scheduler

Assignment: 
- Given out 9th of Octorber 2024 
- Started 13th of October 2024


This is the first quesiton of the assignment, whereby we are tasked with:

# 1. ER Visit Scheduler: 

You are tasked with creating a Python application that helps the emergency room schedule patients for doctor consultations, by implementing a data structure to keep track of incoming patients. You must select an appropriate data structure to maintain the schedule and ensure that critical patients are catered to first. Your application must have the following:

 

A patient class: Stores the patient’s name, surname, and ID number. Includes a method to print the patient’s information.
(5 Marks)

 

A scheduler class: Used to add patient objects to the schedule, retrieve the next patient, print the list of patients waiting, save patient consultations to a file (in order of occurrence), and read the patient consultations file.
(15 Marks)

 

A class that implements your data structure: Used to maintain the data structure used to schedule patients.
(20 Marks)

 

A main menu: Used for navigating the application. The main menu must display options for all functionalities of the application and must use a sentinel to keep displaying the menu until the application is terminated.
(10 Marks)



# Data structure used for Priority Queueing: Binary Heap

A Binary heap is essentially a tree structure that consists of nodes that taper down to its children.

**A Node:**
- Can at most, have **2** children. Referred to the `left` child and the `right` child
- The `left` child is placed in the node as `2n` based on the node's index `n`
- The `right` child is placed in the node as `2n + 1` based on the node's index `n`



Visual representation:
=======================
                    Node (n)
        |                           |
    Child (2n)                Child (2n + 1)
    



