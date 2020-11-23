import pytest
import  logging

from Indian_state_analyzer.my_csv_analyzer.csv_reader_exception import CsvReaderException, ExceptionType
from Indian_state_analyzer.main_indian_state_analyzer.csv_state_census import StateCensusCsvHandler
from Indian_state_analyzer.main_indian_state_analyzer.csv_state_code import StateCodeCsvHandler
from Indian_state_analyzer.my_csv_analyzer.csv_analyzer import CsvAnalyzer
from Indian_state_analyzer.main_indian_state_analyzer.csv_us_census import USCensusCsvHandler

state_census_data_file = "../resources/IndiaStateCensusData.csv"
state_code_data_file = "../resources/IndiaStateCode.csv"
us_census_data = "../resources/USCensusData.csv"
wrong_delimiter_file = "../resources/WrongDelimiter.csv"
wrong_type_file = "../resources/WrongType.txt"
absent_file = "../resources/nofile.csv"

@pytest.mark.parametrize(
    'my_file, pojo_class,number_of_records', [
        (us_census_data, USCensusCsvHandler, 51),
        (state_code_data_file, StateCodeCsvHandler, 37),
        (state_census_data_file, StateCensusCsvHandler, 29)
    ]
)
def test_read_csv_data_should_return_number_of_records_in_file(my_file, pojo_class, number_of_records):
    logging.debug("{} has {} records".format(my_file, number_of_records))
    assert CsvAnalyzer.read_csv_data(my_file, pojo_class).__len__() == number_of_records

@pytest.mark.parametrize(
    'my_file, pojo_class, error_message', [
        (wrong_delimiter_file, StateCodeCsvHandler, ExceptionType.IncorrectDelimiterException),
        (wrong_type_file, StateCodeCsvHandler, ExceptionType.IncorrectFileTypeException),
        (state_census_data_file, StateCodeCsvHandler, ExceptionType.InvalidCsvHeadersException),
        (us_census_data, StateCodeCsvHandler, ExceptionType.InvalidCsvHeadersException),
        (absent_file, StateCodeCsvHandler, ExceptionType.NoSuchFileException),
        (us_census_data,    "str",     ExceptionType.InvalidPojoClassException)
    ]
)
def test_read_csv_data_when_given_inappropriate_file_should_raise_CsvReaderException(my_file, pojo_class, error_message):
    with pytest.raises(CsvReaderException) as csv_error:
        CsvAnalyzer.read_csv_data(my_file, pojo_class)
        logging.debug("Pojo_Class:{}, File:{}, error_messages:{}".format(pojo_class, my_file, error_message))
    assert csv_error.value.message == error_message