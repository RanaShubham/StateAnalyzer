import json
import logging

from Indian_state_analyzer.my_csv_analyzer.csv_analyzer import CsvAnalyzer
from Indian_state_analyzer.my_csv_analyzer.csv_pojo import CsvHandler

logging.basicConfig(filename='./USCensusTest.log', level=logging.DEBUG,
                    format='%(asctime)s | %(levelname)s | %(message)s')

class USCensusCsvHandler(CsvHandler):
    CSV_FILE_UNSORTED = "../resources/USCensusData.csv"
    JSON_FILE_BY_STATE = "../resources/UsCensusData_sortedByState.json"
    JSON_FILE_BY_STATE_CODE = "../resources/UsCensusData_sortedByStateCode.json"
    JSON_FILE_BY_MOST_HOUSING_DENSITY = "../resources/UsCensusData_sortedByMostHousingDensity.json"
    JSON_FILE_BY_MOST_POPULATION_DENSITY = "../resources/UsCensusData_sortedByMostPopulationDensity.json"
    JSON_FILE_BY_STATE_SIZE = "../resources/UsCensusData_sortedByStateSize.json"

    def __init__(self, ordered_dict):
        self.State_Id = ordered_dict.get("State Id")
        self.State = ordered_dict.get("State")
        self.Housing_units = ordered_dict.get("Housing units")
        self.Total_area = ordered_dict.get("Total area")
        self.Water_area = ordered_dict.get("Water area")
        self.Land_area = ordered_dict.get("Land area")
        self.Population_Density = ordered_dict.get("Population Density")
        self.Housing_Density = ordered_dict.get("Housing Density")

    def __repr__(self):
        return 'State_Id:{}, State:{}, Housing_units:{}, Total_area:{}, Water_area:{},' \
               ' Land_area:{}, Population_Density:{}, Housing_Density:{}\n'.format(
            self.State_Id,
            self.State,
            self.Housing_units,
            self.Total_area,
            self.Water_area,
            self.Land_area,
            self.Population_Density,
            self.Housing_Density)

    def display(self):
        '''
            Prints the object data.
            :return: None
            :rtype: None
        '''
        print('\nState_Id:{}, State:{}, Housing_units:{}, Total_area:{}, Water_area:{},'
              ' Land_area:{}, Population_Density:{}, Housing_Density:{}'.format(
            self.State_Id,
            self.State,
            self.Housing_units,
            self.Total_area,
            self.Water_area,
            self.Land_area,
            self.Population_Density,
            self.Housing_Density
        ))

    def compatible_with_file(self):
        '''
            Returns True if all instance variables of this object are not None. Otherwise returns False.

            :return: Returns True if all instance variables of this object are not None. Otherwise returns False.
            :rtype: bool
        '''
        return  self.State_Id and self.State and self.Housing_units and\
                self.Total_area and  self.Water_area and self.Land_area and self.Population_Density and self.Housing_Density


    @staticmethod
    def get_object_list_from_csv():
        '''
            To get object data in list form from the csv file using CsvAnalyzer module.
            :return: List of objects of this type.
            :rtype: list
        '''
        return CsvAnalyzer.read_csv_data(USCensusCsvHandler.CSV_FILE_UNSORTED, USCensusCsvHandler)

    @staticmethod
    def get_list_sorted_by_state():
        '''
            Sorts the list of  objects of this type according to state in ascending order and saves to json file.
            :return: Sorted object list
            :rtype: list
        '''
        my_list = USCensusCsvHandler.get_object_list_from_csv()
        my_list.sort(key=lambda state: state.State)
        save_sorted_to_json(my_list, USCensusCsvHandler.JSON_FILE_BY_STATE)
        logging.debug("-"*75+"STATE"+"-"*75)
        logging.debug(my_list)
        logging.debug("="*200)
        return my_list

    @staticmethod
    def get_list_sorted_by_state_code():
        '''
            Sorts the list of  objects of this type according to state code in ascending order and saves to json file.
            :return: Sorted object list
            :rtype: list
        '''
        my_list = USCensusCsvHandler.get_object_list_from_csv()
        my_list.sort(key=lambda state: state.State_Id)
        save_sorted_to_json(my_list, USCensusCsvHandler.JSON_FILE_BY_STATE_CODE)
        logging.debug("-"*75+"STATE-ID"+"-"*75)
        logging.debug(my_list)
        logging.debug("="*200)
        return my_list

    @staticmethod
    def get_list_sorted_by_state_housing_density():
        '''
            Sorts the list of  objects of this type according to housing density in descending order and saves to json file.
            :return: Sorted object list
            :rtype: list
        '''
        my_list = USCensusCsvHandler.get_object_list_from_csv()
        my_list.sort(key=lambda state: float(state.Housing_Density), reverse=True)
        save_sorted_to_json(my_list, USCensusCsvHandler.JSON_FILE_BY_MOST_HOUSING_DENSITY)
        logging.debug("-"*75+"HOUSING-DENSITY"+"-"*75)
        logging.debug(my_list)
        logging.debug("="*200)
        return my_list

    @staticmethod
    def get_list_sorted_by_state_population_density():
        '''
            Sorts the list of  objects of this type according to state population density in descending order and saves to json file.
            :return: Sorted object list
            :rtype: list
        '''
        my_list = USCensusCsvHandler.get_object_list_from_csv()
        my_list.sort(key=lambda state: float(state.Population_Density), reverse=True)
        save_sorted_to_json(my_list, USCensusCsvHandler.JSON_FILE_BY_MOST_POPULATION_DENSITY)
        logging.debug("-"*75+"POPULATION-DENSITY"+"-"*75)
        logging.debug(my_list)
        logging.debug("="*200)
        return my_list

    @staticmethod
    def get_list_sorted_by_state_size():
        '''
            Sorts the list of  objects of this type according to state size in descending order and saves to json file.
            :return: Sorted object list
            :rtype: list
        '''
        my_list = USCensusCsvHandler.get_object_list_from_csv()
        my_list.sort(key=lambda state: float(state.Land_area), reverse=True)
        save_sorted_to_json(my_list, USCensusCsvHandler.JSON_FILE_BY_STATE_SIZE)
        logging.debug("-"*75+"STATE-SIZE"+"-"*75)
        logging.debug(my_list)
        logging.debug("="*200)
        return my_list


def save_sorted_to_json(sorted_list, sorted_json):
    '''
        Writes the list of objects of this type in json file.
        :param sorted_list: List of objects of this type.
        :type:  list
        :return: None
        :rtype: None
    '''
    with open(sorted_json, "w") as file:
        for object in sorted_list:
            file.write(json.dumps(object.__dict__, indent=4))


def driver_function():
    USCensusCsvHandler.get_list_sorted_by_state()
    USCensusCsvHandler.get_list_sorted_by_state_code()
    USCensusCsvHandler.get_list_sorted_by_state_housing_density()
    USCensusCsvHandler.get_list_sorted_by_state_population_density()
    USCensusCsvHandler.get_list_sorted_by_state_size()

if __name__ == "__main__":
    driver_function()