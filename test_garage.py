from garage import exit_garage

def test_enter_garage_car_to_long(garage):
    garage["cars"] = {"ca","cb", "cc", "cd", "ce","cf", "cg","vksjd","nknjd","kjsdn","ksdnlsnd"}
    with pytest.raises(ValueError):
        enter_garage(garage, 5, "2pm")

