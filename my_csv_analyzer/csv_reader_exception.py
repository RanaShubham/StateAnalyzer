import  enum
class ExceptionType(enum.Enum):
    IncorrectDelimiterException = "CSV File format incorrect.."
    IncorrectFileTypeException = "File type unrecognized."
    InvalidCsvHeadersException = "File headers unrecognized or pojo class incompatible."
    NoSuchFileException = "File path incorrect."
    InvalidPojoClassException = "Required pojo class not available."
    MiscException = "Something went wrong while reading csv."

class CsvReaderException(Exception):
    def __init__(self, *args):
        self.type = args[0]
        self.message = args[1]