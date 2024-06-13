from classes.customer import Customer
import pytest
"""
This test will ensure there is a customer class and that 
a customer class can be properly created
"""

def test_01_customer_creation():
  customer = {
    "id":1,
    "account_type":"sx",
    "first_name":"Monica",
    "last_name":"Gellar",
    "current_video_rentals":["The Godfather"]
  }
  monica = Customer(**customer)
  assert isinstance(monica, Customer)
