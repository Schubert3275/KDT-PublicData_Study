"""
    대중교통 데이터 읽어오기
    - 데이터 헤더
"""
import csv

f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
print(header)
i = 1
for row in data:
    print(row)
    if i > 5:
        break
    i += 1
f.close()
