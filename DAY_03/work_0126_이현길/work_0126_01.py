"""
     대구광역시 전체 및 8개 구,군별 (중구, 동구, 서구, 남구, 북구, 수성구, 달서구, 달성군)
     남녀 비율을 각각의 파이 차트로 구현하세요.
"""
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('gender.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    population = []
    city = '대구광역시'
    city_name = ''
    color = ['cornflowerblue', 'tomato']

    plt.figure(figsize=(12, 8))
    for i in range(9):
        male_count = 0
        female_count = 0
        for row in data:
            if city in row[0]:
                city_name = row[0]
                for j in range(106, 207):
                    male_count += int(row[j].replace(',', ''))
                    female_count += int(row[j + 103].replace(',', ''))
                break
        plt.subplot(3, 3, i + 1)
        plt.pie([male_count, female_count], labels=['남성', '여성'], autopct='%.1f%%', startangle=90)
        plt.title(city_name)
plt.suptitle(city + " 구별 남녀 인구 비율")
plt.tight_layout()
plt.show()
