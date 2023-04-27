# Assessment 2: Object Oriented Programming + CSV Reading

## **Video Inventory Manager**

https://user-images.githubusercontent.com/105952966/234780739-8bdc9d56-4b44-46f2-b40d-ce5648975c38.mp4

## Important Grading Information

- You need to get a 75% or better to pass ie 19/26 tests. (You must pass all assessments in order to graduate Code Platoon's program.)
- If you fail the assessment, you have can retake it once to improve your score. For this assessment...
  - _5% penalty_: If you complete and submit the retake **within one week** of receiving your grade.
  - _10% penalty_: If you complete and submit the retake **by the start of week 12**. A retake for this assessment WILL NOT be accepted after this date.

## Rules / Process

- This test is fully open notes and open Google, but is not to be completed with the help of other students/individuals.

## Requirements

- This assessment should be completed using Python.
- This assessment will utilize a `pytest` test suite.

## Challenge

_Back in the day_, humans would actually leave their homes to go rent a physical video copy of movies (what a strange concept, right?). Blockbuster was the leading video rental company in this era. Today, there is only one Blockbuster location left which is located in Bend, Oregon. We are going to ask you to build a video inventory application for this Blockbuster!

Your Video Inventory Management application should manage the following data:

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
  - customer _by id_
  - each title should be listed separately (i.e. not displayed with slashes from the CSV file)
- Adding a new customer
  - you should not have an initial list of video rentals assigned to a newly created customer
  - can you prevent duplicate ids from existing?
- Renting a video out to a customer
  - video _by title_
  - customer _by id_
  - **IMPORTANT:** Customers should be limited based on their account type. Your application should enforce these limitations when attempting to rent a video!
- Returning a video from a customer
  - video _by title_
  - customer _by id_
- Exiting the application

Be sure to give careful consideration into what data structures & data types (including classes) you might need to use in your application logic.

Your menu should look like this:

```
== Welcome to Code Platoon Video! ==
1. View store video inventory
2. View customer rented videos
3. Add new customer
4. Rent video
5. Return video
6. Exit
```

## Classes Break Down

### **Customer**

#### Fields

| field                 | type              | example data           |
| --------------------- | ----------------- | ---------------------- |
| list_of_customers     | dict of Customers | {1: Customer(1)}       |
| id                    | int               | 1                      |
| account_type          | str               | ['sx', 'px','sf' 'pf'] |
| first_name            | str               | John                   |
| last_name             | str               | Bon                    |
| current_video_rentals | list of str's     | ['Up']                 |

#### Methods

| name                        | parameters     | returns                                                                                                                                                                                                              | endstate                                                                                                                                         |
| --------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| load_data                   | None           | None                                                                                                                                                                                                                 | dict of Customers will have all Customer instances from our CSV with `current_video_rentals` as a list of video titles.                          |
| get_an_instance             | None           | Customer                                                                                                                                                                                                             | Gets a Customer from the list_of_customers dict by id                                                                                            |
| return_a_video              | None           | {video_title} has been removed from your list of rentals, thank you!                                                                                                                                                 | A video is removed from the Customers current_video_rentals list and a Videos copies_avilable is increased                                       |
| rent_a_video                | None           | {video_title} has been added to your list of rentals, thank you! OR You either already hold this video or \nthis video is not covered by your current account type! OR This title doesn't match any videos in stock! | A video title is added to the Customer current_video_rentals list and a Videos copies_avilable is decreased                                      |
| construct_new_customer_dict | None           | {dict with all of Customer init fields}                                                                                                                                                                              | Returns a dict holding all of a new customers information as values and their corresponding fields as keys                                       |
| create_new_customer         | customer_dict  | "{customer['first_name']} has been added as a customer! \nCustomer ID: {new_customer.id}"                                                                                                                            | A new customer instance is created and added to the list_of_customers dict with the customers id as a key and the customer itself as a the value |
| view_customer_rented_videos | None           | Customer instance                                                                                                                                                                                                    | Displays a customers currently rented videos and then returns said customer for further actions                                                  |
| validate_video_rental       | Video Instance | True OR False                                                                                                                                                                                                        | Evaluates if a Customers meets the account type conditions to rent out a a video                                                                 |

### **Video**

#### Fields

| field            | type           | example data      |
| ---------------- | -------------- | ----------------- |
| list_of_videos   | list of Videos | [Video Object(1)] |
| id               | int            | 1                 |
| title            | str            | Up                |
| rating           | str            | PG                |
| release_year     | int            | 2014              |
| copies_available | int            | 1                 |

#### Methods

| name                      | parameters  | returns                                               | endstate                                                                                    |
| ------------------------- | ----------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| display_current_inventory | None        | None                                                  | Displays each video instance inside the list_of_videos                                      |
| load_data                 | None        | None                                                  | Will create and append a video instance from the inventory csv onto the list_of_videos list |
| get_an_instance           | video_title | Video instance                                        | Will grab a video instance from the list_of_videos by title                                 |
| return_a_video            | None        | {self.title} was successfully returned, thank you!    | A videos copies_available is increased                                                      |
| rent_a_video              | None        | {self.title} was successfully checked out, thank you! | A videos copies_available is decreased                                                      |

### **Media**

#### Fields

| field | type | example data |
| ----- | ---- | ------------ |
| id    | int  | 1            |

#### Abstract Class Methods

| name               | endstate                                                                                                                                                                      |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| load_data          | Both Video and Customer will utilize this method with Polymorphism to unpack their respective csv files                                                                       |
| get\_\_an_instance | Both Video and Customer will utilize this method with Polymorphism to get a specific instance by either title or id                                                           |
| return_a_video     | Both Video and Customer will utilize this method with Polymorphism to either remove a title from a customers current_video_rentals list and increase a videos copies_avilable |
| rent_a_video       | Both Video and Customer will utilize this method with Polymorphism to either add a title to a customers current_video_rentals list and decrease a videos copies_avilable      |

## Running Tests

This assignment provides a pytest testsuite that will be utilized to grade your assessment. 

**NOTE: This test suite is a copy of the test suite utilized by GITHUB actions altering it will not help you**

To run the test suite run the following:

```bash
 pytest tests.py -v
```