#https://cataas.com/cat kas kartą užkrauna vis
# skirtingą katės nuotrauką. Parašykite funkciją,
# kuriai į parametrus įrašius, kiek norime nuotraukų,
# išsaugotų jas mūsų kompiuteryje.

import requests
def cat_random(quant):
    for i in range(quant):
        url = "https://cataas.com/cat"
        response = requests.get(url)
        response.raise_for_status()
        filename = f'D:/DUMENYS/DARIUS/Desktop/cat{i}.jpg'
        with open(filename,'wb') as file:
            file.write(response.content)
cat_random(20)

#output
Process finished with exit code 0
