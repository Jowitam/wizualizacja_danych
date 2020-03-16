import json

from format_json.country_codes import get_country_code

# wczytywanie danych z format_json i wrzut ich na liste
filname = 'population_data.json'
with open(filname) as f:
    pop_data = json.load(f)

# wyswietlanie polulacji dla panstw w 2010r
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ": " + str(population))
        else:
            print("BŁĄD - " + country_name)
