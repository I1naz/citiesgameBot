import csv
city = dict()
country = dict()


with open('cities/city.csv') as cities:
    reader = csv.reader(cities, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index % 2 == 0:
            continue
        city[f'{row[-1]}'] = f'{row[0]}, {row[1]}'

with open('cities/country.csv') as countries:
    reader = csv.reader(countries, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index % 2 == 0:
            continue
        country[f'{row[-1]}'] = f'{row[0]}'