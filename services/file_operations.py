from utils.enums.enums import FileMode, FileOperationalStatus
from models.file_operation_response import FileOperationResponse
from typing import List
from pathlib import Path
import os

class FileOperations:
    ''' Service class that allows the application to perform file operations such as wiritng to files and or reading from files.'''

    # ----------------------------- Functions ------------------------------ #
    @staticmethod
    def write_to_file(fileName:str, lines: List[str]) -> FileOperationResponse:
        '''
        Write contents to a file specified
        
        **Parameters:**
        - `fileName`: The name of the file that should be written to.
        - `lines`: The content that should be written to the file.
        '''
        try:
            # Create Path object
            file : Path = Path(fileName)

            # Get directory path
            fileDirectory : Path = file.parent 
            
            # Make sure the directory exists. Exists_ok to ensure that no error is thrown to allow the process to continue
            fileDirectory.mkdir(parents=True, exist_ok=True)

            # Make sure the file exists
            with file.open(FileMode.WRITE.value, encoding="utf-8") as openedFile:
                for line in lines:
                    openedFile.write(f"{line}\n")

            return FileOperationResponse(FileOperationalStatus.SUCCESS , "Successfully wrote contents to file")
        except Exception as e:
            # Handle unexpected error
            return FileOperationResponse(FileOperationalStatus.FAILED , f"Unexpected Error: {e}"); 

   # @staticmethod
    #def read_from_file(fileName : str) -> 