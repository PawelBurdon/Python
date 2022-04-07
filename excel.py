import matplotlib.pyplot as plt
import csv

x = []
z = []

with open('Skoroszyt.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        z.append(row[1])

plt.plot(x,z, marker='o')

plt.title('Srednia')
plt.xlabel('Imie i Nazwisko') 
plt.ylabel('Srednia')
plt.show()