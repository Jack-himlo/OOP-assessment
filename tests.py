import runner
from classes.customer import Customer
from classes.video import Video
from classes.media_interface import Media
import pytest


class Test_Customer:

    def test_001_data_upacked_from_csv_customers(self):
        assert len(Customer.list_of_customers) == 6

    def test_002_get_a_customer_instance(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: '6')
        assert Customer.get_an_instance() == Customer.list_of_customers.get(6)

    def test_003_validate_video_rental_px(self, monkeypatch):
        video = Video.get_an_instance("Inception")
        monkeypatch.setattr('builtins.input', lambda _: '6')
        customer = Customer.get_an_instance()
        assert customer.validate_video_rental(video) == True

    def test_004_validate_video_rental_sx(self, monkeypatch):
        video = Video.get_an_instance("Inception")
        monkeypatch.setattr('builtins.input', lambda _: '4')
        customer = Customer.get_an_instance()
        assert customer.validate_video_rental(video) == True

    def test_005_validate_video_rental_sx(self, monkeypatch):
        video = Video.get_an_instance("Up")
        monkeypatch.setattr('builtins.input', lambda _: '4')
        customer = Customer.get_an_instance()
        customer.current_video_rentals.append("Inception")
        assert customer.validate_video_rental(video) == False
        customer.current_video_rentals.clear()

    def test_006_validate_video_rental_sf_too_many_videos(self, monkeypatch):
        video = Video.get_an_instance("Toy Story")
        monkeypatch.setattr('builtins.input', lambda _: '5')
        customer = Customer.get_an_instance()
        assert customer.validate_video_rental(video) == False

    def test_007_validate_video_rental_pf_too_many_videos(self, monkeypatch):
        video = Video.get_an_instance("Toy Story")
        monkeypatch.setattr('builtins.input', lambda _: '3')
        customer = Customer.get_an_instance()
        assert customer.validate_video_rental(video) == False

    def test_008_validate_video_rental_pf_rated_R(self, monkeypatch):
        video = Video.get_an_instance("Deadpool")
        monkeypatch.setattr('builtins.input', lambda _: '3')
        customer = Customer.get_an_instance()
        customer.current_video_rentals.remove("WALL-E")
        assert customer.validate_video_rental(video) == False

    def test_009_validate_video_rental_pf(self, monkeypatch):
        video = Video.get_an_instance("WALL-E")
        monkeypatch.setattr('builtins.input', lambda _: '3')
        customer = Customer.get_an_instance()
        assert customer.validate_video_rental(video) == True

    def test_010_validate_video_rental_sf_rated_R(self, monkeypatch):
        video = Video.get_an_instance("Deadpool")
        monkeypatch.setattr('builtins.input', lambda _: '5')
        customer = Customer.get_an_instance()
        customer.current_video_rentals.clear()
        assert customer.validate_video_rental(video) == False

    def test_011_validate_video_rental_sf(self, monkeypatch):
        video = Video.get_an_instance("Up")
        monkeypatch.setattr('builtins.input', lambda _: '5')
        customer = Customer.get_an_instance()
        assert customer.validate_video_rental(video) == True

    def test_012_renting_a_video(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'Inception')
        customer = Customer.list_of_customers.get(6)
        assert customer.rent_a_video(
        ) == "Inception has been added to your list of rentals, thank you!"

    def test_013_validate_video_rental_px_too_many_copies(self, monkeypatch):
        video = Video.get_an_instance("Inception")
        monkeypatch.setattr('builtins.input', lambda _: '6')
        customer = Customer.get_an_instance()
        assert customer.validate_video_rental(video) == False

    def test_014_returning_a_video(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'Inception')
        customer = Customer.list_of_customers.get(6)
        assert customer.return_a_video(
        ) == "Inception has been removed from your list of rentals, thank you!"

    def test_015_construct_customer_dict(self, monkeypatch):
        responses = iter(['sx', 'Jimmy', 'John'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        assert Customer.construct_new_customer_dict() == {'current_video_rentals': [
        ], 'account_type': 'sx', 'first_name': "Jimmy", 'last_name': "John"}

    def test_016_create_new_customer(self):
        customer = {'current_video_rentals': [], 'account_type': 'sx',
                    'first_name': "Jimmy", 'last_name': "John"}
        assert Customer.create_new_customer(
            customer) == "Jimmy has been added as a customer! \nCustomer ID: 7"


class Test_Video:

    def test_017_data_unpacked_from_csv_inventory(self):
        assert len(Video.list_of_videos) == 10

    def test_018_getting_a_video_instance(self):
        assert Video.get_an_instance('Inception') == list(
            filter(lambda x: x.title == 'Inception', Video.list_of_videos))[0]

    def test_019_return_a_video(self):
        video = Video.get_an_instance("Inception")
        assert video.return_a_video() == "Inception was successfully returned, thank you!"

    def test_020_rent_a_video(self):
        video = Video.get_an_instance("Inception")
        assert video.rent_a_video() == "Inception was successfully checked out, thank you!"


class Test_Media:

    def test_021_load_data_exist(self):
        assert Media.load_data

    def test_022_get_an_instance(self):
        assert Media.get_an_instance

    def test_023_return_a_video(self):
        assert Media.return_a_video

    def test_024_rent_a_video(self):
        assert Media.rent_a_video


class Test_Runner:

    def test_025_entire_program_with_proper_input(self, monkeypatch):
        responses = iter(['1', '2', '6', '3', 'sx', 'John',
                         'Boyd', '4', '7', 'Up', '5', '7', 'Up', '6'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        assert runner.run_the_store() == "Thank you, please come again!"

    def test_026_entire_program_with_improper_input_included(self, monkeypatch):
        responses = iter(['sx', '1', 'afdaed', '2', 'adfe', '2', '6', '9', '3', '35', 'sx', 'John',
        'Boyd', '4', 'adf', '4', '7', 'adfd', '4', '7', 'Up', '5', 'adfe', '5', '7', 'ajhfpoa', 'Up', '6'])
        monkeypatch.setattr('builtins.input', lambda _: next(responses))
        assert runner.run_the_store() == "Thank you, please come again!"