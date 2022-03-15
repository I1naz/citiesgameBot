import csv
from random import choice
city = dict()
cities_by_first_letter = dict()
cities_only = []
country = dict()


def get_city():
    cities_only.clear()
    city.clear()
    cities_by_first_letter.clear()
    with open('cities/city.csv', encoding='utf-8') as cities:
        reader = csv.reader(cities, delimiter=';', quotechar='"')
        for index, row in enumerate(reader):
            if index == 0:
                continue
            city[f'{row[-1]}'] = f'{row[1]}'
            cities_only.append(row[-1])
            try:
                cities_by_first_letter[row[-1][0]].append(row[-1])
            except Exception as h:
                cities_by_first_letter[row[-1][0]] = [row[-1]]


def get_country():
    country.clear()
    with open('cities/country.csv', encoding='utf-8') as countries:
        reader = csv.reader(countries, delimiter=';', quotechar='"')
        for index, row in enumerate(reader):
            if index == 0:
                continue
            country[f'{row[0]}'] = f'{row[-1]}'
