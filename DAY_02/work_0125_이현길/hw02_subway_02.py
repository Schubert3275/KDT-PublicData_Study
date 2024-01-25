'''
    서울 지하철역에서 퇴근 시간대 가장 많이 내리는 역 5개.
    (오후  7, 8시 하차 기준)
    동일한 이름의 여러 노선을 가지는 역은 모두 누적 계산함
    - subwaytime.csv 파일 분석
    index:
        [35]: 19:00~19:59 하차
        [37]: 20:00~20:59 하차

'''

import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
station_dict = dict()
top5_station = []
number = 0
for row in data:
    row[4:] = map(int, row[4:])
    number = sum(row[35:38:2])  # 오후 7시 [35], 8시 [37] 시 하차 기준 (start=35, end38, step=2)
    if row[3] in station_dict: # row[3]: 지하철역 이름
        station_dict[row[3]] += number # 기존에 역이름이 있으면 값을 업데이트
    else:
        station_dict[row[3]] = number # 새로운 역 이름으로 딕셔너리에 새로운 데이터(역, 하차인원) 추가

sorted_dict = sorted(station_dict.items(), key=lambda x: x[1], reverse=True)

for i in range(5):
    top5_station.append(sorted_dict[i])
    print("{0}: {1:,}명".format(top5_station[i][0], top5_station[i][1]))

subway_dict = dict(top5_station)

# Bar chart 작성
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='AppleGothic')

plt.figure(dpi=100)
plt.bar(range(5), subway_dict.values(), color='blue')
plt.xticks(range(5), subway_dict.keys())
plt.title("서울 지하철 퇴근 시간대 하차 인원 비교(19:00~20:59)")
plt.show()



