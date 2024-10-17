from utils.helpers.helper_functions import SHelperFunctions

class SValidators:
    '''Utility class that has all the validators of the application'''

    @staticmethod
    def validate_id_number(id_number : str) -> str:
        '''
        Validates whether the `id_number` is a valid id number
        
        **Parameters:**
        - `id_number`: The id number provided that will be validated

        **Returns:**
        - A [str] to indicate whether the id is validate
        - `None` means its correct
        - Not `None` means that the id number is not correct
        '''

        # Check if the id is empty
        if SHelperFunctions.is_empty(id_number):
            return "ID number is required. Enter an ID number"
        
        # Check if the id has a valid length
        if len(id_number) != 13:
            return "Invalid ID number. Enter an ID of 13 digits"
        
        # Check birthday as last check
        
        # Get month
        month : int = int(id_number[2:3])
        # Check month validity
        if not (1 <= month <= 12):
            return "Invalid ID Number. Month should be between 01 and 12."
        
        # Get day
        day : str = int(id_number[4:5])
        # Check day validity
        if not (1 <= day <= 31):
            return "Invalid ID Number. Day should be between 01 and 31"


