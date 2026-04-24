import pytest
from garage import calculate_fee, enter_garage, exit_garage, get_available_spots

def test_enter_garage_car_to_long(garage):
    with pytest.raises(ValueError):
        garage["cars"] = {"ca","cb", "cc", "cd", "ce","cf", "cg","vksjd","nknjd","kjsdn","ksdnlsnd"}
        enter_garage(garage, 5, "2pm")

def test_enter_garage_car_already_in(garage):
    with pytest.raises(ValueError):
        enter_garage(garage,12,2)
        enter_garage(garage,12,3)

def test_enter_garage_invalid_hour(garage):
    with pytest.raises(TypeError):
        enter_garage(garage,12,"2")

def test_exit_garage_wrong_ID(garage):
    with pytest.raises(KeyError):
        exit_garage(garage, 3)

def test_calculate_fee_hours_or_rate_neg():
    with pytest.raises(ValueError):
        calculate_fee(-2,2)

def test_calculate_fee_invalid_input():
    with pytest.raises(TypeError):
        calculate_fee(2," ")       

def test_get_available_spots(garage):
    assert 0

@pytest.mark.parametrize("hours, rate, expected", [(2, 2, 4), (6, 5, 30), (1, 2, 2)])
def test_calculate_fee(hours, rate, expected):
    assert calculate_fee(hours, rate) == expected
