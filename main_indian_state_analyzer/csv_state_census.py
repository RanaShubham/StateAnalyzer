import json

from Indian_state_analyzer.my_csv_analyzer.csv_pojo import PojoCsv
from Indian_state_analyzer.my_csv_analyzer.csv_analyzer import CsvAnalyzer

class StateCensusCsv(PojoCsv):

    MY_FILE = "../resources/IndiaStateCensusData.csv"
    SORTED_STATE = "./SortedByState.json"

    def __init__(self, ordered_dict):
        self.State = ordered_dict.get("State")
        self.Population = ordered_dict.get("Population")
        self.AreaInSqKm = ordered_dict.get("AreaInSqKm")
        self.DensityPerSqKm = ordered_dict.get("DensityPerSqKm")

    def display(self):
        '''
            Prints the object data.
            :return: None
            :rtype: None
         '''
        print('State:{}, Population:{}, AreaInSqKm:{}, DensityPerSqKm:{}'.format(
            self.State,
            self.Population,
            self.AreaInSqKm,
            self.DensityPerSqKm
        ))

    def compatible_with_file(self):
        '''
           Returns True if all instance variables of this object are not None. Otherwise returns False.

           :return: Returns True if all instance variables of this object are not None. Otherwise returns False.
           :rtype: bool
        '''
        return  self.State and self.Population and self.AreaInSqKm and self.DensityPerSqKm

    @staticmethod
    def get_object_list():
        '''
            To get object data in list form from the csv file using CsvAnalyzer module.
            :return: List of objects of this type.
            :rtype: list
        '''
        return CsvAnalyzer.read_csv_data(StateCensusCsv.MY_FILE, StateCensusCsv)

    @staticmethod
    def get_list_sorted_by_state():
        '''
            Sorts the list of  objects of this type according to state in ascending order.
            :return: Sorted object list
            :rtype: list
        '''
        my_list = StateCensusCsv.get_object_list()
        my_list.sort(key = lambda state : state.State)
        save_sorted_to_json(my_list)

def save_sorted_to_json(my_list):
    '''
        Writes the list of objects of this type in json file.
        :param my_list: List of objects of this type.
        :type my_list:  list
        :return: None
        :rtype: None
    '''
    with open(StateCensusCsv.SORTED_STATE, "w") as file:
        for each in my_list:
            file.write(json.dumps(each.__dict__, indent=4))

def driver_function():
    StateCensusCsv.get_list_sorted_by_state()

if __name__ == "__main__":
    driver_function()