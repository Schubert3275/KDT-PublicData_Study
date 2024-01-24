import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


def draw_minmax_graph(title, x_data, min_temp, max_temp):
    plt.rcParams['axes.unicode_minus']= False
    plt.figure(figsize=(20, 4))
    plt.plot(x_data, min_temp, label='최저기온', color='b', marker='s')
    plt.plot(x_data, max_temp, label='최고기온', color='r', marker='s')
    plt.xticks(x_data)

    plt.title(title)
    plt.legend()
    plt.show()


def main():
    file = '../daegu-utf8-df.csv'
    weather_df = pd.read_csv(file, encoding='utf-8-sig')
    weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')
    high_temp_list = []
    low_temp_list = []
    start_year = int(input("시작 연도를 입력하세요: "))
    end_year = int(input("마지막 연도를 입력하세요: "))
    select_month = int(input("기온 변화를 측정할 달을 입력하세요: "))

    years = list(range(start_year, end_year+1))

    for year in years:
        year_df = weather_df[(weather_df['날짜'].dt.year == year) &
                             (weather_df['날짜'].dt.month == select_month)]
        high_temp_list.append(round(year_df['최고기온'].mean(), 1))
        low_temp_list.append(round(year_df['최저기온'].mean(), 1))

    print(f'{start_year} 년부터 {end_year} 년까지 {select_month} 월의 기온 변화')
    print(f'{select_month} 월 최저기온 평균:\n', ', '.join(map(str, low_temp_list)))
    print(f'{select_month} 월 최고기온 평균:\n', ', '.join(map(str, high_temp_list)))

    draw_minmax_graph(f'{start_year}년부터 {end_year}년까지 {select_month}월의 기온 변화',
                      years, low_temp_list, high_temp_list)


if __name__ == '__main__':
    main()
