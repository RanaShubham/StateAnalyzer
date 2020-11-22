import pytest

from Indian_state_analyzer.main_indian_state_analyzer.csv_reader_exception import CsvReaderException, ExceptionType
from Indian_state_analyzer.main_indian_state_analyzer.state_analyzer import StateAnalyzer

state_census_data_file = "../resources/IndiaStateCensusData.csv"
state_code_data_file = "../resources/IndiaStateCode.csv"
us_census_data = "../resources/USCensusData.csv"
wrong_delimiter_file = "../resources/WrongDelimiter.csv"
wrong_type_file = "../resources/WrongType.txt"
absent_file = "../resources/nofile.csv"

def test_read_csv_data_should_return_number_of_records_in_file():
    assert StateAnalyzer.read_csv_data(state_census_data_file) == 29

@pytest.mark.parametrize(
    'my_file, error_message', [
        (wrong_delimiter_file, ExceptionType.IncorrectDelimiterException),
        (wrong_type_file, ExceptionType.IncorrectFileTypeException),
        (state_code_data_file, ExceptionType.IncorrectCsvHeaderException),
        (us_census_data, ExceptionType.IncorrectCsvHeaderException),
        (absent_file, ExceptionType.IncorrectFilePathException)
    ]
)
def test_read_csv_data_should_return_number_of_records_in_file(my_file, error_message):
    with pytest.raises(CsvReaderException) as csv_error:
        StateAnalyzer.read_csv_data(my_file)
    assert csv_error.value.message == error_message