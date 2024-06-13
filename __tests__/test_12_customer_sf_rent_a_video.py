from classes.customer_types import Customer_sf

"""
- test will create a Customer_sf
- customer will attempt to rent out more than 1 copy
- customer will return a video
- customer will attempt to rent out a video that is R rated
- customer will rent out a video that is G rated
"""


def test_12_customer_sf_rent_a_video():
    customer = Customer_sf(**{
        "id": 3,
        "account_type": "sf",
        "first_name": "Rachel",
        "last_name": "Green",
        "current_video_rentals": ["WALL-E"],
    })
    try:
        customer.rent_a_video(("Deadpool","R"))
    except Exception:
        try:
            customer.return_a_video("WALL-E")
            customer.rent_a_video(("Deadpool","R"))
        except Exception:
            customer.rent_a_video(("Up", "G"))
    assert customer.current_video_rentals == ["Up"]
