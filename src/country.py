#!/usr/bin/env python

"""
@file   : country.py
@author : blongho
@since  : 2019-03-01
@brief  : A file holding a country object

This class is adapted to get the information from 
https://www.geonames.org/countries/
"""

import json


class Country:
    """
    A country object to represent the iso2, iso3, numeric code, name, 
    population and continent.

    """

    def __init__(self, id, iso2, iso3, name, capital, area, population, continent):
        """
        The constructor for creating a new object
        """
        self.id = id
        self.alpha2 = iso2
        self.alpha3 = iso3
        self.name = name
        self.capital = capital
        self.area = area
        self.population = population
        self.continent = continent

    def __info(self):
        """ 
        String representation of the class
        """
        return "{} [name={} capital={} code={} alpha2={} alpha3={} population={} continent={}]".format(__class__.__name__, self.name, self.capital, self.id, self.alpha2, self.alpha3, self.population, self.continent)

    def display(self):
        """
        Display information about this country.
        """
        print(self.__info())

    def toJson(self):
        """
        Convert this object to json object
        inspired by 
        @see https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable/15538391#15538391
        """
        return json.dumps(self, default=vars, sort_keys=False, indent=4)
