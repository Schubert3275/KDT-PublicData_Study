import csv
f = open('daegu-utf8.csv', encoding='utf-8-sig')

data = csv.reader(f, delimiter=',')  # delimiter 생략 가능
header = next(data)
print(header)
f.close()
