# Generate Cartopy Maps based on CMAP JSON
import matplotlib.pyplot as plt
import json
import cartopy

def generate_world_258_map(center_lon):
	def generate_map(center_lon, map_type):
		# read in country_cmap.py
		with open("country_cmap.json") as json_file:
			country_cmap_dict = json.load(json_file)
			# Country_name: [Red, Green, Blue]

		shpfilename = cartopy.io.shapereader.natural_earth(resolution='10m',
														category='cultural',
														name='admin_0_countries')
		reader = cartopy.io.shapereader.Reader(shpfilename)
		countries = reader.records()

		# matplotlib
		fig = plt.figure(figsize=(10, 10))
		ax = plt.axes(projection=cartopy.crs.PlateCarree(central_longitude=center_lon))
	
		if map_type == "empty":
			ax.add_feature(cartopy.feature.COASTLINE, linestyle="-")
	
		if map_type == "borders":
			ax.add_feature(cartopy.feature.BORDERS, linestyle="-",)
			ax.add_feature(cartopy.feature.COASTLINE, linestyle="-")

		if map_type == "color":
			for country in countries:
				red = country_cmap_dict[country.attributes["GEOUNIT"]][0]
				green = country_cmap_dict[country.attributes["GEOUNIT"]][1]
				blue = country_cmap_dict[country.attributes["GEOUNIT"]][2]
				ax.add_geometries(country.geometry, cartopy.crs.PlateCarree(),
								facecolor=(red, green, blue))
		fig_name = f"maps/world_258_countries_center_long_{center_lon}_{map_type}"
		# remove borders along graphs
		for spine in ax.spines:
			ax.spines[spine].set_color("None")
		print(fig_name)
		print(fig_name+"_transparent")
		plt.savefig(fig_name+".png", dpi=500, bbox_inches="tight", pad_inches=0, transparent=False)
		plt.savefig(fig_name+"_transparent.png", dpi=500, bbox_inches="tight", pad_inches=0, transparent=True)
		plt.close()
	
	for type_of_map in ["empty", "borders", "color"]:
		generate_map(center_lon, type_of_map)

if __name__=="__main__":
	center_longitudes = list(range(0, 190, 10))
	#center_longitudes = [0] # testing
	for cent_lon in center_longitudes:
		generate_world_258_map(cent_lon)
