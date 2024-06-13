from classes.customer_types import Customer_px

"""
- test will create a Customer_px
- customer will attempt to rent out more than 3 copy
- customer will return a video
- customer will rent out a video that is R rated
"""


def test_13_customer_px_rent_a_video():
    customer = Customer_px(
        **{
            "id": 3,
            "account_type": "px",
            "first_name": "Rachel",
            "last_name": "Green",
            "current_video_rentals": ["The Dark Knight", "Inception", "The Prestige"],
        }
    )
    try:
        customer.rent_a_video(("Deadpool", "R"))
    except Exception:
          customer.return_a_video("Inception")
          customer.rent_a_video(("Deadpool", "R"))
    assert customer.current_video_rentals == ["The Dark Knight", "The Prestige", "Deadpool"]
