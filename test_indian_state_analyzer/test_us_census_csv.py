from Indian_state_analyzer.main_indian_state_analyzer.csv_us_census import USCensusCsv

def test_get_list_sorted_by_state_should_return_list_sorted_by_state_name_in_ascending_order():
    my_list = USCensusCsv.get_list_sorted_by_state()
    for each in my_list:
        if (each != my_list[0]):
            assert each.State > my_list[0].State

def test_get_list_sorted_by_state_code_should_return_list_sorted_by_state_name_in_ascending_order():
    my_list = USCensusCsv.get_list_sorted_by_state_code()
    for each in my_list:
        if (each != my_list[0]):
            assert each.State_Id > my_list[0].State_Id

def test_get_list_sorted_by_state_housing_density_should_return_list_sorted_by_state_name_in_descending_order():
    my_list = USCensusCsv.get_list_sorted_by_state_housing_density()
    for each in my_list:
        if (each != my_list[0]):
            assert float(each.Housing_Density) < float(my_list[0].Housing_Density)

def test_get_list_sorted_by_state_population_density_should_return_list_sorted_by_state_name_in_descending_order():
    my_list = USCensusCsv.get_list_sorted_by_state_population_density()
    for each in my_list:
        if (each != my_list[0]):
            assert float(each.Population_Density) < float(my_list[0].Population_Density)

def test_get_list_sorted_by_state_size_should_return_list_sorted_by_state_name_in_descending_order():
    my_list = USCensusCsv.get_list_sorted_by_state_size()
    for each in my_list:
        if (each != my_list[0]):
            assert float(each.Land_area) < float(my_list[0].Land_area)