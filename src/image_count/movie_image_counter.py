from image_count.utilities.count_image import CountImage
from image_count.data.movie_data_access import MovieDataAccess


class MovieImageCounter(object):
    def __init__(self, api_key, data_access=None, image_counter=CountImage()):
        self._api_key = api_key
        self._data_access = data_access or MovieDataAccess(api_key)
        self._image_counter = image_counter


    def get_image_count(self):
        movie_data = self._data_access.get_in_theaters()
        count = self._image_counter.get_image_count(movie_data)

        return count
