from classes.customer import Customer


class Customer_pf(Customer):
    def __init__(
        self, id, account_type, first_name, last_name, current_video_rentals=[]
    ):
        super().__init__(id, account_type, first_name, last_name, current_video_rentals)

    @Customer.current_video_rentals.setter
    def rent_a_video(self, video_details):
        title, rating = video_details
        if len(self.current_video_rentals) < 3 and rating != "R":
            self._current_video_rentals.append(title)
        else:
            print("You have too many videos rented!")


class Customer_sf(Customer):
    def __init__(
        self, id, account_type, first_name, last_name, current_video_rentals=[]
    ):
        super().__init__(id, account_type, first_name, last_name, current_video_rentals)

    @Customer.current_video_rentals.setter
    def rent_a_video(self, video_details):
        title, rating = video_details
        if len(self.current_video_rentals) < 1 and rating != "R":
            self._current_video_rentals.append(title)
        else:
            print("You have too many videos rented!")

class Customer_px(Customer):
    def __init__(
        self, id, account_type, first_name, last_name, current_video_rentals=[]
    ):
        super().__init__(id, account_type, first_name, last_name, current_video_rentals)

class Customer_sx(Customer):
    def __init__(
        self, id, account_type, first_name, last_name, current_video_rentals=[]
    ):
        super().__init__(id, account_type, first_name, last_name, current_video_rentals)

    @Customer.current_video_rentals.setter
    def rent_a_video(self, video_details):
        title, rating = video_details
        if len(self.current_video_rentals) < 1:
            self._current_video_rentals.append(title)
        else:
            print("You have too many videos rented!")
