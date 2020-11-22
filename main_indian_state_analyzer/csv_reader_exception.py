import  enum
class ExceptionType(enum.Enum):
    IncorrectDelimiterException = "CSV File format incorrect.."
    IncorrectFileTypeException = "File type unrecognized."
    IncorrectCsvHeaderException = "File headers unrecognized."
    IncorrectFilePathException = "File path incorrect."

class CsvReaderException(Exception):
    def __init__(self, *args):
        self.type = args[0]
        self.message = args[1]