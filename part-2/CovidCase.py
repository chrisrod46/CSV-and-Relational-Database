#!/usr/bin/env python3
#
# Christopher Rodriguez
# CPSC 223p-03
# 2020-11-12
# chrisrod46@csu.fullerton.edu
#

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base  = declarative_base()

class CovidCase(Base):
    __tablename__ = 'covid_cases'
    id = Column(Integer, primary_key=True)
    county = Column(String)
    state = Column(String)
    date = Column(Date)
    covid_cases = Column(Integer)
    deaths = Column(Integer)
    population = Column(Integer)

    def __init__(self, county, state, date, covid_cases, deaths, population):
        self.county = county
        self.state = state
        self.date = date
        self.covid_cases = covid_cases
        self.deaths = deaths
        self.population = population
    def __repr__(self):
        return 'CovidCase({}, {}, {}, {}, {}, {})'.format(repr(self.county),
        repr(self.state), repr(self.date), repr(self.covid_cases), repr(self.deaths),
        repr(self.population))
