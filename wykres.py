import matplotlib.pyplot as plt
import random as rand
import numpy as np
from numpy import random

# labels = np.array(["SPD", "CDU/CSU", "Greens", "FDP", "AFD", "Left Party"])
# sizes = np.array([206, 196, 118, 92, 83, 39])
# explode = (0, 0, 0, 0, 0, 0) 

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal') 

# plt.show()


# x = np.array(["Niemcy", "Francja", "Włochy", "Wielka Brytania", "Hiszpania", "Holandia", "Belgia", "Szwecja", "Austria", "Dania", "Polska", "Grecja", "Finlandia", "Portugalia", "Irlandia", "Węgry", "Czechy", "Słowacja", "Słowenia", "Luksemburg", "Litwa", "Cypr", "Łotwa", "Estonia", "Malta"])
# y = np.array([22218438941, 17303107859, 14359479157, 13739900046, 8957286488, 5552933781, 4035286807, 2832862800, 2308432030, 2130860212, 2099087114, 1882611879, 1544832284, 1443049602, 1341281313, 1003119411, 932392859, 393148777, 299993572, 241439011, 221997405, 144556416, 115205431, 100756308, 57409269])

# plt.bar(x,y)
# plt.show()


ilosc = rand.randint(1,12)



for x in range(ilosc):
    y = random.randint(1,6, size=(ilosc))
    uczen = np.array([x+1])

print(y)



plt.plot(y, linestyle = 'solid', marker='o')
plt.show()
