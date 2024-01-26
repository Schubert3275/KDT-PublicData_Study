"""
    대구시 산격3동의 인구 분포 그래프 그리기
"""
import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

f = open('age.csv', encoding='utf-8-sig')
data = csv.reader(f)
result = []
city = ''
for row in data:
    if '산격3동' in row[0]:
        city = row[0]
        for data in row[3:]:  # 0세부터 100세 이상까지 데이터
            if ',' in data:
                data = data.replace(',', '')  # 천 단위 콤마 삭제
            result.append(int(data))  # 숫자로 변환
f.close()
print(result)

plt.title(f'{city} 인구현황')
plt.xlabel('나이')
plt.ylabel('인구수')
plt.plot(result)
plt.show()
