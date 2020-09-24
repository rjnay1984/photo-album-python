from photo_album import request_album

"""
Test the length of the album, since it's
consistent in the placeholder API.
"""


def test_photo_album_success():
    album_request = request_album(4)
    assert len(album_request) == 50


def test_photo_album_unsuccessful():
    album_request = request_album(101)
    assert 'There are no photos in this album.' in str(album_request)
