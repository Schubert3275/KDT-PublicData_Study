"""
    gender.csv 헤더 정보
"""
import csv

f = open('gender.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)

for i in range(len(header)):
    print(f'[{i:3d}]: {header[i]}', end=', ')

    if (i+1) % 10 == 0:
        print()
f.close()
