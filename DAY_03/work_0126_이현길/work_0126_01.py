"""
     대구광역시 전체 및 8개 구,군별 (중구, 동구, 서구, 남구, 북구, 수성구, 달서구, 달성군)
     남녀 비율을 각각의 파이 차트로 구현하세요.
"""
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('gender.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    city = '대구광역시'
    count = 1

    plt.figure(figsize=(12, 8))
    color = ['cornflowerblue', 'tomato']
    for row in data:
        if city in row[0]:
            city_name = row[0]
            male_count = int(row[104].replace(',', ''))
            female_count = int(row[207].replace(',', ''))
            plt.subplot(3, 3, count)
            plt.pie([male_count, female_count], labels=['남성', '여성'], autopct='%.1f%%', startangle=90)
            plt.title(city_name)
            count += 1
        if count > 9:
            break

plt.suptitle(city + " 구별 남녀 인구 비율")
plt.tight_layout()
plt.show()
