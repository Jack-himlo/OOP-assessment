from classes.video import Video
import pytest

"""
- Ensure all properties belonging to the Video class exist
"""

def test_16_video_properties():
  video = Video(**{
    "id":1,
    "title":"Toy Story",
    "rating":"G",
    "release_year":1995,
    "copies_available":0
  })
  assert hasattr(video, 'id')
  assert isinstance(video.id, int)

  assert hasattr(video, 'title')
  assert isinstance(video.title, str)

  assert hasattr(video, 'rating')
  assert isinstance(video.rating, str)

  assert hasattr(video, 'copies_available')
  assert isinstance(video.copies_available, int)