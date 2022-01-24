#!/usr/bin/env python3
# File name     : uri_safe.py
# Author        : Jules Bozouklian (@bozou_client)
# Date created  : 24/01/2022

import argparse

# import URI map
import uri_schemes
uri_map = uri_schemes.uri_map

####
def defang(url):
    str1 = url
    for key, value in uri_map.items():
        str1 = str1.replace(key, value)

    print(str1)

####
def rearm(url):
    str1 = url
    for key, value in uri_map.items():
        str1 = str1.replace(value, key)

    print(str1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--defang",  type=str, help="python3 uri_safe.py --defang 'http://exemple.com' ")
    parser.add_argument("--rearm", type=str, help="python3 uri_safe.py --rearm 'hXXp[:]//exmple[.]com' ")
    args = parser.parse_args()


    if args.defang:
        defang(args.defang)
    elif args.fang:
        rearm(args.rearm)


if __name__ == "__main__":
    main()
