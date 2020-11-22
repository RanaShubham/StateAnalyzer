import csv
import re
from Indian_state_analyzer.main_indian_state_analyzer.csv_reader_exception import CsvReaderException, ExceptionType
from Indian_state_analyzer.main_indian_state_analyzer.csv_state_census import StateCensusCsv
from Indian_state_analyzer.main_indian_state_analyzer.csv_state_code import StateCodeCsv


class StateAnalyzer:
    indian_state_census_file = "../resources/IndiaStateCensusData.csv"
    indian_state_code_file = "../resources/IndiaStateCode.csv"

    @staticmethod
    def read_state_census_csv_data(my_file_path):
        '''
            Reads StateCensusCsv file and returns number of records in the file.

            :param my_file_path: Path of the csv file.
            :type my_file_path: str
            :return: Number of records in the file.
            :rtype: int
        '''
        if not my_file_path.endswith(".csv"):
            raise CsvReaderException(CsvReaderException, ExceptionType.IncorrectFileTypeException)
        try:
            with open (my_file_path, "r") as my_file:
                if not re.search('[,]', my_file.readline()):
                    raise CsvReaderException(CsvReaderException, ExceptionType.IncorrectDelimiterException)
                my_file.seek(0)
                reader = csv.DictReader(my_file)
                pojo_object_list = list(map(lambda row: StateCensusCsv(row), reader))
                if not pojo_object_list[0].compatible_with_file():
                    raise CsvReaderException(CsvReaderException, ExceptionType.IncorrectCsvHeaderException)
                return pojo_object_list.__len__()
        except FileNotFoundError:
            raise CsvReaderException(FileNotFoundError, ExceptionType.IncorrectFilePathException)
        except CsvReaderException as error_type:
            raise CsvReaderException(error_type.type, error_type.message)
        except Exception as something_wrong:
            print(something_wrong)

    @staticmethod
    def read_state_code_csv_data(my_file_path):
        '''
                Reads StateCodeCsv file and returns number of records in the file.

                :param my_file_path: Path of the csv file.
                :type my_file_path: str
                :return: Number of records in the file.
                :rtype: int
        '''
        if not my_file_path.endswith(".csv"):
            raise CsvReaderException(CsvReaderException, ExceptionType.IncorrectFileTypeException)
        try:
            with open(my_file_path, "r") as my_file:
                if not re.search('[,]', my_file.readline()):
                    raise CsvReaderException(CsvReaderException, ExceptionType.IncorrectDelimiterException)
                my_file.seek(0)
                reader = csv.DictReader(my_file)
                pojo_object_list = list(map(lambda row: StateCodeCsv(row), reader))
                if not pojo_object_list[0].compatible_with_file():
                    raise CsvReaderException(CsvReaderException, ExceptionType.IncorrectCsvHeaderException)
                return pojo_object_list.__len__()
        except FileNotFoundError:
            raise CsvReaderException(FileNotFoundError, ExceptionType.IncorrectFilePathException)
        except CsvReaderException as error_type:
            raise CsvReaderException(error_type.type, error_type.message)
        except Exception as something_wrong:
            print(something_wrong)

def driver_function():
    print(StateAnalyzer.read_state_census_csv_data(StateAnalyzer.indian_state_census_file))
    print(StateAnalyzer.read_state_code_csv_data(StateAnalyzer.indian_state_code_file))

if __name__ == "__main__":
    driver_function()