"""
    투표 가능 인구수 분석
"""
import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib


def draw_piechart(city_name, city_population, voting_population):
    """
    전체 인구수 대비 투표 가능 인구의 파이차트 작성
    """
    non_voting_population = city_population - voting_population
    # [18세 미만 인구. 투표가능 인구]를 pie chart에 전달
    population = [non_voting_population, voting_population]

    color = ['tomato', 'royalblue']
    plt.pie(population, labels=['18세 미만', '투표가능인구'], autopct='%.1f%%', colors=color, startangle=90)

    plt.legend(loc=1)
    plt.title(city_name + " 투표 가능 인구 비율")
    plt.show()


def get_voting_population(city):
    """
    투표 가능 인구수 분석 row[21:]
    전체 인구수 : row[1]
    """
    f = open('age.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    header = next(data)  # 헤더 정보 건너뜀

    voting_number_list = []
    city_name = ''
    city_population = 0  # 도시 전체 인구수
    voting_population = 0
    for row in data:
        if city in row[0]:
            city_population = row[1]
            if ',' in city_population:
                # 도시 전체 인구수에서 천단위 콤마 제거
                city_population = city_population.replace(',', '')
            city_population = int(city_population)
            city_name = row[0]
            for data in row[21:]:  # 18세 이상
                if ',' in data:
                    data = data.replace(',', '')  # 천단위 콤마 제거
                voting_num = int(data)
                # 각 연령대별 투표 인구수를 리스트에 추가
                voting_number_list.append(voting_num)
                # 누적된 투표 가능 인구수
                voting_population += voting_num
            break  # 특정 도시의 데이터 중에서 제일 먼저 나오는 데이터만 분석하기 위함
    f.close()
    print(f'{city_name}전체 인구수: {city_population:,}명, 투표 가능 인구수: {voting_population:,}명')

    draw_piechart(city_name, city_population, voting_population)


if __name__ == '__main__':
    city = input('투표 가능 인구수를 확인할 도시이름을 입력하시오: ')
    get_voting_population(city)
