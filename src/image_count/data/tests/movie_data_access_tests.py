# from image_count.data.movie_data_access import MovieDataAccess
from nose.plugins.attrib import attr
from unittest2 import skip
import unittest2
from image_count.data.movie_data_access import MovieDataAccess


class MovieDataAccessTests(unittest2.TestCase):

    def test_get_in_theaters_fetch_list_of_movies(self):
        api_key = "fake"
        mock_response = [mock_response_with_2_movies, ""]
        sut = MovieDataAccess(api_key, page_size=5, request_lib=MockRequest(mock_response))
        actual = sut.get_in_theaters()

        self.assertEqual(len(actual), 2)
        self.assertEqual(actual[0]['title'], 'Mad Max: Fury Road')
        self.assertEqual(actual[1]['title'], 'Incredibles')

    def test_get_in_theaters_handles_pagination(self):
        api_key = "fake"
        mock_response = [mock_response1, mock_response2, ""]
        sut = MovieDataAccess(api_key, page_size=1, request_lib=MockRequest(mock_response))
        actual = sut.get_in_theaters()

        self.assertEqual(len(actual), 2)
        self.assertEqual(actual[0]['title'], 'Mad Max: Fury Road')
        self.assertEqual(actual[1]['title'], 'Incredibles')

    @skip("not yet implemented")
    def test_should_throw_if_api_unavailable(self):
        self.fail("not yet implemented")

    @skip("not yet implemented")
    def test_should_throw_if_api_timeout(self):
        self.fail("not yet implemented")



class MockRequest(object):
    def __init__(self, responses):
        self.responses = responses

    def get(self, url, params):
        self.last_params = params

        item = self.responses[0]
        self.responses = self.responses[1:-1]

        return_val = object()
        return_val = lambda: None
        setattr(return_val, 'content', item)
        return return_val


mock_response1 = """
{
                "total": 2,
                "movies": [
                    {
                        "id": "771028170",
                        "title": "Mad Max: Fury Road",
                        "year": 2015,
                        "mpaa_rating": "R",
                        "runtime": 120,
                        "critics_consensus": "",
                        "release_dates": {
                            "theater": "2015-05-15"
                        },
                        "ratings": {
                            "critics_rating": "Certified Fresh",
                            "critics_score": 98,
                            "audience_rating": "Upright",
                            "audience_score": 92
                        },
                        "synopsis": "Filmmaker George Miller gears up for another post-apocalyptic action adventure with Fury Road, the fourth outing in the Mad Max film series. Charlize Theron stars alongside Tom Hardy (Bronson), with Zoe Kravitz, Adelaide Clemens, and Rosie Huntington Whiteley heading up the supporting cast. ~ Jeremy Wheeler, Rovi",
                        "posters": {
                            "thumbnail": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg",
                            "profile": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg",
                            "detailed": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg",
                            "original": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg"
                        },
                        "abridged_cast": [
                            {
                                "name": "Tom Hardy",
                                "id": "391527059",
                                "characters": [
                                    "Max Rockatansky"
                                ]
                            },
                            {
                                "name": "Charlize Theron",
                                "id": "162654733",
                                "characters": [
                                    "Imperator Furiosa"
                                ]
                            },
                            {
                                "name": "Nicholas Hoult",
                                "id": "162654938",
                                "characters": [
                                    "Nux"
                                ]
                            },
                            {
                                "name": "Rosie Huntington-Whiteley",
                                "id": "771075959",
                                "characters": [
                                    "Splendid"
                                ]
                            },
                            {
                                "name": "Zoe Kravitz",
                                "id": "771460102",
                                "characters": [
                                    "Five Wives"
                                ]
                            }
                        ],
                        "alternate_ids": {
                            "imdb": "1392190"
                        },
                        "links": {
                            "self": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170.json",
                            "alternate": "http://www.rottentomatoes.com/m/mad_max_fury_road/",
                            "cast": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170/cast.json",
                            "reviews": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170/reviews.json",
                            "similar": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170/similar.json"
                        }
                    }
                ],
                "links": {
                    "self": "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?page_limit=1&country=us&page=1",
                    "next": "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?page_limit=1&country=us&page=2",
                    "alternate": "http://www.rottentomatoes.com/movie/in_theaters"
                },
                "link_template": "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?page_limit={results_per_page}&page={page_number}&country={country-code}"
            }
"""

mock_response2 = """
            {
                "total": 2,
                "movies": [
                    {
                        "id": "771028470",
                        "title": "Incredibles",
                        "year": 2015,
                        "mpaa_rating": "R",
                        "runtime": 120,
                        "critics_consensus": "",
                        "release_dates": {
                            "theater": "2015-05-15"
                        },
                        "ratings": {
                            "critics_rating": "Certified Fresh",
                            "critics_score": 98,
                            "audience_rating": "Upright",
                            "audience_score": 92
                        },
                        "synopsis": "Filmmaker George Miller gears up for another post-apocalyptic action adventure with Fury Road, the fourth outing in the Mad Max film series. Charlize Theron stars alongside Tom Hardy (Bronson), with Zoe Kravitz, Adelaide Clemens, and Rosie Huntington Whiteley heading up the supporting cast. ~ Jeremy Wheeler, Rovi",
                        "posters": {
                            "thumbnail": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg",
                            "profile": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg",
                            "detailed": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg",
                            "original": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg"
                        },
                        "abridged_cast": [
                            {
                                "name": "Tom Hardy",
                                "id": "391527059",
                                "characters": [
                                    "Max Rockatansky"
                                ]
                            },
                            {
                                "name": "Charlize Theron",
                                "id": "162654733",
                                "characters": [
                                    "Imperator Furiosa"
                                ]
                            },
                            {
                                "name": "Nicholas Hoult",
                                "id": "162654938",
                                "characters": [
                                    "Nux"
                                ]
                            },
                            {
                                "name": "Rosie Huntington-Whiteley",
                                "id": "771075959",
                                "characters": [
                                    "Splendid"
                                ]
                            },
                            {
                                "name": "Zoe Kravitz",
                                "id": "771460102",
                                "characters": [
                                    "Five Wives"
                                ]
                            }
                        ],
                        "alternate_ids": {
                            "imdb": "1392190"
                        },
                        "links": {
                            "self": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170.json",
                            "alternate": "http://www.rottentomatoes.com/m/mad_max_fury_road/",
                            "cast": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170/cast.json",
                            "reviews": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170/reviews.json",
                            "similar": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170/similar.json"
                        }
                    }
                ],
                "links": {
                    "self": "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?page_limit=1&country=us&page=1",
                    "next": "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?page_limit=1&country=us&page=2",
                    "alternate": "http://www.rottentomatoes.com/movie/in_theaters"
                },
                "link_template": "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?page_limit={results_per_page}&page={page_number}&country={country-code}"
            }
"""

mock_response_with_2_movies = """
            {
                "total": 2,
                "movies": [
                    {
                        "id": "771028170",
                        "title": "Mad Max: Fury Road",
                        "year": 2015,
                        "mpaa_rating": "R",
                        "runtime": 120,
                        "critics_consensus": "",
                        "release_dates": {
                            "theater": "2015-05-15"
                        },
                        "ratings": {
                            "critics_rating": "Certified Fresh",
                            "critics_score": 98,
                            "audience_rating": "Upright",
                            "audience_score": 92
                        },
                        "synopsis": "Filmmaker George Miller gears up for another post-apocalyptic action adventure with Fury Road, the fourth outing in the Mad Max film series. Charlize Theron stars alongside Tom Hardy (Bronson), with Zoe Kravitz, Adelaide Clemens, and Rosie Huntington Whiteley heading up the supporting cast. ~ Jeremy Wheeler, Rovi",
                        "posters": {
                            "thumbnail": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg",
                            "profile": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg",
                            "detailed": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg",
                            "original": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg"
                        },
                        "abridged_cast": [
                            {
                                "name": "Tom Hardy",
                                "id": "391527059",
                                "characters": [
                                    "Max Rockatansky"
                                ]
                            },
                            {
                                "name": "Charlize Theron",
                                "id": "162654733",
                                "characters": [
                                    "Imperator Furiosa"
                                ]
                            },
                            {
                                "name": "Nicholas Hoult",
                                "id": "162654938",
                                "characters": [
                                    "Nux"
                                ]
                            },
                            {
                                "name": "Rosie Huntington-Whiteley",
                                "id": "771075959",
                                "characters": [
                                    "Splendid"
                                ]
                            },
                            {
                                "name": "Zoe Kravitz",
                                "id": "771460102",
                                "characters": [
                                    "Five Wives"
                                ]
                            }
                        ],
                        "alternate_ids": {
                            "imdb": "1392190"
                        },
                        "links": {
                            "self": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170.json",
                            "alternate": "http://www.rottentomatoes.com/m/mad_max_fury_road/",
                            "cast": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170/cast.json",
                            "reviews": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170/reviews.json",
                            "similar": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170/similar.json"
                        }
                    },
                    {
                        "id": "771028170",
                        "title": "Incredibles",
                        "year": 2015,
                        "mpaa_rating": "R",
                        "runtime": 120,
                        "critics_consensus": "",
                        "release_dates": {
                            "theater": "2015-05-15"
                        },
                        "ratings": {
                            "critics_rating": "Certified Fresh",
                            "critics_score": 98,
                            "audience_rating": "Upright",
                            "audience_score": 92
                        },
                        "synopsis": "Filmmaker George Miller gears up for another post-apocalyptic action adventure with Fury Road, the fourth outing in the Mad Max film series. Charlize Theron stars alongside Tom Hardy (Bronson), with Zoe Kravitz, Adelaide Clemens, and Rosie Huntington Whiteley heading up the supporting cast. ~ Jeremy Wheeler, Rovi",
                        "posters": {
                            "thumbnail": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg",
                            "profile": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg",
                            "detailed": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg",
                            "original": "http://resizing.flixster.com/fYBKxclWsYLoJy9l5Oa2632NMNM=/54x80/dkpu1ddg7pbsk.cloudfront.net/movie/11/19/12/11191276_ori.jpg"
                        },
                        "abridged_cast": [
                            {
                                "name": "Tom Hardy",
                                "id": "391527059",
                                "characters": [
                                    "Max Rockatansky"
                                ]
                            },
                            {
                                "name": "Charlize Theron",
                                "id": "162654733",
                                "characters": [
                                    "Imperator Furiosa"
                                ]
                            },
                            {
                                "name": "Nicholas Hoult",
                                "id": "162654938",
                                "characters": [
                                    "Nux"
                                ]
                            },
                            {
                                "name": "Rosie Huntington-Whiteley",
                                "id": "771075959",
                                "characters": [
                                    "Splendid"
                                ]
                            },
                            {
                                "name": "Zoe Kravitz",
                                "id": "771460102",
                                "characters": [
                                    "Five Wives"
                                ]
                            }
                        ],
                        "alternate_ids": {
                            "imdb": "1392190"
                        },
                        "links": {
                            "self": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170.json",
                            "alternate": "http://www.rottentomatoes.com/m/mad_max_fury_road/",
                            "cast": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170/cast.json",
                            "reviews": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170/reviews.json",
                            "similar": "http://api.rottentomatoes.com/api/public/v1.0/movies/771028170/similar.json"
                        }
                    }
                ],
                "links": {
                    "self": "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?page_limit=1&country=us&page=1",
                    "next": "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?page_limit=1&country=us&page=2",
                    "alternate": "http://www.rottentomatoes.com/movie/in_theaters"
                },
                "link_template": "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?page_limit={results_per_page}&page={page_number}&country={country-code}"
            }
"""
