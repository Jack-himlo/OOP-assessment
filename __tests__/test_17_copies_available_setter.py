from classes.video import Video
import pytest

"""
- creates a video
- copies available will be set to a string but fail
- copies_available will be set to a negative number but fail
- copies_available will be set to a positive integer
"""

def test_17_copies_available_setter():
  video = Video(**{
    "id":1,
    "title":"Toy Story",
    "rating":"G",
    "release_year":1995,
    "copies_available":0
  })
  try:
    video.copies_available = "-2"
  except:
    try:
      video.copies_available = -2
    except:
      video.copies_available = 2
  assert video.copies_available == 2