from classes.store import Store, Video, Customer
import pytest

"""
- an instance of the Store Class will be instantiated
- upon the instance being created data for both Videos and Customers should be loaded
"""


def test_24_load_data():
    store = Store("Code Platoon")
    assert len(Video.videos) == 10
    assert len(Customer.customers) == 6
