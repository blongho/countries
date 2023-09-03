# -*- coding: utf-8 -*-
"""country_info_processor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/blongho/countries/blob/master/country_info_processor.ipynb
"""

import pandas as pd
import requests
import io
from src.country import Country
from src.extractworld import saveToJson
from src.extract_languages import get_languages
# The web url for country info
countryinfo_url = "https://download.geonames.org/export/dump/countryInfo.txt"

# The headers. Check the weburl above
country_data_cols = ['alpha2', 'alpha3', 'id', 'fips', 'name', 'capital', 'area',
                     'population', 'continent', 'tld', 'currency_code', 'currency_name', 'phone',
                     'Postal_Code_Format', 'Postal_Code_Regex', 'languages',
                     'geonameid', 'neighbours', 'EquivalentFipsCode']

print("Country data columns={}".format(country_data_cols))

# Get the text data from the url
text = requests.get(countryinfo_url).text

"""## Read the country data"""

# read the countries info
# There are some comments at the beginning of the file. After looking at it,
# 50 rows are skipped to avoid the comments cluttering the 'usefull' data
countries = pd.read_csv(io.StringIO(text), skiprows=50,
                        sep='\t', names=country_data_cols)

print(countries.head())

# Drop non-useful columns
countries = countries.drop(columns=['Postal_Code_Format', 'Postal_Code_Regex',
                           'geonameid', 'EquivalentFipsCode', 'fips', 'tld', 'currency_code', 'currency_name'])

print("Countries head")

print(countries.head())

languages = get_languages()
def get_full_language_name(language:str)->str:
    for lang in languages:
        if lang.iso2 == language or lang.iso2.split('-')[0] == language or lang.iso3.split('-')[0] == language:
            return lang.language
    return ""

country_list = []

for c in countries.itertuples(index=False, name='Country'):
    country_languages = []
    for lang in str(c.languages).split(","):
        if get_full_language_name(lang) != '':
            country_languages.append("{} ({})".format(get_full_language_name(lang), lang))
    country_list.append(
        Country(alpha2=c.alpha2,
                alpha3=c.alpha3,
                id=c.id,
                name=c.name,
                capital=c.capital,
                area=c.area,
                population=c.population,
                continent=c.continent,
                phone=c.phone,
                languages=country_languages,
                neighbours=c.neighbours
                )
    )

print(country_list[0])

def run():
    saveToJson(countryList= country_list, filename="countries.json")