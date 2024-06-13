from classes.video import Video
import pytest

"""
- creates a video instance
- adds an instance of a video to Video.videos setting the title of the video as the key and the instance itself as the value
- utilizes monkeypatch to mimick user input
- get_a_video_by_title should handle proper and improper input and return the correct instance
"""

def test_18_add_a_video(monkeypatch):
  video_inst = Video(**{
    "id":1,
    "title":"Toy Story",
    "rating":"G",
    "release_year":1995,
    "copies_available":0
  })
  input_vals = iter(["aoidfhawsidef","Toy Story"])
  Video.add_a_video(video_inst)
  monkeypatch.setattr("builtins.input", lambda _:next(input_vals))
  assert Video.get_a_video_by_title() == video_inst