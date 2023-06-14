class Customer:
    customers = {}

    def __init__(
        self, id, account_type, first_name, last_name, current_video_rentals = []
    ):
        self._id = id
        self._account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        self._current_video_rentals = current_video_rentals

    @property
    def id(self):
        return self._id

    @property
    def current_video_rentals(self):
        return self._current_video_rentals

    @current_video_rentals.setter
    def rent_a_video(self, vide_details):
        title, rating = vide_details
        if len(self.current_video_rentals) < 3:
            self._current_video_rentals.append(title)
        else:
            print("You have too many videos rented!")


    @current_video_rentals.setter
    def return_a_video(self, title):
        if title in self.current_video_rentals:
            self._current_video_rentals.remove(title)
        else:
            print("You don't currently have this video!")



    @classmethod
    def get_customer_by_id(cls):
        id = input("Enter your customer ID: ")
        if id.isnumeric() and int(id) in cls.customers:
            return cls.customers.get(int(id))
        else:
            print("This ID does not exist!")
            return cls.get_customer_by_id()

    @classmethod
    def create_customer(cls):
        def select_an_account_type():
            acceptable_account_types = ["sx", "px", "sf", "pf"]
            account_type = input(
                f"Enter one of the following account types {acceptable_account_types}:  "
            )
            if account_type in acceptable_account_types:
                return account_type
            else:
                return select_an_account_type()

        new_customer = {}
        id = max(list(cls.customers.keys())) + 1
        new_customer["id"] = id
        new_customer["first_name"] = input("Enter your first name:    ")
        new_customer["last_name"] = input("Enter your last name:    ")
        new_customer["account_type"] = select_an_account_type()
        print(f"New customer {new_customer['first_name']} with an id of {id}")
        return new_customer

    def get_customer_rented_videos(self):
        return f"{self.first_name} has the following rentals:\n{self.current_video_rentals}"