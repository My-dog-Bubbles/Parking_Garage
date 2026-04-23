def enter_garage(garage, car_id, entry_hour):
    if len(garage["cars"]) >= garage["capacity"]:
        raise ValueError("TOO many cars")
    if not isinstance(entry_hour, int):
        raise TypeError("Not corrrect input")
    raise ValueError

def exit_garage(garage, car_id):
    pass

def get_available_spots(garage):
    pass

def calculate_fee(hours, rate):
    if not isinstance(hours, (int, float)) or not isinstance(rate, (int, float)):
        raise TypeError("hours or rate must be int or float")
    if hours <= 0 or rate <= 0:
        raise ValueError("hour and rate must be over 0")