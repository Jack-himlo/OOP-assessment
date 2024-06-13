from classes.store import Store
from classes.customer_types import Customer_pf, Customer_sf, Customer_sx, Customer_px
import pytest

"""
- example dict wil be created to be passed into the customer_type_maker method
- customer_type_method will return the correct instance of the customer matching by account type
"""


def test_23_customer_type_maker():
    example_input = {
        "id": 7,
        "first_name": "Daniel",
        "last_name": "Vasquez",
        "account_type": "sf",
    }
    store = Store("Code Platoon")
    assert isinstance(store.customer_type_maker(example_input), Customer_sf)
    example_input["account_type"] = "sx"
    assert isinstance(store.customer_type_maker(example_input), Customer_sx)
    example_input["account_type"] = "px"
    assert isinstance(store.customer_type_maker(example_input), Customer_px)
    example_input["account_type"] = "pf"
    assert isinstance(store.customer_type_maker(example_input), Customer_pf)
