# Generate country_cmap.json
## Unique Colors for Each Country

import cartopy
import json
import distinctipy

# Natural Earth Data: https://www.naturalearthdata.com/

## Country Borders: 258 Countries (https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/)


shpfilename = cartopy.io.shapereader.natural_earth(resolution='10m',
												category='cultural',
												name='admin_0_countries')

## Read in Shapefile
reader = cartopy.io.shapereader.Reader(shpfilename)
countries = reader.records()

all_country_names = {}
colors = distinctipy.get_colors(258)
for i, country in enumerate(countries):
	all_country_names[country.attributes["GEOUNIT"]] = colors[i]

## Save as .json
with open("country_cmap.json", "w") as out_file:
	json.dump(all_country_names, out_file, indent=4, ensure_ascii=False, sort_keys=True)
