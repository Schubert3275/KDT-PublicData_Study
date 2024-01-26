"""
    제주도의 연령대별 성별 비율 산점도
"""
import csv
import matplotlib.pyplot as plt
import platform
import math
import koreanize_matplotlib


def draw_scatter(city, male_list, female_list, bubble_size_list):
    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic')
    else:
        plt.rc('font', family='AppleGothic')

    plt.figure(figsize=(8, 4), dpi=100)
    plt.scatter(male_list, female_list, s=bubble_size_list, c=range(101), alpha=0.5, cmap='jet')
    plt.colorbar()
    plt.plot(range(max(male_list)), range(max(male_list)), 'g--')  # 추세선 추가(녹색 점선)

    plt.title(city + " 지역의 남녀 인구수 비교")
    plt.xlabel("남성 인구 수")
    plt.ylabel("여성 인구 수")
    plt.show()


def calculate_population():
    f = open('gender.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    male_list = []
    female_list = []
    bubble_size_list = []
    city = input("찾고 싶은 지역의 이름을 입력하세요: ")

    for row in data:
        if city in row[0]:
            for i in range(106, 207):
                male_num = int(row[i].replace(',', ''))
                female_num = int(row[i+103].replace(',', ''))
                # 버블의 사이즈 조절
                bubble_size_list.append(math.sqrt(male_num + female_num))
                # bubble_size_list.append(math.log(pow(male_num, 2) + pow(female_num, 2)))
                male_list.append(male_num)
                female_list.append(female_num)
            break
    f.close()
    print(f'[여성 인구]: {female_list}')
    print(f'[남성 인구]: {male_list}')
    draw_scatter(city, male_list, female_list, bubble_size_list)


if __name__ == "__main__":
    calculate_population()
