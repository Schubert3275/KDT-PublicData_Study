"""
    시간대별 지하철 이용 인원 수 (그래프)
"""
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)  # 2줄의 헤더 정보를 건너뜀
    next(data)
    result = []
    total_number = 0
    max_num = -1
    max_station = ''

    for row in data:
        row[4:] = map(int, row[4:])
        total_number += row[4]
        result.append(row[4])
        if row[4] > max_num:
            max_num = row[4]
            max_station = row[3]

print(f'새벽 4시 승차 인원 수: {total_number:,}')
print(f'최대 승차역: {max_station}, 인원수: {max_num:,}')
result.sort()  # 오름차순으로 정렬 result.sort(reverse=True)
plt.figure(dpi=100)
plt.bar(range(len(result)), result)
plt.title('새벽 4시 지하철 승차인원 현황')
plt.show()
