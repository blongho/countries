# Country codes, capital, population, area and continent of the world

## This is a small script for use to download country codes from [geonames.org](https://www.geonames.org/countries/)

This script downloads and extracts the country information and saves them in a json file

## System requirements
1. Python 3.5+
    - Get it from [python official download site](https://www.python.org/downloads/)
2. Python package manager `pip`. 
    - Get both python and pip for windows as described [here](https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation#pip-install)

3. BeautifulSoup (only possible if 1 and 2 are satisfied)
    - Get it with `python pip install beautifulsoup4`
    - For system-specific installs, check this [this stackoverflow answer](https://stackoverflow.com/questions/19957194/install-beautiful-soup-using-pip?answertab=votes#tab-top)


## Usage
1. Get your own copy by [forking the repository](https://github.com/blongho/countries/fork)
2. Clone or download your forked copy ```$ git clone https://github.com/your-user-name/countries.git ```
3. Change directory to countries ```$ cd countries ```

4. Download your data
```$ python3 countries.py```

That's it! You now have a file called `countries.json`. Open it in your favourite editor.

Sample data from `countries.json`
```json 
[
    {
        "id": "020",
        "alpha2": "AD",
        "alpha3": "AND",
        "name": "Andorra",
        "capital": "Andorra la Vella",
        "area": "468.0",
        "population": "84,000",
        "continent": "EU"
    },
    {
        "id": "784",
        "alpha2": "AE",
        "alpha3": "ARE",
        "name": "United Arab Emirates",
        "capital": "Abu Dhabi",
        "area": "82,880.0",
        "population": "4,975,593",
        "continent": "AS"
    },
    //...
]
```

This has been tested on Windows 10 with cygwin installed and used as the terminal.

It works too in Ubuntu 18.04 

If this does not work for your system for any reason, please feel free to [create an issue](https://github.com/blongho/countries/issues) 


## Contributions guidelines
All forms of contributions/criticism are welcome. It is only when i get critique that i will improve. 

Please give it a star if you like it or [create and issue](https://github.com/blongho/countries/issues) out if you dislike it. You can also suggest any cool feature a feature with a [pull request](https://github.com/blongho/countries/pulls).


## LICENSE
GNU General Public Licence 
See [LICENSE](LICENSE) and as specified in [Geonames Terms and Conditions](https://www.geonames.org/export/)

&copy;March 2019 [Bernard Che Longho](mailto:blongho02@gmail.com)
