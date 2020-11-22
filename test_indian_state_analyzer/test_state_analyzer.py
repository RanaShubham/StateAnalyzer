import pytest

from Indian_state_analyzer.my_csv_analyzer.csv_reader_exception import CsvReaderException, ExceptionType
from Indian_state_analyzer.main_indian_state_analyzer.csv_state_census import StateCensusCsv
from Indian_state_analyzer.main_indian_state_analyzer.csv_state_code import StateCodeCsv
from Indian_state_analyzer.my_csv_analyzer.csv_analyzer import CsvAnalyzer
from Indian_state_analyzer.main_indian_state_analyzer.csv_us_census import USCensusCsv

state_census_data_file = "../resources/IndiaStateCensusData.csv"
state_code_data_file = "../resources/IndiaStateCode.csv"
us_census_data = "../resources/USCensusData.csv"
wrong_delimiter_file = "../resources/WrongDelimiter.csv"
wrong_type_file = "../resources/WrongType.txt"
absent_file = "../resources/nofile.csv"

@pytest.mark.parametrize(
    'my_file, pojo_class,number_of_records', [
        (us_census_data, USCensusCsv, 51),
        (state_code_data_file, StateCodeCsv, 37),
        (state_census_data_file, StateCensusCsv, 29)
    ]
)
def test_read_csv_data_should_return_number_of_records_in_file(my_file, pojo_class, number_of_records):
    assert CsvAnalyzer.read_csv_data(my_file, pojo_class).__len__() == number_of_records

@pytest.mark.parametrize(
    'my_file, pojo_class, error_message', [
        (wrong_delimiter_file,   StateCodeCsv,    ExceptionType.IncorrectDelimiterException),
        (wrong_type_file,   StateCodeCsv,   ExceptionType.IncorrectFileTypeException),
        (state_census_data_file,    StateCodeCsv,   ExceptionType.InvalidCsvHeadersException),
        (us_census_data,     StateCodeCsv,   ExceptionType.InvalidCsvHeadersException),
        (absent_file,   StateCodeCsv,    ExceptionType.NoSuchFileException),
        (us_census_data,    "str",     ExceptionType.InvalidPojoClassException)
    ]
)
def test_read_csv_data_when_given_inappropriate_file_should_raise_CsvReaderException(my_file, pojo_class, error_message):
    with pytest.raises(CsvReaderException) as csv_error:
        CsvAnalyzer.read_csv_data(my_file, pojo_class)
    assert csv_error.value.message == error_message