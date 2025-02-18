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
        self._current_video_rentals = [] if current_video_rentals is None else list(current_video_rentals)
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
        title, rating = video_title
        print(f"{self.first_name} is trying to rent '{title}'")
        
        video = Video.videos.get(title)
        #check if video in inventory
        if not video:
            return f"Error: {title} is not available in our inventory."
        #check is copies are available 
        if video.copies_available < 1:
            return f"Sorry, {title} is currently out of stock."
        
        
        
        
        max_rentals = 1 if self._account_type in ["sx", "sf"] else 3
        if len(self._current_video_rentals) >= max_rentals:
            return f"{self.first_name} has max amount of rentals."
         
        
        #    if len(self._current_video_rentals) >= max_rentals:
        #     return f"{self.first_name} has max amount of rentals"
        # #check if family account
        if self._account_type in ["sf", "pf"] and video.rating == "R":
            return f"Account Restriction: {self.first_name} cannot rent R-rated movies."
        
        #show current rentals
        #print(f"Before rental: {self.current_video_rentals}")
        #rent video to customer
        if title in self._current_video_rentals:
            return f"{self.first_name} already has '{title}' rented."
        self._current_video_rentals.append(title)
        #update num of copies available
        video.copies_available -= 1
        #show current rentals 
        #print(f"After rental: {self._current_video_rentals}")
        #inform customer of update
        return f" {self.first_name} has successfully rented '{title}' ."
    
            
        
            

    #define return a video
    def return_a_video(self, video_title):

        #check current rentals
        #print(f"Before return: {self._current_video_rentals}")
        #check if title of movie is in customer rentals
        if video_title not in self._current_video_rentals:
            print(f"ERROR: {video_title} not found in {self._current_video_rentals}")  
            raise ValueError(f"{self.first_name} does not have '{video_title}' rented .")
        ##remove title from customer rentals to return
        self._current_video_rentals.remove(video_title)
        #verify return of video_title
        #print(f"After return: {self._current_video_rentals}")

        #updated num of copies available
        video = Video.videos.get(video_title)
        if video:
            video.copies_available += 1
        else:
            print(f"Warning: {video_title} not found in inventory.")

        return f"{self.first_name} has returned '{video_title}'."
    

        


# Customer.addCustomer()
# Customer.addCustomer()
# Customer.viewCustomer()
# Customer.deleteCustomer()
# Customer.viewCustomer()

 title, rating = video_title
        print(f"{self.first_name} is trying to rent '{title}' (Account Type: {self._account_type})")
        # Raise an error if family account tries to rent an R-rated movie
        if self._account_type in ["sf", "pf"] and rating == "R":
            raise ValueError(f" Account Restriction: {self.first_name} cannot rent R-rated movies.")


        #check inventory
        video = Video.videos.get(title)
        if not video:
            raise ValueError(f"Error: {title} is not available in our inventory.") 
            
        if video.copies_available < 1:
            raise ValueError(f"Sorry, {title} is currently out of stock.")  

    #  setting max rentals
        if self._account_type.lower() == "sx" or self._account_type.lower() == "sf":
            max_rentals = 1  # Standard accounts
        elif self._account_type.lower() == "px" or self._account_type.lower() == "pf":
            max_rentals = 3  # Premium accounts
        else:
            raise ValueError(f"Unknown account type: {self._account_type}")

        if len(self._current_video_rentals) >= max_rentals:
            raise ValueError(f" {self.first_name} has reached the rental limit ({max_rentals}).")

    
        print(f"Before rental: {self._current_video_rentals}") 

        if title in self._current_video_rentals:
            raise ValueError(f"{self.first_name} already has '{title}' rented.")

        self._current_video_rentals.append(title)
        video.copies_available -= 1

        print(f"After rental: {self._current_video_rentals}") 
        return f"{self.first_name} has successfully rented '{title}'."    
       

title, rating = video_title
        print(f"{self.first_name} is trying to rent '{title}' (Account Type: {self._account_type})")

    # Restrict R-rated movies for family accounts
        if self._account_type in ["sf", "pf"] and rating == "R":
            raise ValueError(f"Account Restriction: {self.first_name} cannot rent R-rated movies.")  # ✅ Raises error instead of returning

    # Check if movie exists
        video = Video.videos.get(title)
        if not video:
            raise ValueError(f"Error: {title} is not available in our inventory.")  # ✅ Raise error if movie doesn't exist

    # Check if copies are available
        if video.copies_available < 1:
            raise ValueError(f"Sorry, {title} is currently out of stock.")  # ✅ Raise error if out of stock

    # Enforce rental limits
        max_rentals = 1 if self._account_type in ["sx", "sf"] else 3
        if len(self._current_video_rentals) >= max_rentals:
            raise ValueError(f"{self.first_name} has reached the rental limit ({max_rentals}).")  # ✅ Raise error if limit exceeded

    # Prevent duplicate rentals
        if title in self._current_video_rentals:
            raise ValueError(f"{self.first_name} already has '{title}' rented.")  # ✅ Raise error if movie already rented

    # Rent the movie
        self._current_video_rentals.append(title)
        video.copies_available -= 1
        print(f"{self.first_name} successfully rented '{title}'.")