import  enum
class ExceptionType(enum.Enum):
    IncorrectDelimiterException = "CSV File format incorrect.."
    IncorrectFileTypeException = "File type unrecognized."
    InvalidCsvHeadersException = "File headers unrecognized or pojo class incompatible."
    NoSuchFileException = "File path incorrect."
    InvalidPojoClassException = "Required pojo class not available."
    UnitMismatchException = "Can't do conversion between unrelated unit type."
    UnrecognizedUnitException = "Unit type unrecognized"
    InvalidUnitDataException = "Data type for amount of this unit is invalid."
    InvalidTemperature = "Data type for temperature is invalid."
    MiscException = "Something went wrong while reading csv."

class CsvReaderException(Exception):
    def __init__(self, *args):
        self.type = args[0]
        self.message = args[1]

class UnitError(Exception):
    def __init__(self, *args):
        self.type = args[0]
        self.message = args[1]