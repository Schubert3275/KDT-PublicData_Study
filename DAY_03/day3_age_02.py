"""
    인구수 출력
    - age.csv 데이터 헤더 (연령 구분: 1세)
           [0]        [1]             [2]         [3]   [4]   ...   [102]    [103]
        행정기관 | 총 인구수 | 연령 구간 인구수 | 0세 | 1세 | ... | 99세 | 100세 이상
    - 산격3동 (경북대 인근)의 인구 데이터 출력
"""
import csv

f = open('age.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)

result = []
for row in data:
    if '산격3동' in row[0]:  # '산격3동'이 포함된 자료만 출력
        for data in row[3:]:  # 0세 ~ 100세까지 자료를 리스트에 추가
            result.append(data)
print(result)
f.close()
