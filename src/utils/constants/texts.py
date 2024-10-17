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
    add_patient_surname_input = "Enter Patient Surname (Press Enter to Abort): "
    add_patient_id_input = "Enter Patient ID (Press Enter to Abort): "
    add_patient_priority_level_input = "Enter Patient Priority Level (Press Enter to Abort): "
    add_patient_success_feedback = "Successfully added patient: "

    # Retrieve Next Patient
    retrieve_next_patient_title = "-- Retrieve Next Patient --"
    retrieve_next_menu_option_one = "(1) Retrieve and Consult Patient"
    retrieve_next_menu_option_two = "(2) Abort"
    patient_status_input = "Enter Patient Status (Press Enter to Abort): "
    no_patients_available_to_consult = "No patients available to be consulted."

    # Display All Patients Waiting
    display_all_patients_waiting_title = "-- Display All Patients Waiting --"
    display_all_patients_waiting_menu_option_one = "(1) Display"
    display_all_patients_waiting_menu_option_two = "(2) Abort"

    # Read Patient Consultation File
    read_patient_consultation_file_title = "-- Read Patient Consultation File --"
    read_patient_consultation_file_menu_option_one = "(1) Display Files"
    read_patient_consultation_file_menu_option_two = "(2) Abort"