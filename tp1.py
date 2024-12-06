import csv
import matplotlib.pyplot as plt

population_evolution = []
table=[]
with open('donnees_2008.csv',newline="") as csvfile:
     reader=csv.reader(csvfile,delimiter=',')
     for row in reader:
        table.append(row)

données_importantes = []
total_population = 0

for row in table[1:]:
    if row[2] == '89':
        données_importantes.append([row[0], row[2], row[9]])
        if row[9].isdigit():
            total_population += int(row[9])

table2=[]
with open('donnees_2016.csv',newline="") as csvfile:
     reader=csv.reader(csvfile,delimiter=',')
     for row in reader:
        table2.append(row)

données_importantes2 = []
total_population2 = 0

for row in table2[1:]:
    if row[2] == '89':
        données_importantes2.append([row[0], row[2], row[9]])
        if row[9].isdigit():
            total_population2 += int(row[9])


table3=[]
with open('donnees_2021.csv',newline="") as csvfile:
     reader=csv.reader(csvfile,delimiter=';')
     for row in reader:
        table3.append(row)

données_importantes3 = []
total_population3 = 0

for row in table3[1:]:
    if row[1] == '89':
        données_importantes3.append([row[0], row[2], row[5]])
        if row[5].isdigit():
            total_population3 += int(row[5])


table4=[]
with open('donnees_2023.csv',newline="") as csvfile:
     reader=csv.reader(csvfile,delimiter=';')
     for row in reader:
        table4.append(row)

données_importantes4 = []
total_population4 = 0

for row in table4[1:]:
    if row[2] == '89':
        données_importantes4.append([row[0], row[2], row[10]])
        if row[10].isdigit():
            total_population4 += int(row[10])

population_evolution.append(total_population)
population_evolution.append(total_population2)
population_evolution.append(total_population3)
population_evolution.append(total_population4)

print(population_evolution)

année = [2008, 2016, 2021, 2023]

plt.plot(année, population_evolution, color='b')

plt.title('Évolution de la population de la région 89')
plt.xlabel('Année')
plt.ylabel('Population Totale')

plt.show()











