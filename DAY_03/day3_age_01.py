"""
    대구 산격동 인구 현황
"""
import csv

f = open('age.csv', encoding='utf-8-sig')
data = csv.reader(f)

header = next(data)
print(header)
# row[0]: 행정기관
for row in data:
    if '산격3동' in row[3]:  # '산격3동'이 포함된 자료만 출력
        print(row)
f.close()
