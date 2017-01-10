#!/usr/bin/python

import sys
from src.controller import HotelInfiniteRooms


def main(argv):
    hir = HotelInfiniteRooms()
    print "Size    : " + str(hir.membres_day(int(sys.argv[1]), int(sys.argv[2])))
    #print "Size res: " + str(hir.membres_day_res(int(sys.argv[1]), int(sys.argv[2]),int(sys.argv[1]) ))

if __name__ == "__main__":
   main(sys.argv[1:])