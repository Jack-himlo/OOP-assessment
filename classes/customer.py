# Write you Customer Class here
class Customer:
    customer = {}
    counter = 0
    def __init__(self, id, first_name, last_name, account_type, current_video_rentals = None):
        self._id = id
        Customer.counter += 1
        self.first_name = first_name
        self.last_name = last_name
        self._account_type = account_type
        self._current_video_rentals = current_video_rentals
#set getters
    @property
    def id(self):
        return self._id
    @property
    def current_video_rentals(self):
        return self._current_video_rentals
#rentals should return a list type, set setter
    @current_video_rentals.setter
    def current_video_rentals(self, rentals):
        if isinstance(rentals, list):
            self._current_video_rentals = rentals
        elif isinstance(rentals, str):
            self._current_video_rentals = [rentals]
        else:
            print(f"no current rentals available")
#view each instance of a "customer"    
    @classmethod
    def viewCustomer(cls):
        if not cls.customer:
            print("No customers found.")
            return
        for _id, customer in cls.customer.items():
            print(f"ID: {customer._id}")
            print(f"First name:  {customer.first_name}")
            print(f"Last name : {customer.last_name}")
            print(f"Account type: {customer.account_type}")
            print(f"Current Videos Rented: {customer._current_video_rentals}\n")
        
#add new customer class method
    @classmethod
    def addCustomer(cls):
        #assign customer id
        _id = cls.counter
        #increasecounter for unique ID
        cls.counter += 1
        #gather customer info
        first_name = input("Enter customer first name: ")
        last_name = input("Enter customer last name: ")
        account_type = input("Enter customer account type: ")
        #add new customer to class level dict customers
        newCustomer = cls(customer_id,first_name, last_name, account_type)
        cls.customer[customer_id] = newCustomer
        
        print(f"Customer {first_name} {last_name}'s account has been added")



