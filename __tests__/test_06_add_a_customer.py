from classes.customer import Customer
import pytest

"""
Test will ensure the add_customer_method only accepts a customer instance and will 
throw an error if a different argument is provided.
Additionally this function should add a customer onto the customers dict with the 
customer's `id` as the key and the customer instance as the value.
"""


def test_06_add_a_customer():
    customer_dict = {
        "id": 1,
        "account_type": "sx",
        "first_name": "Monica",
        "last_name": "Gellar",
        "current_video_rentals": ["The Godfather"],
    }
    customer = Customer(**customer_dict)
    try:
        Customer.add_a_customer(customer_dict)
    except Exception as e:
        assert (
            e.args[0]
            == "This function will only accept an instance of the Customer class"
        )
        Customer.add_a_customer(customer)
        assert Customer.customers.get(customer.id) == customer
