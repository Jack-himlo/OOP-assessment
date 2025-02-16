# Write you Customer Class here
class Customer:
    customer = {}
    def __init__(self, customer_id, first_name, last_name, account_type):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.account_type = account_type
        self._current_rentals = []

    @property
    def id(self):
        return self.customer_id
    @property
    def current_rentals(self):
        return self._current_rentals
    @current_rentals.setter
    def current_rentals(self, rentals):
        if isinstance(rentals, list):
            self._current_rentals = rentals
        elif isinstance(rentals, str):
            self._current_rentals = [rentals]
        else:
            print(f"no current rentals available")
    
    def viewCustomer(self):
        return {
            "ID" : self.customer_id,
            "First name" : self.first_name,
            "Last name" : self.last_name,
            "Account type": self.account_type,
            "Current Videos Rented" : self._current_rentals
        }
    def addCustomer(self, customer_id, first_name, last_name, account_type):
        id = 0 
        customer_id = id + 1
        fName = first_name