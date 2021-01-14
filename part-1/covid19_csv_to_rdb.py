#!/usr/bin/env python3
#
# Christopher Rodriguez
# CPSC 223p-03
# 2020-11-12
# chrisrod46@csu.fullerton.edu
#
"""This program will take in data from a csv file and put that data
into a database"""

import sys
import csv
from CovidCase import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import date

def main():
    """This is main it will take in a csv file and put the data into
    relational database"""

    if len(sys.argv) < 3:
        print("Please enter two files")
        exit(1)

    engine = create_engine('sqlite:///' + sys.argv[2])
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind = engine)
    this_session = Session()


    file = sys.argv[1]
    # reading csv file
    with open(file, 'r') as fh:
        reader = csv.reader(fh)
        for i in reader:
            year, month, day = map(int, i[2].split('-'))
            c =CovidCase(i[0], i[1], date(year, month, day), int(i[3]),
            int(i[4]), int(i[5]))
            this_session.add(c)
        this_session.commit()
        this_session.close()


if __name__ == "__main__":
    main()
