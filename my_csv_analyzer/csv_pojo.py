from abc import  *

class CsvHandler(ABC):
    '''
        Interface for all the pojo classes for csv files to implement.
    '''
    @abstractmethod
    def display(self):
        '''
            Display the data.
            :return: None
            :rtype: None
        '''
        pass

    @abstractmethod
    def compatible_with_file(self):
        '''
            Returns True if all instance variables of this object are not None. Otherwise returns False.

            :return: True or False
            :rtype: bool
        '''
        pass