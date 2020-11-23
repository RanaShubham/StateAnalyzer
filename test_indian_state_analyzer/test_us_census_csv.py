from Indian_state_analyzer.main_indian_state_analyzer.csv_us_census import USCensusCsvHandler

def test_get_list_sorted_by_state_should_return_list_sorted_by_state_name_in_ascending_order():
    sorted_object_list = USCensusCsvHandler.get_list_sorted_by_state()
    assert  sorted_object_list[0].State < sorted_object_list[-1].State

def test_get_list_sorted_by_state_code_should_return_list_sorted_by_state_Id_in_ascending_order():
    sorted_object_list = USCensusCsvHandler.get_list_sorted_by_state_code()
    assert sorted_object_list[0].State_Id < sorted_object_list[-1].State_Id

def test_get_list_sorted_by_state_housing_density_should_return_list_sorted_by_state_housing_density_in_descending_order():
    sorted_object_list = USCensusCsvHandler.get_list_sorted_by_state_housing_density()
    assert float(sorted_object_list[0].Housing_Density) > float(sorted_object_list[-1].Housing_Density)

def test_get_list_sorted_by_state_population_density_should_return_list_sorted_by_population_density_in_descending_order():
    sorted_object_list = USCensusCsvHandler.get_list_sorted_by_state_population_density()
    assert float(sorted_object_list[0].Population_Density) > float(sorted_object_list[-1].Population_Density)

def test_get_list_sorted_by_state_size_should_return_list_sorted_by_land_area_in_descending_order():
    sorted_object_list = USCensusCsvHandler.get_list_sorted_by_state_size()
    assert float(sorted_object_list[0].Land_area) > float(sorted_object_list[-1].Land_area)