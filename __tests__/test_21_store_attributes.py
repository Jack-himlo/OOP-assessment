from classes.store import Store
import pytest

"""
- ensures all attributes of the Store Class Exist
"""

def test_21_store_attributes():
  store = Store("Code Platoon")
  assert hasattr(store, "name")