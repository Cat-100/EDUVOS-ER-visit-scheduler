from utils.enums.enums import FileMode, FileOperationalStatus
from models.file_operation_response import FileOperationResponse
from typing import List
from pathlib import Path
import os

class FileOperations:
    ''' Service class that allows the application to perform file operations such as wiritng to files and or reading from files.'''

    # ----------------------------- Functions ------------------------------ #
    @staticmethod
    def write_to_file(fileName:str, lines: List[str] , overwriteFile : bool = False) -> FileOperationResponse:
        '''
        Write contents to a file specified
        
        **Parameters:**
        - `fileName`: The name of the file that should be written to.
        - `lines`: The content that should be written to the file.
        - `overwriteFile`: Optional, whether to overwrite the file contents or append the contents to the file 

        **Returns:**
        - A [FileOperationResponse] to indicate the status of the file operation of writing to a file
        '''
        try:
            # Create Path object
            file : Path = Path(fileName)

            # Get directory path
            fileDirectory : Path = file.parent 
            
            # Make sure the directory exists. Exists_ok to ensure that no error is thrown to allow the process to continue
            fileDirectory.mkdir(parents=True, exist_ok=True)

            # Deterime to use a file mode to append or overwrite the file
            fileMode : FileMode = FileMode.APPEND

            if overwriteFile == True:
                fileMode = FileMode.WRITE

            with file.open(fileMode.value, encoding="utf-8") as openedFile:
                for line in lines:
                    openedFile.write(f"{line}\n")

            return FileOperationResponse(FileOperationalStatus.SUCCESS , "Successfully wrote contents to file")
        except Exception as e:
            # Handle unexpected error
            return FileOperationResponse(FileOperationalStatus.FAILED , f"Unexpected Error: {e}"); 

    @staticmethod
    def read_from_txt_file(fileName : str) -> FileOperationResponse:
        '''
        Read and return the contents of a text file
        
        **Parameters:**
        - `fileName`: The entire file name of the file to be read.

        **Return:**
        - A [FileOperationResponse] is returned to indicate the status of the reading operatoin. 
        - A `payload` will be provided in the response status is `SUCCESS`.        
        '''
        try:
            # Create Path object
            file : Path = Path(fileName)

            # Make sure the file exists before reading the file
            if not file.exists():
                return FileOperationResponse(FileOperationalStatus.STOPPED , f"Cannot read from from {file.name}. File does not exists." )
        
            # File Exists, attempt to read the file
            with file.open(FileMode.READ.value , encoding="utf-8") as opendedFile :
                fileContents = opendedFile.read()
            
            # Return the contents of the file
            return FileOperationResponse(FileOperationalStatus.SUCCESS , f"Successfully read the file. {file.name}" , payload=fileContents)
        except Exception as e:
            # Handle unexpected error
            return FileOperationResponse(FileOperationalStatus.FAILED , f"Unexpected Error: {e}") 