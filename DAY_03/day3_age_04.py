"""
    인구 구조 그래프 함수 구현
"""
import csv
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib


def print_population(population):
    """
    특정 지역의 인구 현황을 화면에 출력함
    """
    for i in range(len(population)):
        print(f'{i:3d}세: {population[i]:6d}명', end=' ')
        if (i + 1) % 10 == 0:
            print()


def draw_population(district_name, population_list):
    """
    특정 지역에 대한 인구 분포를 그래프로 나타냄(plot)
    - district_name: 지역 이름
    - population_list: 0~100세 이상까지 인구수 리스트
    """
    # 그래프 출력
    plt.style.use('ggplot')
    plt.title(f'{district_name} 인구 현황')
    plt.xlabel('나이')
    plt.ylabel('인구수')

    plt.bar(range(101), population_list)
    plt.xticks(range(0, 101, 10))  # 0세 ~ 100세 이상

    plt.plot(population_list)
    plt.show()


def get_population(city):
    f = open('age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)  # 헤더 정보 건너뜀

    population_list = []
    district_name = ''
    for row in data:
        if city in row[0]:  # row[0]에 입력한 도시 정보를 포함하고 있는 경우
            district_name = row[0]
            for data in row[3:]:
                if ',' in data:
                    data = data.replace(',', '')  # 천 단위 콤마 제거
                population_list.append(int(data))
            break  # 처음으로 일치하는 도시명만 검색하기 위함
    f.close()
    print_population(population_list)
    draw_population(district_name, population_list)


if __name__ == '__main__':
    city = input('인구 구조를 알고 싶은 지역의 이름(읍면동 단위)을 입력하세요: ')
    get_population(city)
