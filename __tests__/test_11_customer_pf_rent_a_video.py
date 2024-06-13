from classes.customer_types import Customer_pf

"""
- test will create a Customer_pf
- customer will attempt to rent out more than 3 copies
- customer will return a video
- customer will attempt to rent out a video that is R rated
- customer will rent out a video that is G rated
"""


def test_11_customer_pf_rent_a_video():
    customer = Customer_pf(**{
        "id": 3,
        "account_type": "pf",
        "first_name": "Rachel",
        "last_name": "Green",
        "current_video_rentals": ["Inside Out", "WALL-E", "The Prestige"],
    })
    try:
        customer.rent_a_video(("Deadpool","R"))
    except Exception:
        try:
            customer.return_a_video("WALL-E")
            customer.rent_a_video(("Deadpool","R"))
        except Exception:
            customer.rent_a_video(("Up", "G"))
    assert customer.current_video_rentals == ["Inside Out", "The Prestige", "Up"]

