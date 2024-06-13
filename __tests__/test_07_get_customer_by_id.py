from classes.customer import Customer
import pytest

"""
- ensures get_customer_by_id method can accept improper and proper input without raising an error

- ensures the method returns the correct customer
"""


def test_07_get_customer_by_id(monkeypatch):
    customer = Customer(**{
        "id": 1,
        "account_type": "sx",
        "first_name": "Monica",
        "last_name": "Gellar",
        "current_video_rentals": ["The Godfather"],
    })
    choices = ['aurednfa','1']
    input_val = iter(choices)
    Customer.add_a_customer(customer)
    monkeypatch.setattr('builtins.input', lambda _:next(input_val))
    assert Customer.get_customer_by_id() == customer