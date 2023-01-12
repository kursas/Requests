#Parašykite programą, kuri iš adreso https://orai.15min.lt/prognozes
# ištrauktų ir atspausdintų oro prognozę Vilniuje šiuo metu.
# Galima naudoti str metodus, regex.

import requests
r = requests.get('https://orai.15min.lt/prognozes')
html = r.text
split_by_vilnius = html.split('Vilnius')
split_by_hot = split_by_vilnius[-1].split('hot">')
res = split_by_hot[1].split()[0]
print(res)

#output
+1°

Process finished with exit code 0
