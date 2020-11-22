class StateCensusCsv:

    def __init__(self, ordered_dict):
        self.State = ordered_dict.get("State")
        self.Population = ordered_dict.get("Population")
        self.AreaInSqKm = ordered_dict.get("AreaInSqKm")
        self.DensityPerSqKm = ordered_dict.get("DensityPerSqKm")

    def display(self):
        print('State:{}, Population:{}, AreaInSqKm:{}, DensityPerSqKm:{}'.format(
            self.State,
            self.Population,
            self.AreaInSqKm,
            self.DensityPerSqKm
        ))

    def compatible_with_file(self):
            return  self.State and self.Population and self.AreaInSqKm and self.DensityPerSqKm