# Importing necessary modules and classes
from classes.store import Store
from classes.customer import Customer
from classes.customer_types import Customer_pf, Customer_sf, Customer_sx
from classes.video import Video
import pytest

# Creating an instance of the Store class
block_buster = Store("Block Buster")

# Loading data for customers and inventory
block_buster.load_data("customers")
block_buster.load_data("inventory")


class Test_Customer:
    def test_001_data_upacked_from_csv_customers(self):
        # Asserting that the number of customers loaded from CSV is 6
        assert len(list(Customer.customers.keys())) == 6

    def test_002_get_customer_by_id(self, monkeypatch):
        # Monkeypatching the input to simulate user input of "6"
        monkeypatch.setattr("builtins.input", lambda _: "6")
        # Asserting that the customer retrieved by ID is the one with ID 6
        assert Customer.get_customer_by_id() == Customer.customers.get(6)

    def test_003_return_a_video(self):
        # Retrieving a customer with ID 2
        customer = Customer.customers.get(2)
        # Setting the video to be returned by the customer
        customer.return_a_video = "The Dark Knight"
        # Asserting that the customer's current video rentals are updated correctly
        assert customer.current_video_rentals == ["Inception", "The Prestige"]

    def test_004_get_customer_rented_videos(self):
        # Retrieving a customer with ID 5
        customer = Customer.customers.get(5)
        # Asserting that the method returns a formatted string with the customer's rented videos
        assert (
            customer.get_customer_rented_videos()
            == f"{customer.first_name} has the following rentals:\n{customer.current_video_rentals}"
        )

    def test_005_create_customer_dict(self, monkeypatch):
        # Monkeypatching the input to simulate user input of "John", "Wick", and "sx"
        responses = iter(["John", "Wick", "sx"])
        monkeypatch.setattr("builtins.input", lambda _: next(responses))
        # Asserting that the created customer dictionary matches the expected dictionary
        assert Customer.create_customer() == {
            "id": 7,
            "first_name": "John",
            "last_name": "Wick",
            "account_type": "sx",
        }


class Test_Video:
    def test_006_data_unpacked_from_csv_inventory(self):
        # Asserting that the number of videos loaded from CSV is 10
        assert len(list(Video.videos.keys())) == 10

    def test_007_get_video_by_title(self, monkeypatch):
        # Monkeypatching the input to simulate user input of "Up"
        monkeypatch.setattr("builtins.input", lambda _: "Up")
        # Asserting that the video retrieved by title is the one with the title "Up"
        assert Video.get_a_video_by_title() == Video.videos.get("Up")

    def test_008_return_a_video(self):
        # Retrieving a video with the title "Inception"
        video = Video.videos.get("Inception")
        # Setting the number of returned videos to be one more than the available copies
        video.return_a_video = video.copies_available + 1
        # Asserting that the number of available copies is updated correctly
        assert video.copies_available == 5

    def test_009_rent_a_video(self):
        # Retrieving a video with the title "Inception"
        video = Video.videos.get("Inception")
        # Setting the number of rented videos to be one less than the available copies
        video.rent_a_video = video.copies_available - 1
        # Asserting that the number of available copies is updated correctly
        assert video.copies_available == 4


class Test_Runner:
    def test_010_entire_program_with_proper_input(self, monkeypatch):
        # Monkeypatching the input to simulate user interaction with the program
        responses = iter(
            [
                "1",
                "2",
                "6",
                "3",
                "John",
                "Boyd",
                "sx",
                "4",
                "7",
                "Up",
                "5",
                "7",
                "Up",
                "6",
            ]
        )
        monkeypatch.setattr("builtins.input", lambda _: next(responses))
        # Asserting that the program runs successfully and returns the expected message
        assert block_buster.run_the_store() == "Thank you, please come again!"

    def test_011_entire_program_with_improper_input_included(self, monkeypatch):
        # Monkeypatching the input to simulate user interaction with the program including improper inputs
        responses = iter([
                "adifhad", "1",
                "adifhad", "adifhad", "2",
                "adifhad", "6",
                "adifhad", "adifhad", "3",
                "adifhad", "John",
                "adifhad", "adifhad", "Boyd",
                "adifhad", "adifhad", "sx",
                "adifhad", "adifhad", "4",
                "adifhad", "7",
                "adifhad", "adifhad", "Up",
                "adifhad", "5",
                "adifhad", "adifhad", "7",
                "adifhad", "Up",
                "adifhad", "adifhad", "6",
            ])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        # Asserting that the program runs successfully and returns the expected message
        assert block_buster.run_the_store() == "Thank you, please come again!"

    def test_012_adding_a_customer_pf(self):
        # Creating a customer dictionary with account_type "pf"
        pf = {
            "id": 7,
            "first_name": "John",
            "last_name": "Wick",
            "account_type": "pf",
        }
        # Creating a customer instance using the customer_type_maker method
        customer = block_buster.customer_type_maker(pf)
        # Asserting that the customer instance is of the expected class Customer_pf
        assert isinstance(customer, Customer_pf)

    def test_013_adding_a_customer_sf(self):
        # Creating a customer dictionary with account_type "sf"
        sf = {
            "id": 7,
            "first_name": "John",
            "last_name": "Wick",
            "account_type": "sf",
        }
        # Creating a customer instance using the customer_type_maker method
        customer = block_buster.customer_type_maker(sf)
        # Asserting that the customer instance is of the expected class Customer_sf
        assert isinstance(customer, Customer_sf)

    def test_014_adding_a_customer_sx(self):
        # Creating a customer dictionary with account_type "sx"
        sx = {
            "id": 7,
            "first_name": "John",
            "last_name": "Wick",
            "account_type": "sx",
        }
        # Creating a customer instance using the customer_type_maker method
        customer = block_buster.customer_type_maker(sx)
        # Asserting that the customer instance is of the expected class Customer_sx
        assert isinstance(customer, Customer_sx)

    def test_015_adding_a_customer_count(self):
        assert len(list(Customer.customers.keys())) == 8


class Test_Renting_A_Video:

    def test_016_px_too_many_videos(self):
        # Retrieving a customer with ID 2
        customer = Customer.customers.get(2)
        # Renting a video with title "Up" and rating "G"
        customer.rent_a_video = ("Up", "G")
        # Asserting that the number of current video rentals for the customer is 3
        assert len(customer.current_video_rentals) == 3

    def test_017_px_rent_rated_R(self):
        # Retrieving a customer with ID 6
        customer = Customer.customers.get(6)
        # Renting a video with title "Deadpool" and rating "R"
        customer.rent_a_video = ("Deadpool", "R")
        # Asserting that the number of current video rentals for the customer is 3
        assert len(customer.current_video_rentals) == 3

    def test_018_pf_too_many_videos(self):
        # Retrieving a customer with ID 3
        customer = Customer.customers.get(3)
        # Renting a video with title "Up" and rating "G"
        customer.rent_a_video = ("Up", "G")
        # Asserting that the current video rentals for the customer match the expected list
        assert customer.current_video_rentals == ['Inside Out', 'WALL-E', 'The Prestige']

    def test_019_pf_rated_R(self):
        # Retrieving a customer with ID 3
        customer = Customer.customers.get(3)
        # Returning the video "WALL-E"
        customer.return_a_video = "WALL-E"
        # Renting a video with title "Deadpool" and rating "R"
        customer.rent_a_video = ("Deadpool", "R")
        # Asserting that the current video rentals for the customer match the expected list
        assert customer.current_video_rentals == ['Inside Out', 'The Prestige']

    def test_020_sx_too_many_videos(self):
        # Retrieving a customer with ID 1
        customer = Customer.customers.get(1)
        # Renting a video with title "Deadpool" and rating "R"
        customer.rent_a_video = ("Deadpool", "R")
        # Asserting that the current video rentals for the customer match the expected list
        assert customer.current_video_rentals == ["The Godfather"]

    def test_021_sx_rated_R(self):
        # Retrieving a customer with ID 4
        customer = Customer.customers.get(4)
        # Renting a video with title "Deadpool" and rating "R"
        customer.rent_a_video = ("Deadpool", "R")
        # Asserting that the current video rentals for the customer match the expected list
        assert customer.current_video_rentals == ["Deadpool"]

    def test_022_sf_too_many_videos(self):
        # Retrieving a customer with ID 5
        customer = Customer.customers.get(5)
        # Renting a video with title "Up" and rating "G"
        customer.rent_a_video = ("Up", "G")
        # Asserting that the current video rentals for the customer match the expected list
        assert customer.current_video_rentals == ["WALL-E"]

    def test_023_sf_rated_R(self):
        # Retrieving a customer with ID 5
        customer = Customer.customers.get(5)
        # Returning the video "WALL-E"
        customer.return_a_video = 'WALL-E'
        # Renting a video with title "Deadpool" and rating "R"
        customer.rent_a_video = ("Deadpool", "R")
        # Asserting that the current video rentals for the customer match the expected list
        assert customer.current_video_rentals == []



