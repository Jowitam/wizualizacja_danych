import json

from pygal.maps.world import World
from format_json.country_codes import get_country_code

# wczytywanie danych z format_json i wrzut ich na liste
filname = 'population_data.json'
with open(filname) as f:
    pop_data = json.load(f)

# utworzenie slownika danych dotyczacych populacji
cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_population[code] = population
        else:
            print("BŁĄD - " + country_name)

wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'Populacja na świecie 2010'
wm.add('2010', cc_population)
wm.render_to_file('world_population.svg')
