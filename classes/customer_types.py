# Write your independent Customer account type classes here
#import Customer from classes.customer.py
from classes.customer import Customer
from classes.video import Video

#inherint Customer 
class Customer_pf(Customer):  # Premium Family (Max 3, No R-rated Movies)
    def rent_a_video(self, video_title):
        return super().rent_a_video(video_title)


class Customer_sf(Customer):  # Standard Family (Max 1, No R-rated Movies)
    def rent_a_video(self, video_title):
        return super().rent_a_video(video_title)


class Customer_px(Customer):  # Premium (Max 3, Can rent R-rated)
    def rent_a_video(self, video_title):
        return super().rent_a_video(video_title)


class Customer_sx(Customer):  # Standard (Max 1, Can rent R-rated)
    def rent_a_video(self, video_title):
        return super().rent_a_video(video_title)