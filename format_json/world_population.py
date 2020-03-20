import json

from pygal.maps.world import World
from pygal.style import RotateStyle

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

# podzielenie panstw na trzy grupy ze wzgledu na wielkosc populacji
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
# wyswietlenie liczby panstw w poszczegolnych grupach
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.title = 'Populacja na świecie 2010'
wm.add('0-10 mln', cc_pops_1)
wm.add('10 mln - 1mld', cc_pops_2)
wm.add('> 1mld', cc_pops_3)
wm.render_to_file('world_population.svg')
