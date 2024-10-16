from utils.enums.enums import FileOperationalStatus
from typing import Any
class FileOperationResponse(object):
    ''' 
    
    Utility class object that represents a message and a status to indicate the overall status of a file operation 
    
    **Properties:**
    - `status`: The [FileOperationalStatus] of the file operation. Indicates if the operation was successful, stopped, or failed.
    - `message`: The message that indicates additional context to the status of the file operation.
    - `payload`: The data returned from the file operation, such as reading from a file, if any is returned.
    '''

    def __init__(self, status: FileOperationalStatus , message: str  , payload : Any = None) -> None:
        self.status = status
        self.message = message
        self.payload = payload