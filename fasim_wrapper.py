#!/usr/bin/env python3
from sys import argv
from os import system

"""
    This small wrapper is used to call fasim with input fastas as paths instead of files in the current
    directory.
    The script makes a symlink to the provided files into the current directory and calls fasim 
    on these.
    ! - The script does not clean up the symlinks after fasim has finished -
    it is meant to run on temporary containers.
"""

def make_link_return_filename(path):
    system(f"ln -s {path} {path.split('/')[-1]}")
    return path.split("/")[-1]

def main():
    args = argv[1:]
    try:
        indx = args.index('-f1')
        args[indx+1] = make_link_return_filename(args[indx+1])
    except ValueError as e:
        exit("Error: Missing -f1 argument")
    try:
        indx = args.index('-f2')
        args[indx+1] = make_link_return_filename(args[indx+1])
    except ValueError as e:
        exit("Error: Missing -f2 argument")

    new_args = " ".join(args)
    system(f"./usr/bin/fasim {new_args}")

if __name__ == '__main__':
    main()