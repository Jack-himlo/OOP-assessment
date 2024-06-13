from classes.store import Store
import pytest


def test_25_run_the_store_proper(monkeypatch):
    store = Store("Code Platoon")
    choices = [
        "aoidfnaserf",  # main menu should handle improper input
        "1",  # lists all inventory
        "2",  # starts viewing customer rented videos prompt
        "adpofihasedr",  # prompt should handle improper input
        "1",  # returns the rented videos for Monica
        "3",  # starts add a new customer prompts
        "aoidfjnasedfae",  # improper input will be passed
        "n",  # confirmation will be denied and prompt for first name will populate again
        "Daniel",  # this will be passed to first name prompt
        "y",  # will confirm the first name input
        "Vasquez",  # will be passed as last name prompt
        "y",  # will confirm the last name input
        "aieo9dfnaoeidf",  # account type prompt will receive improper input,
        "px",  # will be passed as the proper input for account type
        "4",  # starts the Rent a video prompt
        "7",  # will be passed as the input to grab the newly created member
        "aopidefnaopdif",  # improper input will be passed in for video selection
        "Deadpool",  # deadpool will be rented out by the newly created customer
        "5",  # starts the Return a video prompt
        "7",  # will grab our newly created member with the id of 7
        "Deadpool",  # will be the returned title
        "6" # will end the run_the_store program
    ]
    input_vals = iter(choices)
    monkeypatch.setattr("builtins.input", lambda _:next(input_vals))
    assert store.run_the_store() == "Thank you, please come again!"
