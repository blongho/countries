#!/usr/bin/env python

"""
@brief  : A script to download the data in https://www.geonames.org/countries/
This is my attempt to practice webscrapping with python.
I also need this in building the library at
    https://github.com/blongho/world-country-flags


@author : blongho.
@since  : 2019-03-01.

@pre
- BeautifulSoup
    Get as described in
    https://stackoverflow.com/questions/19957194/install-beautiful-soup-using-pip?answertab=votes#tab-top

- cURL
    Get it from https://curl.haxx.se/download.html

- Basics of HTML5 && CSS3
    https://www.w3schools.com/html/default.asp
    https://www.w3schools.com/css/default.asp
"""
import os
from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request as requests
from src.country import Country
# ============================================================================
# ============================================================================
#   Default variables

# Directory listing all the countries of the world
directory = "https://www.geonames.org/countries/"

fileName = "countries.json"  # Default file name

# ============================================================================


def download(url=directory):
    """
    Download information from url and return the raw file as string.

    @param link The url containing country data
    @param doc  The file where the download will be saved

    @pre  cURL must be installed in the system
    """
    print("\n\n==>> Downloading files from {}".format(url))

    document = requests.urlopen(url).read().decode("utf8")

    print("==>> Download completed :)")
    return document

# ============================================================================
# Get the data


def extractInfo(websiteContent):
    """
    Extract the information from the downloaded site.

    @param doc The document {string} read from the downloaded file
    """
    print("==>> Extracting data data...")

    soup = BeautifulSoup(websiteContent, 'html.parser')
    table = soup.find("table", attrs={"id": "countries"})

    trList = table.find_all("tr")
    iso2 = iso3 = code = name = capital = area = pop = continent = None
    countries = []  # Container to hold all the countries

    for tr in trList:
        td = tr.find_all("td")
        for idx in td:
            iso2 = td[0].find(text=True)
            iso3 = td[1].find(text=True)
            code = td[2].find(text=True)
            name = td[4].find(text=True)
            capital = td[5].find(text=True)
            area = td[6].find(text=True)
            pop = td[7].find(text=True)
            continent = td[8].find(text=True)

        country = Country(code, iso2, iso3, name,
                          capital, area, pop, continent)

        # Save full continent name
        # c = Country(code, iso2, iso3, name, capital, area, pop, continent)

        if country.name is not None:  # Resist storing the table headers (th)
            countries.append(country)

    print("==>> Data extraction complete :)")
    return countries

# ============================================================================


def showExtractedInfo(countryList):
    """
    Display the extracted information to the user .

    @param  countryList The list of the countries extracted
    """
    # Sort by continent
    clearScreen()
    countryList.sort(key=lambda c: c.name, reverse=False)
    showInterval = 50
    print("\nYou will see {} items at a time\n".format(showInterval))

    idx = 1
    for c in countryList:
        print(str(idx) + ": ", end="")
        c.display()
        idx += 1
        if (idx % (showInterval + 1) == 0):
            proceed = input("\n==>Show more? (y/n): ")
            if (proceed[0].lower() == "y"):
                clearScreen()
                continue
            else:
                break

    print("\n")
# ============================================================================


def saveToJson(countryList, filename=fileName):
    """
    Save the country list as a json.

    @param  countryList The list of the countries to save
    @param  filename    The name of the json file

    """
    idx = 0
    countries = len(countryList)
    with open(fileName, 'w') as outfile:
        outfile.write("[")  # open array
        for c in countryList:
            outfile.write(c.toJson())
            idx += 1
            if (idx < countries):
                outfile.write(",\n")
            else:
                outfile.write("\n")

        outfile.write("]")  # close array
        outfile.close()  # clean up

    print("\n***********************\nCountries saved in ", end="")
    print(" {}\n*********************\n".format(filename))

# ============================================================================


def run():
    """
    Run the script.
    @pre : python3
    """
    clearScreen()
    startTime = datetime.now().second
    stringContent = download()
    countryList = extractInfo(stringContent)
    saveToJson(countryList)
    endTime = datetime.now().second
    showextract = input("Do you want to see the extracted data? (y/n): ")
    if (showextract[0].lower() == "y"):
        showExtractedInfo(countryList)
    else:
        pass

    total = round((endTime - startTime), 2)
    print("\nTotal time (download, extraction and saving to file): ", end="")
    print("{} seconds\n".format(total))
# ============================================================================


def clearScreen():
    """
    Clears the console output like "clear"
    """
    if (os.name == 'nt'):
        os.system("cls")
    else:
        os.system("clear")
# ============================================================================
