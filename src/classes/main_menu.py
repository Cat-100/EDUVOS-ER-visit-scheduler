from utils.enums.enums import MainMenuOption
from classes.scheduler import Scheduler


class MainMenu(object):
    ''' 
    Object class that represents the main menu of the ER application. 
    
    Contains the scheduler, business and GUI logic to allow the user to:
    - Add patients to the Scheduler
    - Retrieve Patients in the queue. Consult them after being retrieved
    - Display all patients in the waiting queue
    - Read a Patient Consultation File
    - Exit the application
    
    **Properties:**
    - `stop_application`: Sentinal value that stops the application when its value becomes `True`
    - `scheduler`: The [Scheduler] object that manages the priority queue of patients.
    '''

    # --------------------------- Functions ----------------------------- #

    def __init__(self) -> None:
        '''Constructor for the class'''
        self.stop_application = False 
        self.scheduler = Scheduler()

    def start(self):
        '''Starts the application, running the main menu until the user exists the application.'''
        # Continue displaying, running the application, until terminate or stop application is selected
        while self.stop_application == False:
            # Display menu
            self._display_main_menu()

            # Get User Choice
            menu_option_made : MainMenuOption = self._get_user_menu_choice() 

            # Handle the user choice made
            self._handle_menu_option_selected(menu_option_made)

    def _display_main_menu(self) -> None:
        '''Prints the main menu for the user to use and select a option'''
        print("Clinic ER visit scheduler")
        print("------------------------------------------")
        print("(1) Add Patient to Schedule.")
        print("(2) Retrieve Next Patient.")
        print("(4) Display All Patients Waiting.")
        print("(5) Read Patient Consultation File")
        print("(6) Exit application")
        print()

    def _get_user_menu_choice(self) -> MainMenuOption:
        menu_choice : MainMenuOption = None
        while menu_choice == None:
            menu_choice_str =  input("Please selected an option from the menu: ")
            
            try:
                # Attempt to convert input to an int and get the correct Menu Option
                menu_choice = int(menu_choice_str)
                # Convert int choice to enum value
                menu_choice = MainMenuOption.from_int(menu_choice)

                # Handle edge case where the value is not in the range of the options provided
                if menu_choice is None:
                    raise ValueError
                
                # Valid choice, return
                return menu_choice

            except ValueError:
                # Handle case where the user provided a input that was not valid
                print("Invalid Input. Please select an option from the menu as a number.\nEx. 1")

    def _handle_menu_option_selected(self, menu_option: MainMenuOption) -> None:
        '''Invokes certain process based on the Main Menu Option provided'''
        match menu_option:
            case MainMenuOption.ADD_PATIENT_TO_SCHEDULE:
                pass
            case MainMenuOption.RETRIEVE_NEXT_PATIENT:
                pass
            case MainMenuOption.DISPLAY_ALL_PAIENTS_WAITING:
                pass
            case MainMenuOption.READ_PATIENT_CONSULTATION_FILE:
                pass
            case MainMenuOption.EXIT_APPLICATION:
                self._exit_application()
          
    # =========================== Main Menu Option Functions ============================== #
    def _exit_application(self):
        '''Terminates the application by setting the sentinal'''
        self.stop_application = True
        print("Application successfully terminated")
