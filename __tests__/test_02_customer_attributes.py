from classes.customer import Customer
import pytest

"""
This test will ensure all attributes within the Customer class are created
"""


def test_02_customer_attributes():
    customer = Customer(**{
        "id": 1,
        "account_type": "sx",
        "first_name": "Monica",
        "last_name": "Gellar",
        "current_video_rentals": ["The Godfather"],
    })
    # Test existence and types of attributes
    assert hasattr(customer, "_id")

    assert hasattr(customer, "first_name")

    assert hasattr(customer, "last_name")

    assert hasattr(customer, "_account_type")

    assert hasattr(customer, "_current_video_rentals")
