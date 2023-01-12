#parašykite funkciją, kuri į args priimtų url eilučių sąrašą
# ir grąžintų, kokį serverį naudoja svetainė.
# Atsakymas galėtų atrodyti maždaug taip:

import requests
def get_server_name(*args):
    print(f"{'URL':<25} {'Server':<15}")
    print(f"{'-' * 35:<35}")
    for i in args:
        item = requests.get(f"{i}")
        print(f"{item.url:<25} - {item.headers['Server']:<15}")


get_server_name('https://www.delfi.lt/', 'https://www.alfa.lt/', 'https://www.15min.lt/', 'https://www.lrytas.lt/',
                'http://www.google.com/')

#output
URL                       Server         
-----------------------------------
https://www.delfi.lt/     - DWS            
https://www.alfa.lt/      - nginx/1.14.0 (Ubuntu)
https://www.15min.lt/     - nginx          
https://www.lrytas.lt/    - openresty      
http://www.google.com/    - gws            

Process finished with exit code 0
