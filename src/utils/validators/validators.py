from utils.helpers.helper_functions import SHelperFunctions
import re

class SValidators:
    '''Utility class that has all the validators of the application'''

    @staticmethod
    def is_digits_only(value: str) -> bool:
        '''
        Determines if a value only contains digits
        
        **Parameters:**
        - `value`: The [str] passed to check if the value only contains digits

        **Returns:**
        - [bool] to indicate if the `value` is only digits
        - `True` indicates that the `value` is only digits
        - `False` indicates that the `value` is not only digits
        '''
        
        pattern = "^\d+$"
        return bool(re.match(pattern, value))
    
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
        
        # Check if the id is only digits
        if not SValidators.is_digits_only(id_number):
            return "Invalid ID Number. Enter an ID number of only digits, not characters"
        
        # Check if the id has a valid length
        if len(id_number) != 13:
            return "Invalid ID number. Enter an ID of 13 digits"
    
        # Check birthday as last check
        
        # Get month
        month : int = int(id_number[2:4])
        # Check month validity
        if not (1 <= month <= 12):
            return "Invalid ID Number. Month should be between 01 and 12."
        
        # Get day
        day : str = int(id_number[4:6])
        # Check day validity
        if not (1 <= day <= 31):
            return "Invalid ID Number. Day should be between 01 and 31"

        # Valid ID, continue
        return None
