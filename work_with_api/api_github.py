import pygal
import requests
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def print_info_repo():
    """metoda pomocnicza"""
    print("Liczba zwroconych repozytoriów: ", len(repo_dicts))
    print("\nWybrane informacje o wszystkich repozytoriach:")
    for repo_dict in repo_dicts:
        print("Nazwa: ", repo_dict['name'])
        print("Właściciel: ", repo_dict['owner']['login'])
        print("Gwiazdki: ", repo_dict['stargazers_count'])
        print("Repozytorium: ", repo_dict['html_url'])
        print("Utworzone: ", repo_dict['created_at'])
        print("Uaktualnione: ", repo_dict['updated_at'])
        print("Opis: ", repo_dict['description'])


def pygal_my_config():
    """metoda tworzaca obiekt konfiguracyjny wykres"""
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000
    return my_config


# wywolanie API i zapis otrzymanej odpowiedzi - projekty github w pythonie - ilosc gwiazdek
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
req = requests.get(url)
print("Kod stanu:", req.status_code)
# odpowiedz z API w zmiennej
response_dict = req.json()
# # przetworzenie wynikow
# print(response_dict.keys())

# # przeanalizowanie pierwszego repozytorium
# repo_dict = repo_dicts[0]
# print("\nKlucze: ", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

print("Całkowita liczba repozytoriow: ", response_dict['total_count'])

# przetworzenie informacji o repozytoriach
repo_dicts = response_dict['items']
print_info_repo()
names, stars_description_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    stars_description = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url'],
    }
    stars_description_dicts.append(stars_description)

# utworzenie wizualizacji
my_style = LS('#336699', base_style=LCS)
my_config = pygal_my_config()
chart = pygal.Bar(my_config, style=my_style)
chart.force_uri_protocol = 'http'
chart.title = "Repozytoria z największą liczbą gwiazdek dla projetków w Pythonie w serwisie GitHub"
chart.x_labels = names

chart.add('', stars_description_dicts)
chart.render_to_file('python_repos.svg')
