from classes.video import Video
import pytest

"""
- Ensure all attributes belonging to the Video class exist
"""

def test_15_video_attributes():
  video = Video(**{
    "id":1,
    "title":"Toy Story",
    "rating":"G",
    "release_year":1995,
    "copies_available":0
  })
  assert hasattr(video, '_id')
  assert hasattr(video, '_title')
  assert hasattr(video, '_rating')
  assert hasattr(video, 'release_year')
  assert hasattr(video, '_copies_available')