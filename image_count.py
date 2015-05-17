#!/usr/bin/env python

# TODO: implement this

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-k','--key', help='Api Key', required=True)
args = parser.parse_args()


# TODO
print("api key used: " + args.key)
print("Nothing to see here, come back when this program is done.")