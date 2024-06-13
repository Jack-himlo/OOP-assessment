from classes.video import Video
import pytest

"""
- creates a video dictionary
- creates a video instance
- attempts to add a dictionary to Video.videos
- adds an instance of a video to Video.videos setting the title of the video as the key and the instance itself as the value
"""

def test_18_add_a_video():
  video_dict = {
    "id":1,
    "title":"Toy Story",
    "rating":"G",
    "release_year":1995,
    "copies_available":0
  }
  video_inst = Video(**video_dict)
  try:
    Video.add_a_video(video_dict)
  except:
    Video.add_a_video(video_inst)
    assert Video.videos == {"Toy Story":video_inst}
