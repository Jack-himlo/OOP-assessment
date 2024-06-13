from classes.customer import Customer


# Write your independent Customer account type classes here
class Customer_sx(Customer):
    

    def rent_a_video(self, video: tuple):
        if len(self.current_video_rentals) > 0:
            raise Exception("This customer can only rent out up to 1 video")
        rentals = self.current_video_rentals
        rentals.append(video[0])
        self.current_video_rentals = rentals
        return self.get_customer_rented_videos()


class Customer_px(Customer):
    pass


class Customer_sf(Customer):
    

    def rent_a_video(self, video: tuple):
        if len(self.current_video_rentals) > 0 or video[1] == "R":
            raise Exception(
                "This customer can only rent out up to 1 video and none rated R"
            )
        rentals = self.current_video_rentals
        rentals.append(video[0])
        self.current_video_rentals = rentals
        return self.get_customer_rented_videos()


class Customer_pf(Customer):
    

    def rent_a_video(self, video: tuple):
        if len(self.current_video_rentals) > 2 or video[1] == "R":
            raise Exception(
                "This customer can only rent out up to 3 videos and none rated R"
            )
        rentals = self.current_video_rentals
        rentals.append(video[0])
        self.current_video_rentals = rentals
        return self.get_customer_rented_videos()
