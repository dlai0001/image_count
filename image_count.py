#!/usr/bin/env python
import argparse
import sys
import os
import pprint

parser = argparse.ArgumentParser()
parser.add_argument('-k','--key', help='Api Key', required=True)
args = parser.parse_args()

localSrcPath = os.path.join(os.path.dirname(__file__), "src")
sys.path.insert(0, localSrcPath)

from image_count.movie_image_counter import MovieImageCounter
movie_image_counter = MovieImageCounter(args.key)
result = movie_image_counter.get_image_counts()

printer = pprint.PrettyPrinter(indent=4)
printer.pprint(result)
