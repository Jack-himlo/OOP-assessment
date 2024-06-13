from classes.store import Store
import pytest

"""
- Ensures all class methods exist
"""


def test_22_store_methods():
    assert hasattr(Store, "customer_type_maker")
    assert hasattr(Store, "load_data")
    assert hasattr(Store, "run_the_store")
