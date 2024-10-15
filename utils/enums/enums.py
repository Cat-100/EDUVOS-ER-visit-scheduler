from enum import Enum, auto


class FileOperation(Enum):
    ''' 
    Denotes file operations when opening files

    - `Write:` Opens a file for writing, will create the file if it does not exist.
    - `Read:` Opens a file for Read-only, allow for reading of a file but not editing the file.
    '''
    # Values
    WRITE = "w"
    READ = "r"
    APPEND = "a"
    
class FileOperationalStatus(Enum):
    ''''
    File Status that indicates whether a file operation was:
    - `Successful:` The file operation was successfull. It ran to completion and accomplished it goal.  
    - `Failed:` The file operation failed, the operation did not run to completion as an exception was thrown.
    - `Stopped:` The file operation was stopped, this could be due to that the file was already overwritten or that a directory does not need to be recreated.
    '''
    # Values
    SUCCESS = auto()
    FAILED = auto()
    STOPPED = auto()



