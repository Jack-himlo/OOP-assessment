from runner import Store
from classes.customer import Customer
from classes.customer_types import Customer_pf, Customer_sf, Customer_sx
from classes.video import Video
import pytest

block_buster = Store("Block Buster")
block_buster.load_data("customers")
block_buster.load_data("inventory")


class Test_Customer:
    def test_001_data_upacked_from_csv_customers(self):
        assert len(list(Customer.customers.keys())) == 6

    def test_002_get_customer_by_id(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "6")
        assert Customer.get_customer_by_id() == Customer.customers.get(6)

    def test_003_return_a_video(self):
        customer = Customer.customers.get(2)
        customer.return_a_video = "The Dark Knight"
        assert customer.current_video_rentals == ["Inception", "The Prestige"]

    def test_004_get_customer_rented_videos(self):
        customer = Customer.customers.get(5)
        assert (
            customer.get_customer_rented_videos()
            == f"{customer.first_name} has the following rentals:\n{customer.current_video_rentals}"
        )

    def test_005_create_customer_dict(self, monkeypatch):
        responses = iter(["John", "Wick", "sx"])
        monkeypatch.setattr("builtins.input", lambda _: next(responses))
        assert Customer.create_customer() == {
            "id": 7,
            "first_name": "John",
            "last_name": "Wick",
            "account_type": "sx",
        }


class Test_Video:
    def test_006_data_unpacked_from_csv_inventory(self):
        assert len(list(Video.videos.keys())) == 10

    def test_007_get_video_by_title(self, monkeypatch):
        monkeypatch.setattr("builtins.input", lambda _: "Up")
        assert Video.get_a_video_by_title() == Video.videos.get("Up")

    def test_008_return_a_video(self):
        video = Video.videos.get("Inception")
        video.return_a_video = video.copies_available + 1
        assert video.copies_available == 5

    def test_009_rent_a_video(self):
        video = Video.videos.get("Inception")
        video.rent_a_video = video.copies_available - 1
        assert video.copies_available == 4


class Test_Runner:
    def test_010_entire_program_with_proper_input(self, monkeypatch):
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
        assert block_buster.run_the_store() == "Thank you, please come again!"

    def test_011_entire_program_with_improper_input_included(self, monkeypatch):
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
        assert block_buster.run_the_store() == "Thank you, please come again!"

    def test_012_adding_a_customer_pf(self):
        pf = {
            "id": 7,
            "first_name": "John",
            "last_name": "Wick",
            "account_type": "pf",
        }
        customer = block_buster.customer_type_maker(pf)
        assert isinstance(customer, Customer_pf)


    def test_013_adding_a_customer_sf(self):
        sf = {
            "id": 7,
            "first_name": "John",
            "last_name": "Wick",
            "account_type": "sf",
        }
        customer = block_buster.customer_type_maker(sf)
        assert isinstance(customer, Customer_sf)

    def test_014_adding_a_customer_sx(self):
        sx = {
            "id": 7,
            "first_name": "John",
            "last_name": "Wick",
            "account_type": "sx",
        }
        customer = block_buster.customer_type_maker(sx)
        assert isinstance(customer, Customer_sx)


class Test_Renting_A_Video:

    def test_015_px_too_many_videos(self):
        customer = Customer.customers.get(2)
        customer.rent_a_video = ("Up", "G")
        assert len(customer.current_video_rentals) == 3

    def test_016_px_rent_rated_R(self):
        customer = Customer.customers.get(6)
        customer.rent_a_video = ("Deadpool", "R")
        assert len(customer.current_video_rentals) == 3

    def test_017_pf_too_many_videos(self):
        customer = Customer.customers.get(3)
        customer.rent_a_video = ("Up", "G")
        assert customer.current_video_rentals == ['Inside Out', 'WALL-E', 'The Prestige']

    def test_018_pf_rated_R(self):
        customer = Customer.customers.get(3)
        customer.return_a_video = "WALL-E"
        customer.rent_a_video = ("Deadpool", "R")
        assert customer.current_video_rentals == ['Inside Out', 'The Prestige']

    def test_019_sx_too_many_videos(self):
        customer = Customer.customers.get(1)
        customer.rent_a_video = ("Deadpool", "R")
        assert customer.current_video_rentals == ["The Godfather"]

    def test_020_sx_rated_R(self):
        customer = Customer.customers.get(4)
        customer.rent_a_video = ("Deadpool", "R")
        assert customer.current_video_rentals == ["Deadpool"]

    def test_021_sf_too_many_videos(self):
        customer = Customer.customers.get(5)
        customer.rent_a_video = ("Up", "G")
        assert customer.current_video_rentals == ["WALL-E"]
    
    def test_022_sf_rated_R(self):
        customer = Customer.customers.get(5)
        customer.return_a_video = 'WALL-E'
        customer.rent_a_video = ("Deadpool", "R")
        assert customer.current_video_rentals == []