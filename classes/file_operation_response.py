from utils.enums.enums import FileOperationalStatus

class FileOperationResponse(object):
    ''' Utility class object that represents a message and a status to indicate the overall status of a file operation'''

    def __init__(self, status: FileOperationalStatus , message: str ) -> None:
        self.status = status
        self.message = message