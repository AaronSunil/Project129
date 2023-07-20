from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv

# URLto Scrape Data
url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

# Get Page
page = requests.get(url)

# Parse Page
soup = bs(page.text,'html.parser')

# Get <table> with class = 'wikitable sortable'
star_table = soup.find_all('table', {"class":"wikitable sortable"})

total_table = len(star_table)


temp_list= []

table_rows = star_table[1].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

print(temp_list)

for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

# Convert to CSV
headers = ['Star_name','Distance','Mass','Radius']  
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)

df2.to_csv('dwarf_stars.csv', index=True, index_label="id")

df = df2[df2['column_name'].notna()]

# Convert mass and radius into floating point values

float_mass = float(Mass)
float_radius = float(Radius)

# Convert to solar radius and solar mass

solar_radius =  0.102763 * float_radius
solar_mass =  0.102763 * float_mass

# Making new csv file 
df2.to_csv('dwarf_stars_new.csv', index=True, index_label="id")

# Merging the two csv files

dataset_1 = []
dataset_2 = []
with open("dwarf_starts_new.csv", "r") as f:
    csvreader = csv.reader(f)
for row in csvreader:
    dataset_1.append(row)
with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
for row in csvreader:
    dataset_2.append(row)
headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]
headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]
headers = headers_1 + headers_2
planet_data = []
for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] + planet_data_2[index])
with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
