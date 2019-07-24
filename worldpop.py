from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.maps import World
from pygal.style import RotateStyle
import json 
#Function to return code for country
def return_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return 'none'

#call worldmap

filename = 'C:\Practice\data_visualalization\population_data.json'

#load data into list
with open(filename) as pop:
    data = json.load(pop)

#Print the 2010 population for each country
world_maps = {}
highest3 = {}
pop_list =[]
for pop_dict in data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = return_code(country_name)
        pop_list.append(population)
        #print(country_name+': ' + population+ '>>>'+ return_code(country_name))
        if code:
            world_maps[code] = population
        else:
            print('Error '+ country_name)
cc_pops1 = {}
cc_pops2 = {}
for cc, pop in world_maps.items():
    if pop <10000000:
        cc_pops1[cc] = pop
    else:
        cc_pops2[cc] = pop
wm = World()
wm_style = RotateStyle('#723ac3')
wm = World(style=wm_style)
wm.title = "World Population in 2010"
wm.add('World population', world_maps)
wm.add('Top 5 Most Populated', cc_pops1)
wm.add('toppp',cc_pops2)
wm.render_to_file('world_map.svg')
