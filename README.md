# **Assessment 1: Object Oriented Programming + CSV Reading**

## Important Grading Information

- You need to get a 70% or better to pass ie 18/25 tests. (You must pass all assessments in order to graduate Code Platoon's program.)
- If you fail the assessment, you have can retake it once to improve your score. For this assessment...
  - _5% penalty_: If you complete and submit the retake **within one week** of receiving your grade.
  - _10% penalty_: If you complete and submit the retake **by the start of week 12**. A retake for this assessment WILL NOT be accepted after this date.

## Requirements

- This assessment should be completed using Python Object Oriented Programming.
- This assessment will utilize a `pytest` test suite.
- Install all dependencies by running

```bash
pip install -r requirements.txt #if this fails run `pip3 install -r requirements.txt'
```

### Rules / Process

- This test is fully open notes and open Google, but is not to be completed with the help of other students/individuals.

## Challenge

_Back in the day_, humans would actually leave their homes to go rent a physical video copy of movies (what a strange concept, right?). Blockbuster was the leading video rental company in this era. Today, there is only one Blockbuster location left which is located in Bend, Oregon. We are going to ask you to build a video inventory application for this Blockbuster!

Your Video Inventory Management application should manage the following data:

- Load cutomer and video inventory data from the csv files provided
- Manage customer information:
  - customer id
  - customer account type (sx/px/sf/pf)
    - "sx" = standard account: max 1 rental out at a time
    - "px" = premium account: max 3 rentals out at a time
    - "sf" = standard family account: max 1 rental out at a time AND can not rent any "R" rated movies
    - "pf" = premium family account: max 3 rentals out at a time AND can not rent any "R" rated movies
  - customer first name
  - customer last name
  - current list of video rentals (_by title_), each title separated by a forward slash "/"
- Manage the store's video inventory:
  - video id
  - video title
  - video rating
  - video release year
  - number of copies currently available in-store

Your application should allow:

- Viewing the current video inventory for the store
- Viewing a customer's current rented videos
  - Get a customer _by id_
  - Display a list of currently rented titles
- Adding a new customer
  - You should not have an initial list of video rentals assigned to a newly created customer
  - No duplicate ID's
- Renting a video out to a customer
  - Get video _by title_
  - Decrement video copies
- Returning a video from a customer
  - Get video _by title_
  - Increment video copies
- Exiting the application
- **IMPORTANT:** Customers should be limited based on their account type. Your application should enforce these limitations when attempting to rent a video!

Be sure to give careful consideration into what data structures & data types (including classes) you might need to use in your application logic.

Your menu should look like this:

```bash
== Welcome to Code Platoon Video! ==
1. View store video inventory
2. View customer rented videos
3. Add new customer
4. Rent video
5. Return video
6. Exit
```

## Class Breakdown

### Customer

Attributes

| attribute            | type           | example data      | cls or inst |
| ---------------- | -------------- | ----------------- | --- |
| customers   | dict | {1: Customer(1)}  | cls |
| _id               | int            | 1                 | inst |
| first_name           | str            | John          | inst |
| last_name           | str            | Brawn           | inst |
| _account_type    | str           | sx             | inst |
| _current_video_rentals | list           | ['Toy Story'] | inst |

> Every newly created Customer should have at minimum an empty list for `_current_video_rentals`

Getters and Setters

| property     | type   | parent | input |
|--------------|--------|-------|----|
| id           | getter | _id | N/A   |
| current_video_rentals| getter | _current_video_rentals| N/A |
| current_video_rentals| setter | _current_video_rentals| list |

> current_video_rentals setter should only accept a list of video titles, if it is not a list type the setter should raise an exception with the following text: 'Current Video Rentals should only be a list'

Methods

| methods            | return type    | example return  | cls or inst | input |
| ---------------- | -------------- | ----------------- | --- | ---- |
| create_a_customer_dict  | dict   | {'id':7,'first_name':str, 'last_name':str, 'account_type':str}| static | N/A |
| add_a_customer | str | f"{customer.first_name} has been added into our database!"| cls | Customer(1) |
| get_customer_by_id | Customer Class inst | Customer(1) | cls | N/A |
| get_customer_rented_videos   | str | f"{self.first_name} has the following rentals:\n{self.current_video_rentals}" | inst | N/A|
| rent_a_video | str | f"{self.first_name} has the following rentals:\n{self.current_video_rentals}" | inst|("Toy Story", "G")|
| return_a_video | str | f"{self.first_name} has the following rentals:\n{self.current_video_rentals}" |inst| "Toy Story" |

### Customer_pf

- Inherits all attributes and methods from the `Customer` class
- Overrides `rent_a_video` method to meet account conditions

### Customer_sf

- Inherits all attributes and methods from the `Customer` class
- Overrides `rent_a_video` method to meet account conditions

### Customer_sx

- Inherits all attributes and methods from the `Customer` class
- Overrides `rent_a_video` method to meet account conditions

### Customer_px

- Inherits all attributes and methods from the `Customer` class
- Utilizes inherited `rent_a_video` method that already meets account conditions

### Video

Attributes

| attribute            | type           | example data      | cls or inst |
| ---------------- | -------------- | ----------------- | --- |
| videos   | dict | {"Toy Story":Video Object(1),} | cls |
| _id               | int            | 1                 | inst |
| _title            | str            | Up                | inst |
| _rating           | str            | PG                | inst |
| release_year     | int            | 2014              | inst |
| _copies_available | int            | 1                 | inst |

Getters and Setters

| property     | type   | parent | input |
|--------------|--------|-------|----|
| id           | getter | _id | N/A   |
| title          | getter | _title | N/A   |
| rating           | getter | _rating | N/A   |
| copies_available | getter | _copies_available | N/A   |
| copies_available | setter | _copies_available|int|

Methods

| methods            | type           | example return  | cls or inst | input |
| ---------------- | -------------- | ----------------- | --- | ---- |
| get_a_video_by_title | Video Class inst | Video Object(1) | cls | N/A|
| list_inventory| None | Prints each videos _str | cls | N/A |

## Store

Attributes

| attribute            | type           | example data      | cls or inst |
| ---------------- | -------------- | ----------------- | --- |
| name   | str | Code Platoon | inst |

Methods

| methods            | type           | input | example return  | cls or inst |
| ---------------- | -------------- | ------|----------- | --- |
| customer_type_maker | Customer Class inst | {'id':7,'first_name':str, 'last_name':str, 'account_type':str}| Customer Object(1) | inst |
| load_data| None | file name i.e. videos or customers | None| inst |
| run_the_store | str | None |Thank you, please come again!| inst |

> `load_data` should build the dictionaries of Video.videos and Customer.customers with the proper information from the correct csv file upon an instance of the Store class.
