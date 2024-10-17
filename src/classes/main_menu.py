from utils.enums.enums import *
from classes.scheduler import Scheduler
from classes.patient import Patient
from utils.constants.texts import STexts
from typing import List, TypeVar , Type , Optional
from utils.helpers.helper_functions import SHelperFunctions
from exceptions.exceptions import AbortProcess
from utils.validators.validators import SValidators

class MainMenu(object):
    ''' 
    Object class that represents the main menu of the ER application. 
    
    Contains the _scheduler, business and GUI logic to allow the user to:
    - Add patients to the _scheduler
    - Retrieve Patients in the queue. Consult them after being retrieved
    - Display all patients in the waiting queue
    - Read a Patient Consultation File
    - Exit the application
    
    **Properties:**
    - `_stop_application`: Sentinal value that stops the application when its value becomes `True`
    - `_scheduler`: The [scheduler] object that manages the priority queue of patients.
    '''

    # Setup
    # Generics
    T = TypeVar('T' , bound=MenuOption)
    
    # --------------------------- Functions ----------------------------- #

    def __init__(self) -> None:
        '''Constructor for the class'''
        self._stop_application = False 
        self._stop_menu_process = False
        self._scheduler = Scheduler()

    def start(self):
        '''Starts the application, running the main menu until the user exists the application.'''
        # Continue displaying, running the application, until terminate or stop application is selected
        while self._stop_application == False:
            # Display menu
            self._display_chosen_option_menu(OptionMenu.MAIN)

            # Get User Choice
            menu_option_made : MainMenuOption = self._get_menu_choice(MainMenuOption , STexts.menu_choice_input) 

            # Handle the user choice made
            self._handle_menu_option_selected(menu_option_made)

    def _get_menu_choice(self , menu_type: Type[T] , prompt : str) -> T:
        '''Get the relative menu option'''
        menu_choice : Optional[T] = None
        while menu_choice is None:
            menu_choice_str =  input(prompt)
            
            try:
                # Attempt to convert input to an int and get the correct Menu Option
                menu_choice = int(menu_choice_str)
            
                # Convert int choice to enum value
                menu_choice = menu_type.from_value(menu_choice)

                # Handle edge case where the value is not in the range of the options provided
                if menu_choice is None:
                    raise ValueError
                
                # Valid choice, return
                return menu_choice

            except ValueError:
                # Handle case where the user provided a input that was not valid
                print(STexts.menu_choice_invalid_input)

    def _display_chosen_option_menu(self , menu_type: OptionMenu ) -> None:
        match menu_type:
            case OptionMenu.MAIN:
                '''Prints the main menu for the user to use and select a option'''
                print(STexts.menu_title)
                print("------------------------------------------")
                print(STexts.first_menu_option)
                print(STexts.second_menu_option)
                print(STexts.third_menu_option)
                print(STexts.fourth_menu_option)
                print(STexts.fifth_menu_option)
                print()
            case OptionMenu.ADD_PATIENT_TO_SCHEDULE:
                '''Displays a mini menu for adding a patient to the schedule'''
                print(STexts.add_patient_to_schedule_title)
                print(STexts.add_patient_menu_option_one)
                print(STexts.add_patient_menu_abort_option)
            case OptionMenu.RETRIEVE_NEXT_PATIENT:
                '''Displays The Retrieve Next Patient Menu'''
                print(STexts.retrieve_next_patient_title)
                print(STexts.retrieve_next_menu_option_one)
                print(STexts.retrieve_next_menu_option_two)

    def _handle_menu_option_selected(self, menu_option: T , patient: Optional[Patient] = None) -> None:
        '''Invokes certain process based on the Main Menu Option provided'''
        # Add spacing for readability
        if isinstance(menu_option, MainMenuOption):
            # Main Menu Option operations
            match menu_option:
                case MainMenuOption.ADD_PATIENT_TO_SCHEDULE:
                    self._start_add_patient_process()
                case MainMenuOption.RETRIEVE_NEXT_PATIENT:
                    self._start_retrieve_next_patient_process()
                case MainMenuOption.DISPLAY_ALL_PAIENTS_WAITING:
                    pass
                case MainMenuOption.READ_PATIENT_CONSULTATION_FILE:
                    pass
                case MainMenuOption.EXIT_APPLICATION:
                    self._exit_application()
        if isinstance(menu_option , AddPatientMenuOption):
            # Add Patient Menu Options
            print()
            match menu_option:
                case AddPatientMenuOption.ADD_PATIENT:
                    self._add_patient_option()
                case AddPatientMenuOption.ABORT:
                    self._abort_menu_process()
        if isinstance(menu_option , RetrieveNextPatientMenuOption):
            # Retrieve and consult patient options
            print()
            match menu_option:
                case RetrieveNextPatientMenuOption.RETREIVE_AND_CONSULT_PATIENT:
                    self._retrieve_and_consult_patient()
                case RetrieveNextPatientMenuOption.ABORT:
                    self._abort_menu_process()


    def _abort_menu_process(self) -> None:
        '''Aborts a Currently Active Menu Process'''
        self._stop_menu_process = True
        print(STexts.add_patient_abort_process)
    
    # =========================== Main Menu Option Functions ============================== #
    #  ---------------------- Add Patient to Schedule --------------------------- #

    def _get_patient_info(self, prompt: str) -> str:
        info: str = None
        while info is None:
            info = str(input(prompt))

            return info

        
    def _get_patient_id_number(self) -> str:
        patient_id : str = None
        while patient_id is None:
            # Get the Patient ID
            patient_id =  input(STexts.add_patient_id_input)
            if SHelperFunctions.is_empty(patient_id) : raise AbortProcess # Abort process if empty
            
            # Validate if the id number is correct
            validate : str =  SValidators.validate_id_number(patient_id)
            
            # Display the error or continue
            if (validate != None):
                patient_id = None
                print(validate)
            else: 
                # Return patient id if the id is valid
                return patient_id

    def _get_patient_priority_level(self) -> int:
        patient_priority_level : int = None
        while patient_priority_level is None:
            # Get the Patient Priority Level
            patient_priority_level_str =  input(STexts.add_patient_priority_level_input)
            if SHelperFunctions.is_empty(patient_priority_level_str) : raise AbortProcess # Abort process if empty
            
            # Attempt to parse value
            try:
                patient_priority_level = int(patient_priority_level_str)

                # Validate the priority level
                if not( 1 <= patient_priority_level <= 5):
                    raise ValueError

                return patient_priority_level
            except ValueError as e:
                print("Invalid Priority level. Enter a number between 1 - 5")
                patient_priority_level = None            
            

    def _add_patient_option(self) -> None:
        '''Add the patient being populated to the schedule'''
        try:
            # Get the patient name
            patient_name : str = self._get_patient_info(STexts.add_patient_name_input)
            if SHelperFunctions.is_empty(patient_name) : raise AbortProcess # Abort if empty
            
            # Get the Patient Surname
            patient_surname : str = self._get_patient_info(STexts.add_patient_surname_input)
            if SHelperFunctions.is_empty(patient_surname)  : raise AbortProcess # Abort if empty

            # Get Patient ID Number 
            patient_id : str = self._get_patient_id_number()
            
            # Assign Patient priority level
            patient_priority_level : int = self._get_patient_priority_level()

            # Consturct Patient Object
            new_patient : Patient = Patient(patient_name , patient_surname, patient_id, patient_priority_level)
            
            # Add patient to the scheduler
            self._scheduler.add_patient(new_patient) 
            
            # Provide feeback
            print(f"{STexts.add_patient_success_feedback} {new_patient.name} {new_patient.surname}")
        except AbortProcess:
            # Handle abort process
            return
        
    def _start_add_patient_process(self) -> None:
        '''Starts the Add Patient Process'''
        self._stop_menu_process = False
        while not self._stop_menu_process:
            # Display Patient Menu Options
            self._display_chosen_option_menu(OptionMenu.ADD_PATIENT_TO_SCHEDULE)

            # Get menu option
            menu_option : AddPatientMenuOption = self._get_menu_choice(AddPatientMenuOption , STexts.menu_choice_input)
            
            # Handle the menu option selected
            self._handle_menu_option_selected(menu_option)

    # -------------------- Retrieve Next Patient ---------------------- #
    def _retrieve_and_consult_patient(self) -> None:
        try:
            # Retrieve patient
            retrieved_patient = self._scheduler.retrieve_next_patient()

            # Display the patient details for the doctor to use and consult the patient
            print(retrieved_patient.display_details())

            # Get status.
            patient_status : str  = self._get_patient_info(STexts.patient_status_input)
            if SHelperFunctions.is_empty(patient_status) : raise AbortProcess

            # Add the status to the 
        except AbortProcess:
            # Reinsert the retrieved patient if the process was aborted
            self._scheduler.add_patient(retrieved_patient)
        except IndexError as e:
            print("No patients available to be consulted.")
            

    def _start_retrieve_next_patient_process(self) -> None:
        '''Starts the Next Patient process'''
        self._stop_menu_process = False
        while not self._stop_menu_process:
            # Display Patient Menu Options
            self._display_chosen_option_menu(OptionMenu.RETRIEVE_NEXT_PATIENT)

            # Get menu option
            menu_option : AddPatientMenuOption = self._get_menu_choice(AddPatientMenuOption , STexts.menu_choice_input)
            
            # Handle the menu option selected
            self._handle_menu_option_selected(menu_option)
        
    #  ---------------------- Exit Application --------------------------- #
    def _exit_application(self):
        '''Terminates the application by setting the sentinal'''
        self._stop_application = True
        print(STexts.application_terminated)
    
