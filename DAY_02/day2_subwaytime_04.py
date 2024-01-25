"""
    시간대별 가장 많이 승차하는 역 정보 분석
"""
import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    max = [0] * 23  # 새벽 3시는 지하철 운행 안함
    max_station = [''] * 23
    xtick_list = []

    for i in range(4, 27):
        n = i % 24  # x축의 tick을 4, 5, 6, ..., 23, 0, 1, 2시로 표시하기 위함 (24 % 24 = 0)
        xtick_list.append(str(n))

    for row in data:
        row[4:] = map(int, row[4:])
        for j in range(23):
            a = row[j * 2 + 4]  # j=0: data[0 *2 + 4]의 값을 max[0]에 저장하기 위함
            if a > max[j]:
                max[j] = a
                max_station[j] = xtick_list[j] + '시:' + row[3]  # 4시: 구로

    for i in range(len(max)):
        print(f'[{max_station[i]}]: {max[i]:,}')

if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='AppleGothic')

plt.figure(figsize=(10, 10))
plt.title('시간대별 최대 승차역 정보')
plt.bar(range(23), max)
plt.xticks(range(23), labels=max_station, rotation=80)
plt.tight_layout()
plt.show()
