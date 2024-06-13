# Write your video Class here
class Video:
    videos = {}

    def __init__(
        self, id: int, title: str, rating: str, release_year: int, copies_available: int
    ):
        self._id = id
        self._title = title
        self._rating = rating
        self.release_year = release_year
        self._copies_available = copies_available

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
    def copies_available(self):
        return self._copies_available

    @copies_available.setter
    def copies_available(self, val):
        if isinstance(val, int) and val >= 0:
            self._copies_available = val
        else:
            raise Exception("This attribute could only be set to an int")
        
    @classmethod
    def add_a_video(cls, video):
        if isinstance(video, Video):
            cls.videos[video.title] = video
            return f"{video.title} has been added to our inventory"
        raise Exception("This method will only accept an instance of the Video class")
        

    @classmethod
    def get_a_video_by_title(cls):
        def provide_title():
            title = input("Please provide the title you are looking for:\n")
            if title in cls.videos.keys():
                return title
            print(
                f"This title is not in our inventory. Please choose from the following:\n{', '.join(list(cls.videos.keys()))}"
            )
            return provide_title()

        video = cls.videos.get(provide_title())
        return video

    @classmethod
    def list_inventory(cls):
        for key, val in cls.videos.items():
            print(f"{val.title} has {val.copies_available} copies in stock.")
