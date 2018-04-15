
import pandas as pd
import csv
filename = 'countryInfo.csv'

with open(filename) as fn:
    handle = csv.DictReader(fn)
    country = []
    capital = []
    population = []
    for row in handle:
        for item in row.items():
            if list(item)[0] is None:
                pass
            else:
                list1 = list(item)[1].split('\t')
                country.append(list1[4])
                capital.append(list1[5])
                population.append(int(list1[7]))

df = pd.DataFrame({'country': country, 'capital': capital,
                   'population': population})
df = df[['country', 'capital', 'population']]
df.sort_values('population', ascending=False, inplace=True)
df.to_csv('country_simple_info.csv', index=False)
