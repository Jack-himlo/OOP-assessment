from classes.customer import Customer
import pytest

"""
- ensures instance methods of rent_a_video and return_a_video existing within the program
"""


def test_09_rent_return_a_video():
    assert hasattr(Customer, 'return_a_video')
    assert hasattr(Customer, 'rent_a_video')