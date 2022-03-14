import csv
from random import choice
city = dict()
cities_only = []
country = dict()
# first_letters = {'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ё': 0, 'ж': 0, 'з': 0, 'и': 0, 'й': 0,
#                               'к': 0, 'л': 0, 'м': 0, 'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0, 'т': 0, 'у': 0, 'ф': 0,
#                               'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0, 'ю': 0, 'я': 0}
# all_cities = ''


with open('cities/city.csv', encoding='utf-8') as cities:
    reader = csv.reader(cities, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index % 2 == 0:
            continue
        city[f'{row[-1]}'] = f'{row[1]}'
        cities_only.append(row[-1])
print(cities_only)

with open('cities/country.csv', encoding='utf-8') as countries:
    reader = csv.reader(countries, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index % 2 == 0:
            continue
        country[f'{row[0]}'] = f'{row[-1]}'

# current_city = choice(cities_only)
# all_cities += current_city
# first_letters[current_city[0].lower()] += 1
# mess = f'{current_city}, {country[city[current_city]]}'