from pygal.maps.world import COUNTRIES

# #kody dwuznakowe panstw
#
# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])

def get_country_code(contry_name):
    """zwraca dwuznakowy kod kraju stosowany przez pygal"""
    for code, name in COUNTRIES.items():
        if name == contry_name:
            return code
    return None