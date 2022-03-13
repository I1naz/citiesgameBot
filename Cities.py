import csv
city = dict()
cities_only = []
country = dict()


with open('cities/city.csv', encoding='utf-8') as cities:
    reader = csv.reader(cities, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index % 2 == 0:
            continue
        city[f'{row[-1]}'] = f'{row[0]}, {row[1]}'
        cities_only.append(row[-1])
print(cities_only)

with open('cities/country.csv', encoding='utf-8') as countries:
    reader = csv.reader(countries, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index % 2 == 0:
            continue
        country[f'{row[-1]}'] = f'{row[0]}'