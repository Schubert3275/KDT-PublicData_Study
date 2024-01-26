"""
    학령 인구 비율 예제
"""
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib


def draw_pie_chart(city, population_list, label_list):
    plt.pie(population_list, labels=label_list, autopct='%.1f%%', startangle=90)

    plt.legend(loc=1)
    plt.title(city + " 학령 인구 비율")
    plt.show()


def get_population(row, start, end):
    population = 0
    for num in row[start:end+1]:
        if ','in num:
            num = num.replace(',', '')
        num = int(num)
        population += num
    return population


def school_age_population(city):
    city_population = 0
    non_school_pop = 0
    school_age_pop = 0

    label_list = ['초등학생','중학생', '고등학생', '대학생', '비학령인구']
    population_list = []

    f = open('age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    header = next(data)  # 헤더 정보 건너뜀

    for row in data:
        if city in row[0]:
            city_population = row[1]
            if ',' in city_population:
                # 도시 전체 인구수에서 천단위 콤마 제거
                city_population = city_population.replace(',', '')
            city_population = int(city_population)

            # 각 구간별 인구 계산
            elementary_pop = get_population(row, 9, 14)
            population_list.append(elementary_pop)

            middleschool_pop = get_population(row, 15, 17)
            population_list.append(middleschool_pop)

            highschool_pop = get_population(row, 18, 20)
            population_list.append(highschool_pop)

            university_pop = get_population(row, 21, 24)
            population_list.append(university_pop)

            school_age_pop = (elementary_pop + middleschool_pop + highschool_pop + university_pop)

            non_school_pop = city_population - school_age_pop
            population_list.append(non_school_pop)
            break
    f.close()
    print(f'전체 인구수: {city_population:,} 학령인구수: {school_age_pop:,}'
          f' 학령인구 비율: {round((school_age_pop*100)/city_population, 1)}%')
    draw_pie_chart(city, population_list, label_list)


if __name__ == '__main__':
    city = input('학령인구를 분석할 도시 이름: ')
    school_age_population(city)
