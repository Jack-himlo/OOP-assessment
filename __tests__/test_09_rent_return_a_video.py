from classes.customer import Customer
import pytest

"""
- ensures instance methods of rent_a_video and return_a_video existing within the program
- ensures the return_a_video method works as intended
"""


def test_09_rent_return_a_video():
    customer = Customer(**{
        "id": 1,
        "account_type": "sx",
        "first_name": "Monica",
        "last_name": "Gellar",
        "current_video_rentals": ["The Godfather"],
    })
    assert hasattr(Customer, 'return_a_video')
    assert hasattr(Customer, 'rent_a_video')
    try:
        customer.return_a_video("Deadpool")
    except Exception as e:
        customer.return_a_video('The Godfather')
        assert customer.current_video_rentals == []