from classes.customer import Customer
from classes.customer_types import Customer_pf, Customer_sf, Customer_sx, Customer_px
from classes.video import Video
import csv


class Store:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def customer_type_maker(self, row):
        match row.get("account_type"):
            case "sx":
                return Customer_sx(**row)
            case "sf":
                return Customer_sf(**row)
            case "pf":
                return Customer_pf(**row)
            case _:
                return Customer_px(**row)

    def load_data(self, file):
        with open(f"./data/{file}.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row["id"] = int(row["id"])
                if file == "inventory":
                    row["copies_available"] = int(row["copies_available"])
                    Video.videos[row["title"]] = Video(**row)
                else:
                    if row["current_video_rentals"]:
                        row["current_video_rentals"] = row[
                            "current_video_rentals"
                        ].split("/")
                    else:
                        row["current_video_rentals"] = []
                    Customer.customers[row["id"]] = self.customer_type_maker(row)

    # Write your solution here!
    def run_the_store(self):
        user_choice = input(
            f"""== Welcome to {self.name}! ==
1. View store video inventory
2. View customer rented videos
3. Add new customer
4. Rent video
5. Return video
6. Exit
"""
        )
        match user_choice:
            case "1":
                Video.list_inventory()
                return self.run_the_store()
            case "2":
                customer = Customer.get_customer_by_id()
                print(customer.get_customer_rented_videos())
                return self.run_the_store()
            case "3":
                new_customer = Customer.create_customer()
                Customer.customers[new_customer["id"]] = self.customer_type_maker(
                    new_customer
                )
                return self.run_the_store()
            case "4":
                customer = Customer.get_customer_by_id()
                video = Video.get_a_video_by_title()
                if video.copies_available:
                    customer.rent_a_video = (video.title, video.rating)
                video.rent_a_video = video.copies_available - 1
                return self.run_the_store()
            case "5":
                customer = Customer.get_customer_by_id()
                video = Video.get_a_video_by_title()
                customer.return_a_video = video.title
                if video.title not in customer.current_video_rentals:
                    video.return_a_video = video.copies_available + 1
                return self.run_the_store()
            case "6":
                return "Thank you, please come again!"
            case _:
                print("invalid input".upper())
                return self.run_the_store()


# ENSURE THE PRINT STATEMENT IS COMMENTED OUT WHEN YOU SUBMIT YOUR ASSESSMENT AND RUN TESTS
# block_buster = Store("Block Buster")
# block_buster.load_data("inventory")
# block_buster.load_data("customers")
# print(block_buster.run_the_store())
