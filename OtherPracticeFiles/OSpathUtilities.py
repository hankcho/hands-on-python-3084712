import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    #  print the name of the OS
    print(os.name)

    # check for item existence type
    # print("item exists:", str(path.exists("practiceFiles")))
    print("item exists:", path.exists("practiceFiles"))
    print("itme is a file:", path.isfile("practiceFiles"))
    print("item is a directory:", path.isdir("practiceFiles"))

    print("item exists:", path.exists("textfile.txt"))
    print("itme is a file:", path.isfile("textfile.txt"))
    print("item is a directory:", path.isdir("textfile.txt"))

    # work with file paths
    print("item's path:", path.realpath("OSpathUtilities.py"))
    print("item's path and name:", path.split(
        path.realpath("OSpathUtilities.py")))

    # get the modicication time
    t = time.ctime(path.getmtime("textfile.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("hello.py")))

    # calculate how long ago the itme was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("hello.py"))
    print("it has been",td," since the file was modified")
    print("or, ",td.total_seconds(), "seconds")

if __name__ == "__main__":
    main()
