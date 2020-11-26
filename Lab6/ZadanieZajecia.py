import random
import math


losowePunkty1 = list(map(lambda a: (random.randint(0, 100) / -200, random.randint(0, 100) / 200),range(0, 1000)))
funkcja1 = len(list(filter(lambda b: math.sqrt(0.25+b[0]**2<b[1]), losowePunkty1)))

losowePunkty2 = list(map(lambda a: ((random.randint(0, 100) / 200), (random.randint(0, 100) / 200)),range(0, 1000)))
funkcja2 = len(list(filter(lambda b: -math.sqrt((-1)*b[0]**2+b[0])+0.5<b[1],losowePunkty2)))

losowePunkty3 = list(map(lambda a: (random.randint(0, 100) / -200, random.randint(0, 100) / -200),range(0, 1000)))
funkcja3 = len(list(filter(lambda b: math.sqrt(1+b[0]*(4*(-b[0]))*0.09)< b[1], losowePunkty3)))

losowePunkty4 = list(map(lambda a: (random.randint(0, 100) / 200, random.randint(0, 100) / -2000),range(0, 1000)))
funkcja4 = len(list(filter(lambda b: 1.2*b[0]**2-0.3<b[1], losowePunkty4)))


pole = (0.25*(funkcja1/len(losowePunkty1))+0.25*(funkcja2/len(losowePunkty2))+0.25*(funkcja3/len(losowePunkty3))+0.25*(funkcja4/len(losowePunkty4)))
print(pole)
