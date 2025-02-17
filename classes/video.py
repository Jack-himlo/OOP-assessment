# Write your video Class here
import csv

class Video:
    videos = {}
    

    
    def __init__(self, id, title, rating, release_year, copies_available):
        self._id = int(id)
        self._title = title
        self._rating = rating
        self._release_year = int(release_year)
        self._copies_available = int(copies_available)
    
    #set attributes
    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def rating(self):
        return self._rating

    @property
    def release_year(self):
        return self._release_year

    @property
    def copies_available(self):
        return self._copies_available
    #set setter
    @copies_available.setter
    def copies_available(self,value):
        #ensure value is not negative
        if value < 0:
            raise ValueError ("Copiesavailable cannot be negative ")
        self._copies_available = value
    @classmethod 
    def load_data(cls, filename = "data/videos.csv"):
        try:
            with open("data/videos.csv") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    video = Video(
                            id = row["id"],
                            title = row["title"],
                            rating  = row["rating"],
                            release_year = int(row["release_year"]),
                            copies_available = int(row["copies_available"]),
                            )
                    cls.videos[video.title] = video
            print("Video data loaded successfully")
        except FileNotFoundError:
            print(f"Error: {filename} not found")