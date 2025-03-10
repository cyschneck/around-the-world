# Generate Cartopy Maps based on CMAP JSON
import matplotlib.pyplot as plt
import json
import cartopy

def generate_world_258_map(center_lon):
	# Generate world map for all 258 countries
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
		fig = plt.figure(figsize=(18, 18))
		ax = plt.axes(projection=cartopy.crs.PlateCarree(central_longitude=center_lon))
	
		if map_type == "empty":
			ax.add_feature(cartopy.feature.COASTLINE, linestyle="-")
	
		if map_type == "borders":
			ax.add_feature(cartopy.feature.BORDERS, linestyle="-",)
			ax.add_feature(cartopy.feature.COASTLINE, linestyle="-")

		if map_type == "color":
			for country in countries:
				red = country_cmap_dict[country.attributes["GEOUNIT"]]["RGB"][0]
				green = country_cmap_dict[country.attributes["GEOUNIT"]]["RGB"][1]
				blue = country_cmap_dict[country.attributes["GEOUNIT"]]["RGB"][2]
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

def generate_usa_map():
	# Generate USA map
	with open("states_cmap.json") as json_file:
		states_cmap_dict = json.load(json_file)
		# state_name: [Red, Green, Blue]	
	shpfilename = cartopy.io.shapereader.natural_earth(resolution='110m',
														category='cultural',
														name='admin_1_states_provinces')
	reader = cartopy.io.shapereader.Reader(shpfilename)
	states_shp = reader.records()

	projection_cartopy = cartopy.crs.PlateCarree(central_longitude=-106)

	# matplotlib
	fig = plt.figure(figsize=(18, 18))
	ax = plt.axes(projection=projection_cartopy)
	ax.set_extent([-125, -66.5, 20, 50], cartopy.crs.Geodetic())
	#ax.add_feature(cartopy.feature.COASTLINE, linestyle="-")
	#ax.add_feature(cartopy.feature.BORDERS, linestyle="-",)
	#ax.add_feature(cartopy.feature.STATES, linestyle="-",)

	# remove borders along graphs
	for spine in ax.spines:
		ax.spines[spine].set_color("None")

	#ax.background_patch.set_visible(False)
	#ax.outline_patch.set_visible(False)

	us_states = ["Alaska", "Alabama", "Arkansas",
			"Arizona", "California", "Colorado",
			"Connecticut", "Delaware", "Florida", 
			"Georgia", "Hawaii", "Iowa", "Idaho", 
			"Illinois", "Indiana", "Kansas", "Kentucky", 
			"Louisiana", "Massachusetts", "Maryland", 
			"Maine", "Michigan", "Minnesota",
			 "Missouri", "Mississippi", "Montana", 
			 "North Carolina", "North Dakota", "Nebraska", 
			 "New Hampshire", "New Jersey", "New Mexico", 
			 "Nevada", "New York", "Ohio", 
			 "Oklahoma", "Oregon", "Pennsylvania", 
			 "Rhode Island", "South Carolina", "South Dakota", 
			 "Tennessee", "Texas", "Utah", 
			 "Virginia", "Vermont", "Washington", 
			 "Wisconsin", "West Virginia", "Wyoming"]
	
	for state in states_shp:
		if state.attributes["name"] in us_states:
			red = states_cmap_dict[state.attributes["name"]][0]
			green = states_cmap_dict[state.attributes["name"]][1]
			blue = states_cmap_dict[state.attributes["name"]][2]
			ax.add_geometries([state.geometry],
								projection_cartopy,
								facecolor=(red, green, blue))

	plt.show()
	
if __name__=="__main__":
	center_longitudes = [0]
	for cent_lon in center_longitudes:
		generate_world_258_map(cent_lon)
	#generate_usa_map()
