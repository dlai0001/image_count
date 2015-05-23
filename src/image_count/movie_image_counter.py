from image_count.implementation.movie_processor import MovieProcessor
from image_count.data.movie_data_access import MovieDataAccess


class MovieImageCounter(object):
    def __init__(self, api_key, data_access=None, image_counter=MovieProcessor()):
        self._api_key = api_key
        self._data_access = data_access or MovieDataAccess(api_key)
        self._image_counter = image_counter


    def get_image_counts(self):
        movie_data = self._data_access.get_in_theaters()
        results = self._image_counter.get_image_count(movie_data)

        return results
