import csv


class Video:
    videos = {}

    def __init__(self, id, title, rating, release_year, copies_available):
        self._id = id
        self._title = title
        self._rating = rating
        self._release_year = release_year
        self._copies_available = copies_available

    @property
    def title(self):
        return self._title

    @property
    def id(self):
        return self._id

    @property
    def rating(self):
        return self._rating

    @property
    def copies_available(self):
        return self._copies_available

    @copies_available.setter
    def rent_a_video(self, count):
        if count > 0:
            self._copies_available = count
        else:
            print("This video is out of stock!")

    @copies_available.setter
    def return_a_video(self, count):
        self._copies_available = count

    def __str__(self):
        return f"Title: {self.title} | Copies: {self.copies_available}"

    @classmethod
    def get_a_video_by_title(cls):
        title = input("Enter the title of the video:    ")
        if title in cls.videos:
            return cls.videos.get(title)
        else:
            print("This title does not exist")
            return cls.get_a_video_by_title()

    @classmethod
    def list_inventory(cls):
        for idx, video in enumerate(list(cls.videos.values())):
            print(f"{idx+1} {video}")
