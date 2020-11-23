from Indian_state_analyzer.my_csv_analyzer.csv_pojo import PojoCsv

class StateCensusCsv(PojoCsv):

    MY_FILE = "../resources/IndiaStateCensusData.csv"
    FILE_SORTED_BY_SATE_CODED = "./SortedByStateCode.json"

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

