"""
    모든 지하철역에서 시간대별 승하차 인원
"""
import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    subway_in = [0] * 24  # 승차 인원 저장 리스트
    subway_out = [0] * 24  # 하차 인원 저장 리스트

    for row in data:
        row[4:] = map(int, row[4:])
        for i in range(24):
            subway_in[i] += row[4+i*2]
            subway_out[i] += row[5+i*2]

    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic')
    else:
        plt.rc('font', family='AppleGothic')

xtick_list = []
for i in range(4, 28):
    n = i % 24
    xtick_list.append(str(n))

plt.figure(dpi=100)
plt.title('지하철 시간대별 승하차 인원 추이', size=16)
plt.grid(linestyle=':')  # 그리드 라인 표시
plt.plot(subway_in, label='승차')
plt.plot(subway_out, label='하차')
plt.legend()

plt.xticks(range(24), labels=xtick_list)
plt.xlabel('시간')
plt.ylabel('인원 (천만명)')
plt.show()
