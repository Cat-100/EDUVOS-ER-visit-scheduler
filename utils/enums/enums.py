from enum import Enum, auto


class FileOperation(Enum):
    ''' 
    Denotes file operations when opening files

    - Write: Opens a file for writing, will create the file if it does not exist.
    - Read: Opens a file for ReadOnluy, allow for reading of a file but not editing the file.
    '''

    # Values
    WRITE = "w"
    READ = "r"
    APPEND = "a"
    
class FileOperationalStatus(Enum):
    ''''
    File Status that indicates whether a file operation was:
    - Successful 
    - Failed
    - Stopped
    '''
    # Values
    SUCCESS = auto()
    FAILED = auto()
    STOPPED = auto()



