from utils.enums.enums import MainMenuOption , MenuOption, AddPatientMenuOption
from classes.scheduler import Scheduler
from classes.patient import Patient
from utils.constants.texts import STexts
from typing import List, TypeVar , Type , Optional
from utils.helpers.helper_functions import SHelperFunctions
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
        self._stop_add_patient_process = False
        self._scheduler = Scheduler()

    def start(self):
        '''Starts the application, running the main menu until the user exists the application.'''
        # Continue displaying, running the application, until terminate or stop application is selected
        while self._stop_application == False:
            # Display menu
            self._display_main_menu()

            # Get User Choice
            menu_option_made : MainMenuOption = self._get_menu_choice(MainMenuOption , STexts.menu_choice_input) 

            # Handle the user choice made
            self._handle_menu_option_selected(menu_option_made)

            

    def _display_main_menu(self) -> None:
        '''Prints the main menu for the user to use and select a option'''
        print(STexts.menu_title)
        print("------------------------------------------")
        print(STexts.first_menu_option)
        print(STexts.second_menu_option)
        print(STexts.third_menu_option)
        print(STexts.fourth_menu_option)
        print(STexts.fifth_menu_option)
        print()

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

    def _handle_menu_option_selected(self, menu_option: T , patient: Optional[Patient] = None) -> None:
        '''Invokes certain process based on the Main Menu Option provided'''
        # Add spacing for readability
        if isinstance(menu_option, MainMenuOption):
            # Main Menu Option operations
            match menu_option:
                case MainMenuOption.ADD_PATIENT_TO_SCHEDULE:
                    self._start_add_patient_process()
                case MainMenuOption.RETRIEVE_NEXT_PATIENT:
                    pass
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
                    self._abort_add_patient_process()
            
    # =========================== Main Menu Option Functions ============================== #
    #  ------------------------------ Add Patient to Schedule --------------------------- #
    def _display_add_patient_to_schedule_menu(self) -> None:
        '''Displays a mini menu for adding a patient to the schedule'''
        print(STexts.add_patient_to_schedule_title)
        print(STexts.add_patient_menu_option_one)
        print(STexts.add_patient_menu_abort_option)

    def _get_patient_info(self, prompt: str) -> str:
        info: str = None
        while info is None:
            info = str(input(prompt))

            return info

        
    #def _get_patient_id_number() -> str:


    def _add_patient_option(self) -> None:
        '''Add the patient being populated to the schedule'''
        # Get the patient name
        patient_name : str = self._get_patient_info(STexts.add_patient_name_input)
        if SHelperFunctions.is_empty(patient_name) == True : return # Abort if empty
        
        # Get the Patient Surname
        patient_surname : str = self._get_patient_info(STexts.add_patient_surname_input)
        if SHelperFunctions.is_empty(patient_name) == True : return # Abort if empty

        # Get Patient ID Number 

    def _abort_add_patient_process(self) -> None:
        '''Aborts the Add Patient Process'''
        self._stop_add_patient_process = True
        print(STexts.add_patient_abort_process)

    def _start_add_patient_process(self) -> None:
        '''Starts the Add Patient Process'''
        # Declare global to handle the patient process
        self._stop_add_patient_process = False
        while not self._stop_add_patient_process:
            # Display Patient Menu Options
            self._display_add_patient_to_schedule_menu()

            # Get menu option
            menu_option : AddPatientMenuOption = self._get_menu_choice(AddPatientMenuOption , STexts.menu_choice_input)
            
            # Handle the menu option selected
            self._handle_menu_option_selected(menu_option)

    #  ------------------------------ Exit Application --------------------------- #
    def _exit_application(self):
        '''Terminates the application by setting the sentinal'''
        self._stop_application = True
        print(STexts.application_terminated)
    
