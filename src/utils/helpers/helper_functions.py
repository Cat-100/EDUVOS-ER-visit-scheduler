from typing import List, Any
from datetime import date

class SHelperFunctions:
    '''Contains all helper functions for the application'''
    
    @staticmethod
    def swap_element_in_list(lst : List , original_index : int, swap_index: int  ) -> None:
        '''
        Swaps two elements in a list based on the indices provided
        
        **Parameters:**
        - `lst`: The list where the elements will be swapped.
        - `original_index`: The initial index that will be swapped with the swap element
        - `swap_index`: The swap index that will be swapped with the original element in the list.
        '''
        lst[original_index] , lst[swap_index] = lst[swap_index] , lst[original_index]

    @staticmethod
    def is_empty(value: Any) -> bool:
        '''
        Returns a bool to indicate if the `value` is empty or not. True for empty
        
        **Parameters:**
        - `value`: Any value which could be a list, string, or set Any variable
        
        **Returns:**
        - A bool to indicate if the value is empty.
        '''
        value_type : type = type(value) 
        
        if (value_type is List):
            return len(value) == 0
        
        match value_type:
            case str:
                return len(value) == 0 or value == ""

    @staticmethod       
    def get_current_date() -> str:
        ''' 
        Returns the calendar date in the form of yyyy-mm-dd without additional data such as time.
        
        **Returns**:
        - A formatted date string, in the format of yyyy-mm-dd
        '''
        return date.today().strftime('%Y-%m-%d')
            
            
