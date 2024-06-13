from classes.customer_types import Customer_pf, Customer_sf, Customer_px, Customer_sx
from classes.customer import Customer
import pytest

"""
- Ensures all attributes from Customer class have been inherited
"""



def test_10_customer_pf_inheritance():
    base_class_attributes = set(dir(Customer))
    inherit_class_attributes = set(dir(Customer_pf))
    missing_attributes = base_class_attributes - inherit_class_attributes
    assert not missing_attributes
    inherit_class_attributes = set(dir(Customer_px))
    missing_attributes = base_class_attributes - inherit_class_attributes
    assert not missing_attributes
    inherit_class_attributes = set(dir(Customer_sf))
    missing_attributes = base_class_attributes - inherit_class_attributes
    assert not missing_attributes
    inherit_class_attributes = set(dir(Customer_sx))
    missing_attributes = base_class_attributes - inherit_class_attributes
    assert not missing_attributes

