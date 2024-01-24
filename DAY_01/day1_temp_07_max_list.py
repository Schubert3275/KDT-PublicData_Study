import csv
import matplotlib.pyplot as plt

f = open('daegu-utf8.csv', encoding='utf-8-sig')  # 'utf-8-sig' 생략 가능
data = csv.reader(f)

header = next(data)
result = []

for row in data:
    if row[4] != '':  # 최고 기온 데이터 값이 있으면, 리스트에 저장
        result.append(float(row[4]))

print(len(result))
f.close()
plt.figure(figsize=(10, 2))  # 그래프 크기 조절(가로 10인치, 세로 2인치)
plt.plot(result, 'r')  # result 리스트에 저장된 값을 빨간색 그래프로 그리기
plt.show()  # 그래프 그리기
