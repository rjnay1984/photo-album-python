from photo_album import request_album

"""
Test the length of the album, since it's
consistent in the placeholder API.
"""


def test_photo_album():
    album_request = request_album(4)
    print(album_request)
    assert len(album_request) == 50
