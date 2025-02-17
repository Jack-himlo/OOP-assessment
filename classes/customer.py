# Write you Customer Class here
from classes.video import Video

class Customer:
    customer = {}
    counter = 1

    def __init__(self, id, first_name, last_name, account_type, current_video_rentals = None):
        self._id = id
        # Customer.counter += 1
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
            print(f"no current rentals available\n")
#view each instance of a "customer"    
    @classmethod
    def viewCustomer(cls):
        if not cls.customer:
            print("No customers found.\n")
            return
        for _id, customer in cls.customer.items():
            print(f"ID: {customer._id}")
            print(f"First name:  {customer.first_name}")
            print(f"Last name : {customer.last_name}")
            print(f"Account type: {customer._account_type}")
            print(f"Current Videos Rented: {customer._current_video_rentals}\n")
        
#add new customer class method
    @classmethod
    def add_a_customer(cls, customer):
        # deconstruct dict
        if isinstance(customer, dict):
            customer = cls(**customer) 
        # Ensure that the input is actually a Customer instance
        if not isinstance(customer, cls):
            raise TypeError("This function will only accept an instance of the Customer class")

    # Store the provided Customer instance in the customer dictionary
        cls.customer[customer.id] = customer

    # Return success message
        return f"{customer.first_name} has been added into our database!"
        
        
        
        # #assign customer id
        # _id = cls.counter
        # #increasecounter for unique ID
        # cls.counter += 1
        # #gather customer info
        # first_name = input("Enter customer first name: ")
        # last_name = input("Enter customer last name: ")
        # account_type = input("Enter customer account type: ")
        # #add new customer to class level dict customers
        # newCustomer = cls(_id,first_name, last_name, account_type)
        # cls.customer[_id] = newCustomer
        
        # print(f"Customer {first_name} {last_name}'s account has been added\n")
    @classmethod
    def delete_a_Customer(cls):
       #Loop interface until valid input
        while True:
        # toRemove = int(input("Enter the customer ID you would like to delete: "))
            try:
                toRemove = int(input("Enter the customer ID you would like to delete: "))
                break
            except ValueError:
                print("Error: Customer ID must be a number.\n")

        if toRemove in cls.customer:
            cls.customer.pop(toRemove)
            print(f"Customer ID: {toRemove}, has been removed.\n")
        else:
            print("There was no customer found with that ID\n")
    @staticmethod
    def  create_a_customer_dict():
        valid_account_types = {"sx", "px", "sf", "pf"}
        # Customer.counter += 1
        #require first name to be letters and longer than a single character 
        while True:
            first_name = input("Enter customer first name: ")
            if first_name.isalpha() and len(first_name) > 1:
                break
            print("enter a valid first name")
        #require last name to be letters and longer than a single character 
        while True:
            last_name = input("Enter customer last name: ")
            if last_name.isalpha() and len(last_name) > 1:
                break
            print("enter a valid last name")
        # require account type to valid input
        while True:
            account_type = input("Enter customer account type: ")
            if account_type.lower() in valid_account_types:
                break
            print("Invalid account type. Please enter one of: sx, px, sf, pf.")
        #returns customer data that was just added
        return {
            "id" : Customer.counter,
            "first_name" : first_name,
            "last_name" : last_name,
            "account_type" : account_type
        }
    #define class level method to find customer by ID
    @classmethod
    def get_customer_by_id(cls):
        #iterate through customer id list 
        while True:
            try:
                customer_id = input("enter customer id to search: ")
                customer_id = int(customer_id)
                break
            #require user to enter a number to search 
            except ValueError:
                print("Invalid ID. PLease enter a number.")
        #return customer if id is found
        if customer_id in cls.customer:
            return cls.customer[customer_id]
        #inform user customer id didnt find customer
        else:
            return f"No customer was found with that id"

    #define get customer rented videos method
    def get_customer_rented_videos(self):
        #check if customer currently has any rentals
        if self._current_video_rentals:
            return f"{self.first_name} has the following rentals:\n{self._current_video_rentals}"
        #if no rentals are found
        return f"{self.first_name} has no current rentals."
    
    #define rent a video method
    def rent_a_video(self, video_title):
        # from classes.video import Video
        #check account type, sort by max number of rentals
        if self._account_type.lower() == "sx" or self._account_type.lower() == "sf":
            max_rentals = 1
            #check i
            if len(self._current_video_rentals) >= max_rentals:
                return f"{self.first_name} has max amount of rentals"
        elif self._account_type.lower() == "px" or self._account_type.lower() == "pf":
            max_rentals = 3
            if len(self._current_video_rentals) >= max_rentals:
                return f"{self.first_name} has max amount of rentals"
            
        
            

    #define return a video
    def return_a_video(self, video_title):
        #check if title of movie is in customer rentals
        if video_title not in self._current_video_rentals:
            raise ValueError(f"{video_title} is not in your rentals.")
        ##remove title from customer rentals to return
        else:
            self._current_video_rentals.remove(video_title)
            return f"{self.first_name} has returned '{video_title}'."
    

        


# Customer.addCustomer()
# Customer.addCustomer()
# Customer.viewCustomer()
# Customer.deleteCustomer()
# Customer.viewCustomer()



