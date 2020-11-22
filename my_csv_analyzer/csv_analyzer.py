import csv
import re
from Indian_state_analyzer.my_csv_analyzer.csv_pojo import PojoCsv
from Indian_state_analyzer.my_csv_analyzer.csv_reader_exception import CsvReaderException, ExceptionType
from  typing import Type

class CsvAnalyzer:

    @staticmethod
    def read_csv_data(my_file_path, pojo_class: Type[PojoCsv]):
        '''
                Reads StateCodeCsv file and returns number of records in the file.

                :param pojo_class: Pojo class whose objects hold the data from each row of csv file.
                :type pojo_class:
                :param my_file_path: Path of the csv file.
                :type my_file_path: str
                :return: List of objects of pojo class.
                :rtype: list
        '''
        if not my_file_path.endswith(".csv"):
            raise CsvReaderException(CsvReaderException, ExceptionType.IncorrectFileTypeException)
        try:
            with open(my_file_path, "r") as my_file:
                if not re.search('[,]', my_file.readline()):
                    raise CsvReaderException(CsvReaderException, ExceptionType.IncorrectDelimiterException)
                my_file.seek(0)
                reader = csv.DictReader(my_file)
                pojo_object_list = list(map(lambda row: pojo_class(row), reader))
                if not pojo_object_list[0].compatible_with_file():
                    raise CsvReaderException(CsvReaderException, ExceptionType.InvalidCsvHeadersException)
                return pojo_object_list
        except FileNotFoundError:
            raise CsvReaderException(FileNotFoundError, ExceptionType.NoSuchFileException)
        except CsvReaderException as error_type:
            raise CsvReaderException(error_type.type, error_type.message)
        except TypeError:
            raise CsvReaderException(TypeError, ExceptionType.InvalidPojoClassException)
        except Exception as something_wrong:
            print(something_wrong)

def driver_function():
    pass
if __name__ == "__main__":
    driver_function()