# from injector import Module, Key, provides, Injector, inject, singleton
import requests
import json

class MovieDataAccess(object):

    API_URL = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json"
    DEFAULT_PAGE_SIZE = 50

    def __init__(self, api_key, page_size=10, request_lib=requests):
        self._request_lib = request_lib
        self.api_key = api_key
        self.page_size = page_size

    def get_in_theaters(self):
        count = 1
        total = 9999999

        movies = []

        while count <= total:
            params = {
                'apikey': self.api_key,
                'page': count,
                'page_limit': self.DEFAULT_PAGE_SIZE
            }
            response = json.loads(self._request_lib.get(self.API_URL, params).content)

            if response['total'] < total:
                total = response['total']

            count += len(response['movies'])
            for movie in response['movies']:
                movies.append(movie)

        return movies
