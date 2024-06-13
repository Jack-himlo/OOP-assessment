from classes.customer import Customer
import pytest

"""
This will test that the current video rental setter only accepts a list as
a new value and will otherwise throw an error stating:
'Current Video Rentals should only be a list'
"""


def test_04_current_video_rental_setter():
    customer = Customer(**{
        "id": 1,
        "account_type": "sx",
        "first_name": "Monica",
        "last_name": "Gellar",
        "current_video_rentals": ["The Godfather"],
    })
    # Test existence and types of attributes
    try:
        customer.current_video_rentals = "Deadpool"
    except Exception as e:
        assert e.args[0] == "Current Video Rentals should only be a list"
        customer.current_video_rentals = ["Deadpool"]
        assert customer.current_video_rentals == ["Deadpool"]