from classes.customer import Customer
import pytest

"""
- ensures this instance methods returns the instance current video rentals
"""


def test_08_get_customer_videos():
    customer = Customer(**{
        "id": 1,
        "account_type": "sx",
        "first_name": "Monica",
        "last_name": "Gellar",
        "current_video_rentals": ["The Godfather"],
    })
    assert customer.get_customer_rented_videos() == "Monica has the following rentals:\n['The Godfather']"