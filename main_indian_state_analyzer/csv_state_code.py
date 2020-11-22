from Indian_state_analyzer.my_csv_analyzer.csv_pojo import PojoCsv

class StateCodeCsv(PojoCsv):

    def __init__(self, ordered_dict):
        self.SrNo = ordered_dict.get("SrNo")
        self.State_Name = ordered_dict.get("State Name")
        self.TIN = ordered_dict.get("TIN")
        self.StateCode = ordered_dict.get("StateCode")

    def display(self):
        '''
            Prints the object data.
            :return: None
            :rtype: None
        '''
        print('SrNo:{}, State_Name:{}, TIN:{}, StateCode:{}'.format(
            self.SrNo,
            self.State_Name,
            self.TIN,
            self.StateCode
        ))

    def compatible_with_file(self):
        '''
            Returns True if all instance variables of this object are not None. Otherwise returns False.

            :return: Returns True if all instance variables of this object are not None. Otherwise returns False.
            :rtype: bool
        '''
        return  self.SrNo and self.State_Name and self.TIN and self.StateCode