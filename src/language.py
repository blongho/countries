"""
@file   : language.py
@author : blongho
@since  : 2023-09-02
@brief  : A file holding a language object

This class is adapted to get the information from 
https://www.fincher.org/Utilities/CountryLanguageList.shtml   
"""
import json

class Language:
    """A class to hold a language object
    """
    def __init__(self, country:str, language:str, iso2:str, iso3:str, id:int) -> None:
        """The constructor of a language object

        Args:
            country (str): The full country name e.g Afghanistan
            language (str): The language name e.g Pashto
            iso2 (str): The language two letter representation, e.g ps-AF
            iso3 (str): The language three letter representation, e.g ps-AFG
            id (int): The lanauges lcid number
        """
        self.country = country
        self.country_alpha2 = str(iso2).split('-')[1] # eg ps-AF gives AF
        self.language = language
        self.iso2 = iso2
        self.iso3 = iso3
        self.id = int(id)

    def toJson(self):
        """
        Convert this object to json object
        """
        return json.dumps(self, default=vars, sort_keys=True, indent=4)
    
    def __str__(self) -> str:
        return "{} : name={}, iso2={}, iso3={}, countryName={}, countryAlpha2={}, languageNumber={}".format(__class__.__name__, self.language, self.iso2, self.iso3, self.country, self.country_alpha2, self.id)
