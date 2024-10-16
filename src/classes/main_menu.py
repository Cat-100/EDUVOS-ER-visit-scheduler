class MainMenu(object):
    ''' Object class that represents the main menu of the ER application'''

    # --------------------------- Functions ----------------------------- #

    def __init__(self) -> None:
        '''Constructor for the class'''
        self.stop_application = False # Sentinal variable to manage when to stop the main menu from continuing.


    def display_main_menu() -> None:
        '''Prints the main menu for the user to use and select a option'''
        print("(1) Add Patient to Schedule.")
        print("(2) Retrieve Next Patient.")
        print("(3) Display All Patients Waiting.")
        print("(4) Read Patient Consultation File")
        print("(5) Exit application")
