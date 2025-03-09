# Generate states_cmap.json
## Unique Colors for Each State in the US

import json
import distinctipy

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

all_state_names = {}
colors = distinctipy.get_colors(51)
for i, state in enumerate(us_states):
	all_state_names[state] = colors[i]

## Save as .json
with open("states_cmap.json", "w") as out_file:
	json.dump(all_state_names, out_file, indent=4, ensure_ascii=False, sort_keys=True)
