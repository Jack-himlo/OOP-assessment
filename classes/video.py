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
    #import csv using direct path
    @classmethod 
    def load_data(cls, filename= "../data/videos.csv"):
        try:
            with open(filename, mode="r", newline= '', encoding="utf-8" ) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    video = Video(
                            id = int(row["id"].strip()),
                            title = row["title"].strip(),
                            rating  = row["rating"].strip(),
                            release_year = int(row["release_year"].strip()),
                            copies_available = int(row["copies_available"].strip()),
                            )
                    cls.videos[video.title] = video
            print("Video data loaded successfully")
            print("Current Videos in inventory: ", list(cls.videos.keys()))
        except FileNotFoundError:
            print(f"Error: {filename} not found")
    #add a video
    @classmethod
    def add_a_video(cls,video):
        
        #check if video is a dict and decunstruct if it is 
        if isinstance(video, dict):
            video = Video(**video)
        #return typeerror if video is not in class Video
        if not isinstance(video, Video):
            raise TypeError("Only Video instances can be added")
        #store video in video dict by key of title
        cls.videos[video.title] = video
        #return success message
        return f"Video '{video.title}' has been added to inventory."
    #get video by title
    @classmethod
    def get_a_video_by_title(cls, title= None):
        
        #loop until valid title is found
        while True:
        #prompt user to enter title to search
            if title is None:
                title = input("Enter the title of the video: ")
            if not isinstance(title, str):
                raise TypeError("Title must be a string.")
        #format title
            title = title.strip()
        #search for video by title
            video = cls.videos.get(title)

            if video is not None:
                # raise ValueError(f"Error: '{title}' not found in inventory.")
                return video
            print(f"Error: '{title}' not found in inventory. Please try again")
            title = None


            



Video.load_data()