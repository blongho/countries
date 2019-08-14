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
    A country object to represent the alpha2, alpha3, numeric code, name, 
    population and continent.

    """

    def __init__(self, alpha2, alpha3, code, name, capital, area, population, continent):
        """
        The constructor for creating a new object
        """
        self.alpha2 = alpha2
        self.alpha3 = alpha3
        self.code = code
        self.name = name
        self.capital = capital
        self.area = area
        self.population = population
        self.continent = continent

    def __info(self):
        """ 
        String representation of the class
        """
        return "{} [name={} capital={} population={} code={} alpha2={} alpha3={} area={} continent={}]".format(__class__.__name__, self.name, self.capital, self.population, self.code, self.alpha2, self.alpha3, self.area, self.continent)

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
        return json.dumps(self, default=vars, sort_keys=True, indent=4)
