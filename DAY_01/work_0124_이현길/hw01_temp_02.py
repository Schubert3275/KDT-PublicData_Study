import pandas as pd
import matplotlib.pyplot as plt
import platform


def draw_two_plots(title, x_data, min_list, y_label1, max_list, y_label2):
    '''
        x_data: 연도(시작 연도 ~ 마지막 연도)
        min_list: 최저 기온 리스트
        max_list: 최고 기온 리스트
    '''
    if (platform.system() == 'Windows'):
        plt.rc('font', family='Malgun Gothic')
    else:
        plt.rc('font', family='AppleGothic')

    plt.rcParams['axes.unicode_minus'] = False # 음수(-)가 깨지는 현상 방지
    plt.figure(figsize=(18, 4))
    plt.plot(x_data, min_list, marker='s', markersize=6, color='b', label=y_label1)
    plt.plot(x_data, max_list, marker='s', markersize=6, color='r', label=y_label2)
    plt.xticks(x_data)  # 모든 xtick값을 출력함
    # plt.yticks([0, 10, 20, 30, 40]) # 모든 yticks 값을 출력함
    plt.title(title)
    plt.legend()
    plt.show()

def print_temp_list(title, temp_list):
    count = len(temp_list)
    print(title)
    for i in range(count):
        if(i <= count-2): # 마지막 데이터에 쉼표를 출력하지 않음
            print("%.1f" % temp_list[i], end=', ')
        else:
            print("%.1f" % temp_list[i])
        if(i+1) % 10 == 0:
            print()

def main():
    start_year = int(input('시작 연도를 입력하세요: '))
    end_year = int(input('마지막 연도를 입력하세요: '))
    target_month = int(input("기온 변화를 측정할 달을 입력하세요: "))

    weather_df = pd.read_csv('daegu-utf8-df.csv', encoding='utf-8-sig')
    weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')

    period = (end_year - start_year)+1 # 기온 분석 기간

    max_month_list = [0] * period # 특정 기간 동안의 해당 월의 최고기온의 평균 저장
    min_month_list = [0] * period # 특정 기간 동안의 해당 월의 최저기온 값의 평균 저장

    for year in range(start_year, end_year+1):
        year_df = weather_df[weather_df['날짜'].dt.year == year]
        month_df = year_df[year_df['날짜'].dt.month == target_month]
        min_month_list[year-start_year] = round(month_df['최저기온'].mean(), 1)
        max_month_list[year-start_year] = round(month_df['최고기온'].mean(), 1)

    title = format("{0}년부터 {1}년까지 {2}월의 기온 변화".format(start_year, end_year, target_month))
    print(title)

    print_temp_list(str(target_month) + "월 최저기온 평균: ", min_month_list)
    print_temp_list(str(target_month) + "월 최고기온 평균: ", max_month_list)

    # x축 tick 리스트 생성
    x_ticks = list()
    for year in range(start_year, end_year+1):
        x_ticks.append(year)

    y_label1 = '최저기온'
    y_label2 = '최고기온'

    draw_two_plots(title, x_ticks, min_month_list, y_label1, max_month_list, y_label2)

main()