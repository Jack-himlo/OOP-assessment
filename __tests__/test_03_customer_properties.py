from classes.customer import Customer
import pytest

"""
This test will ensure all properties within the Customer class are created
"""


def test_03_customer_properties():
    customer = Customer(**{
        "id": 1,
        "account_type": "sx",
        "first_name": "Monica",
        "last_name": "Gellar",
        "current_video_rentals": ["The Godfather"],
    })
    # Test existence and types of attributes
    assert hasattr(customer, "id")
    assert isinstance(customer.id, int)
    
    assert hasattr(customer, "current_video_rentals")
    assert isinstance(customer.current_video_rentals, list)
