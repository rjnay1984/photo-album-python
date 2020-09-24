import fire
import requests


def request_album(id):
    apiUrl = f'https://jsonplaceholder.typicode.com/photos?albumId={id}'
    resp = requests.get(apiUrl)
    photos = []
    if resp.status_code != 200:
        # This means something went wrong.
        raise Exception(f'GET /photos {resp.status_code}')

    # Print the id and title of each photo
    for photo in resp.json():
        photos.append(f"[{photo['id']}] {photo['title']}")

    if len(photos) < 1:
        return 'There are no photos in this album.'

    return photos


if __name__ == '__main__':
    fire.Fire(request_album)
