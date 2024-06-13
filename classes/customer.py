# Write you Customer Class here
class Customer:
    customers = {}

    def __init__(
        self,
        id: int,
        first_name: str,
        last_name: str,
        account_type: str,
        current_video_rentals: list = [],
    ):
        self._id = id
        self.first_name = first_name
        self.last_name = last_name
        self._account_type = account_type
        self._current_video_rentals = current_video_rentals

    @property
    def id(self):
        return self._id

    @property
    def current_video_rentals(self):
        return self._current_video_rentals

    @current_video_rentals.setter
    def current_video_rentals(self, updated_list):
        if isinstance(updated_list, list):
            self._current_video_rentals = updated_list
        else:
            raise Exception("Current Video Rentals should only be a list")

    @staticmethod
    def create_a_customer_dict():
        def provide_name(forl: bool):
            name_type = "first" if forl else "last"
            name = input(f"Please provide your {name_type} name:\n")
            confirmation = input(f"Please type 'Y/y' to confirm {name} as your name:\n")
            if confirmation.upper() == "Y":
                return name
            return provide_name(forl)

        def select_account_type():
            acceptable_accounts = ["sx", "px", "sf", "pf"]
            account = input("Please input the account type you want:\n")
            if account.lower() in acceptable_accounts:
                return account
            print(
                f"This is not a valid account please choose from {', '.join(acceptable_accounts)}!"
            )
            return select_account_type()

        new_customer_dict = {
            "id": max(Customer.customers.keys()) + 1 if Customer.customers else 1,
            "first_name": provide_name(True),
            "last_name": provide_name(False),
            "account_type": select_account_type(),
        }
        return new_customer_dict

    @classmethod
    def add_a_customer(cls, customer):
        if customer and isinstance(customer, Customer):
            cls.customers[customer.id] = customer
            return f"{customer.first_name} ID:{customer.id} has been added into our database!"
        else:
            raise Exception(
                "This function will only accept an instance of the Customer class"
            )

    @classmethod
    def get_customer_by_id(cls):
        def provide_id() -> int:
            choice = input("Please provide your customer id:\n")
            if choice.isnumeric() and int(choice) in cls.customers.keys():
                return int(choice)
            print("Your input was invalid!")
            return provide_id()

        customer_id = provide_id()
        return cls.customers.get(customer_id)

    def get_customer_rented_videos(self):
        return f"{self.first_name} has the following rentals:\n{self.current_video_rentals}"

    def rent_a_video(self, video: tuple):
        if len(self.current_video_rentals) > 2:
            raise Exception("This customer can only rent out up to 3 videos")
        rentals = self.current_video_rentals
        rentals.append(video[0])
        self.current_video_rentals = rentals
        return self.get_customer_rented_videos()

    def return_a_video(self, video: str):
        if video in self.current_video_rentals:
            rentals = self.current_video_rentals
            rentals.remove(video)
            return self.get_customer_rented_videos()
        raise Exception("This video is not rented out by this customer!")
