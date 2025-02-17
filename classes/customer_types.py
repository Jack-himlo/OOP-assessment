# Write your independent Customer account type classes here
#import Customer from classes.customer.py
from classes.customer import Customer

#inherint Customer 
class Customer_sx(Customer):
    def __init__(self, id, first_name, last_name, account_type = "sx" , current_video_rentals = None):
        super().__init__(id, first_name, last_name, account_type, current_video_rentals)
    


class Customer_px(Customer):
    
    def __init__(self, id, first_name, last_name, account_type = "px" , current_video_rentals = None):
        super().__init__(id, first_name, last_name, account_type, current_video_rentals)


class Customer_sf(Customer):
    
    def __init__(self, id, first_name, last_name, account_type = "sf" , current_video_rentals = None):
        super().__init__(id, first_name, last_name, account_type, current_video_rentals)


class Customer_pf(Customer):
    
    def __init__(self, id, first_name, last_name, account_type = "pf" , current_video_rentals = None):
        super().__init__(id, first_name, last_name, account_type, current_video_rentals)
