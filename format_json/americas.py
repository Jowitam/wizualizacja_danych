from pygal.maps.world import World
# oznaczone kraje na mapie oraz ameryka polnocna z wielkoscia populacji
wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'Ameryka Północna, Środkowa, Południowa'
wm.add('Ameryka Północna', {'ca': 34126000, 'mx': 113423000, 'us': 309349000})
wm.add('Ameryka Środkowa', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('Ameryka Południowa', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
