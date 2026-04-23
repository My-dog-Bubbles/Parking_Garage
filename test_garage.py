import pytest
from garage import calculate_fee

# def test_enter_garage_car_to_long(garage):
#     garage["cars"] = {"ca","cb", "cc", "cd", "ce","cf", "cg","vksjd","nknjd","kjsdn","ksdnlsnd"}
#     with pytest.raises(ValueError):
#         enter_garage(garage, 5, "2pm")

# def test_enter_garage_car_to_long():
#     with pytest.raise(ValueError)
#         enter_garage(garage, 5, "2pm")

# def test_exit_garage_wrong_ID():
#     with pytest.raise(KeyError)
#         exit_garage(garage, 3)

def test_calculate_fee_hours_or_rate_neg():
    with pytest.raises(ValueError):
        calculate_fee(-2,2)