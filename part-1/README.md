# CPSC 223p
##  CSV File to Relational Database

Write a program named `covid19_csv_to_rdb.py` which takes two arguments. The first argument is an input CSV data file and the second argument is the output relational database file. The program reads in the input CSV data file and and coverts it to a relational database using Python's [CSV reader](https://docs.python.org/3/library/csv.html) and [SQLAlchemy](https://www.sqlalchemy.org/). The file is a CSV file of the COVID-19 data as reported by the [John Hopkins Coronavirus Resource Center](https://coronavirus.jhu.edu/) that has been edited to only include data for Orange County, California. The full data set can be found online at [https://github.com/govex/COVID-19](https://github.com/govex/COVID-19).

Using SQLAlchemy means that you will need to define a class that uses the same types as SQLAlchemy and inherits from SQLAlchemy's class hierarchy. Use the SQLAlchemy [reference library](https://www.sqlalchemy.org/library.html#reference) and [tutorials](https://www.sqlalchemy.org/library.html#tutorials) to help you get started with SQLAlchemy.

The data in the file, `simplified_orange_county.csv`, has six columns. The column names are given in `header.txt`. They are:

1. Countyname
1. Statename
1. Date
1. Confirmed (COVID-19 cases)
1. Deaths
1. Population



