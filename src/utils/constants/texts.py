class STexts():
    '''Utility class that holds all the texts for the application'''
    # Menu
    menu_title : str= "Clinic ER Visit Scheduler" 
    first_menu_option : str = "(1) Add Patient to Schedule."
    second_menu_option : str = "(2) Retrieve Next Patient."
    third_menu_option :str = "(3) Display All Patients Waiting."
    fourth_menu_option : str = "(4) Read Patient Consultation File"
    fifth_menu_option : str  ="(5) Exit application"

    # Menu inputs
    menu_choice_input =  "Please selected an option from the menu: "
    menu_choice_invalid_input = "Invalid Input. Please select an option from the menu.\nEx. 1"

    # Application terminated
    application_terminated = "Application successfully terminated"

    # Add Patient to Schedul
    add_patient_to_schedule_title = "-- Add Patient to Schedule --"
    add_patient_menu_option_one = "(1) Add Patient"
    add_patient_menu_abort_option = "(2) Abort"
    add_patient_abort_process = "Add Patient to Schedule was Aborted..."
    add_patient_name_input = "Enter Patient Name (Press Enter to Abort): "
    add_patient_surname_input = "Enter Patient Suranem (Press Enter to Abort): "

