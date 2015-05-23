from image_count.utilities.count_image import CountImage
from nose.plugins.attrib import attr
import unittest2
import json


class CountingImageTests(unittest2.TestCase):

    def test_count_returns_correct_image_count(self):
        sut = CountImage()

        movies = json.loads(movie_entries)

        actual = sut.get_image_count(movies)
        self.assertEqual(actual, 8)

    def test_count_returns_zero_if_no_images(self):
        sut = CountImage()

        movies = json.loads(movie_entries_no_images)

        actual = sut.get_image_count(movies)
        self.assertEqual(actual, 0)

    def test_count_returns_zero_if_no_movies(self):
        sut = CountImage()

        movies = []

        actual = sut.get_image_count(movies)
        self.assertEqual(actual, 0)


movie_entries = """
            [
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
                ]
"""

movie_entries_no_images = """
            [
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
                            "thumbnail": null,
                            "profile": null,
                            "detailed": null,
                            "original": null
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
                            "thumbnail": null,
                            "profile": null,
                            "detailed": null,
                            "original": null
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
                ]
"""