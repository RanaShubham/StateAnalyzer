from Indian_state_analyzer.my_csv_analyzer.csv_pojo import PojoCsv

class USCensusCsv(PojoCsv):

    def __init__(self, ordered_dict):
        self.State_Id = ordered_dict.get("State Id")
        self.State = ordered_dict.get("State")
        self.Housing_units = ordered_dict.get("Housing units")
        self.Total_area = ordered_dict.get("Total area")
        self.Water_area = ordered_dict.get("Water area")
        self.Land_area = ordered_dict.get("Land area")
        self.Population_Density = ordered_dict.get("Population Density")
        self.Housing_Density = ordered_dict.get("Housing Density")

    def display(self):
        '''
            Prints the object data.
            :return: None
            :rtype: None
        '''
        print('State_Id:{}, State:{}, Housing_units:{}, Total_area:{}, Water_area:{}, Land_area:{}, Population_Density:{}, Housing_Density:{}'.format(
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