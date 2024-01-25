"""
    최대 무임 승차 비율 확인
"""
import csv

f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
max_rate = 0
for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])  # 4, 5, 6, 7 컬럼 값을 정수로 확인
    if row[6] != 0:
        # 무임 승차 (%) - (무임 승차 수 x 100) / (유임 승차 수 + 무임 승차 수)
        rate = (row[6] * 100) / (row[4] + row[6])
        if rate > max_rate:
            max_rate = rate
            print(row, round(rate, 2), '%')
f.close()
