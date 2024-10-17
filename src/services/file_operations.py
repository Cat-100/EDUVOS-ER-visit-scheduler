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
            print(f"Debugging:\n{lines[0]}")
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
        - A `payload` will be provided if the response status is `SUCCESS`.        
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
    
    @staticmethod
    def are_directory_paths_equal(rootDirectory : Path , filePath  : Path ) -> bool:
        '''
        Utility function that checks whether two directory paths are the same
        Will take the parent of the file path so do not provide the directory path of the file.

        **Parameters:**
        - `rootDirectory`: The directory path that will be compared with the file path's directory path
        - `filePath`: The entire file path of the file. Will be deconstructed to its directory to check if its equal

        **Return:**
        - A boolean to indicate if the directory paths are equal or not.
        - True indicates that they are equal
        - False indicates that they are not equal 
        '''
        # Get File directory path
        fileDirectoryPath : Path = filePath.parent

        return rootDirectory == fileDirectoryPath
    
    @staticmethod
    def get_files_in_directory(directory : Path) -> FileOperationResponse:
        ''' 
        Returns all files in a directory
        
        **Parameters:**
        - `directory`: The Path that will be used to iterate the files in the directory.

        **Returns:**
        - `FileOperationalResponse` to indicate if the operation was successful or correct.
        - `SUCCESS` will have a payload of List[File]
        '''
        try:
            print(directory.is_dir())
            # Check if the directory is a directory before proceeding
            if not directory.is_dir():
                return FileOperationResponse(FileOperationalStatus.STOPPED , message=f"{directory.name} is not a directory.")
            
            # Create empty list of files to store
            files = []

            # iterate through the directory
            for file in directory.iterdir():
                if file.is_file():
                    files.append(file)
            
            print(files)
            # Return the files
            return files
        except Exception as e:
            return FileOperationResponse(FileOperationalStatus.FAILED , message=f"Unexpected error: {e}")
        