from classes.customer_types import Customer_sx

"""
- test will create a Customer_sx
- customer will attempt to rent out more than 3 copy
- customer will return a video
- customer will rent out a video that is R rated
"""


def test_14_customer_sx_rent_a_video():
    customer = Customer_sx(
        **{
            "id": 3,
            "account_type": "sx",
            "first_name": "Rachel",
            "last_name": "Green",
            "current_video_rentals": ["The Dark Knight"],
        }
    )
    try:
        customer.rent_a_video(("Deadpool", "R"))
    except Exception:
          customer.return_a_video("The Dark Knight")
          customer.rent_a_video(("Deadpool", "R"))
    assert customer.current_video_rentals == ["Deadpool"]
