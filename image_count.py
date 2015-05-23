#!/usr/bin/env python
import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('-k','--key', help='Api Key', required=True)
args = parser.parse_args()

localSrcPath = os.path.join(os.path.dirname(__file__), "src")
sys.path.insert(0, localSrcPath)

from image_count.movie_image_counter import MovieImageCounter
movie_image_counter = MovieImageCounter(args.key)
count = movie_image_counter.get_image_count()

print "Number of images counted for movies in theater: " + str(count)
