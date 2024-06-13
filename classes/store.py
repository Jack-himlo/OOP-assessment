from classes.customer_types import (
    Customer,
    Customer_sx,
    Customer_px,
    Customer_sf,
    Customer_pf,
)
from classes.video import Video
import csv
import os


# Write your Store Class here
class Store:
    def __init__(self, name):
        self.name = name
        self.load_data("customers")
        self.load_data("videos")

    def customer_type_maker(self, customer_dict: dict):
        customer = None
        if customer_dict.get("account_type") == "sx":
            customer = Customer_sx(**customer_dict)
        elif customer_dict.get("account_type") == "sf":
            customer = Customer_sf(**customer_dict)
        elif customer_dict.get("account_type") == "px":
            customer = Customer_px(**customer_dict)
        else:
            customer = Customer_pf(**customer_dict)
        return customer

    def load_data(self, file_name):
        if file_name not in ["customers", "videos"]:
            raise Exception("This is not a valid parameter")
        with open(os.path.abspath(f"./data/{file_name}.csv"), "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["id"] = int(row.get("id"))
                if file_name == "customers":
                    row["current_video_rentals"] = (
                        row["current_video_rentals"].split("/")
                        if row["current_video_rentals"]
                        else []
                    )
                    customer = self.customer_type_maker(row)
                    Customer.add_a_customer(customer)
                else:
                    row["release_year"] = int(row["release_year"])
                    row["copies_available"] = int(row["copies_available"])
                    Video.add_a_video(Video(**row))

    def run_the_store(self):
        menu = """
== Welcome to Code Platoon Video! ==
1. View store video inventory
2. View customer rented videos
3. Add new customer
4. Rent video
5. Return video
6. Exit
"""
        choice = input(f"{menu}")
        match choice:
            case "1":
                Video.list_inventory()
                return self.run_the_store()
            case "2":
                customer = Customer.get_customer_by_id()
                print(customer.get_customer_rented_videos())
                return self.run_the_store()
            case "3":
                customer_dict = Customer.create_a_customer_dict()
                new_customer = self.customer_type_maker(customer_dict)
                print(Customer.add_a_customer(new_customer))
                return self.run_the_store()
            case "4":
                customer = Customer.get_customer_by_id()
                Video.list_inventory()
                video = Video.get_a_video_by_title()
                print(video.title, video.copies_available)
                try:
                    if video.copies_available:
                        customer.rent_a_video((video.title, video.rating))
                        video.copies_available -= 1
                except Exception as e:
                    print(e.args[0])
                return self.run_the_store()
            case "5":
                customer = Customer.get_customer_by_id()
                print(customer.get_customer_rented_videos())
                try:
                    video = Video.get_a_video_by_title()
                    customer.return_a_video(video.title)
                    video.copies_available += 1
                except Exception as e:
                    print(e.args[0])
                return self.run_the_store()
            case "6":
                return "Thank you, please come again!"
            case _:
                print("This is not a valid input")
                return self.run_the_store()
