import csv

f = open('daegu.csv', 'r', encoding='utf-8')
data = csv.reader(f, delimiter=',')
print(data)
f.close()
