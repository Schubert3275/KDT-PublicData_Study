"""
    최근 10년 동안 대구 기온 일교차 분석

"""
import pandas as pd
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

def draw_graph(temp_df):
    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic')
    else:
        plt.rc('font', family='AppleGothic')
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(10, 5))
    plt.title("지난 10년간 대구의 일교차가 가장 큰 달")

    x_data = temp_df['Year/Month'].to_list()
    y_data = temp_df['diff'].to_list()
    plt.bar(x_data, y_data)
    plt.xlabel('Year/Month')
    plt.ylabel('일교차')
    plt.show()


def main():
    start_year = 2014
    end_year = 2023

    temp_df = pd.read_csv('daegu-utf8-df.csv', encoding='utf-8-sig')
    temp_df['날짜'] = pd.to_datetime(temp_df['날짜'], format='%Y-%m-%d')

    max_month_df = pd.DataFrame(columns=['Year/Month', 'diff'])

    #year_mean_df = pd.DataFrame(columns=['Year/Month', 'diff'])

    for year in range(start_year, end_year+1):
        year_mean_df = pd.DataFrame(columns=['Year/Month', 'diff'])
        for month in range(1, 13):
            temp_diff_month = temp_df[(temp_df['날짜'].dt.year == year) &
                                      (temp_df['날짜'].dt.month == month)]

            month_diff_mean = (temp_diff_month['최고기온'].mean() -
                               temp_diff_month['최저기온'].mean())
            month_diff_mean = round(month_diff_mean, 1)
            year_month_string = str(year) + '.' + str(month)
            year_mean_df.loc[len(year_mean_df)] = [year_month_string, month_diff_mean]

        max_month_index = year_mean_df[['diff']].idxmax()
        max_month_df = pd.concat([max_month_df, year_mean_df.loc[max_month_index]])

    print("전체 데이터 프레임 ")
    print(max_month_df)
    draw_graph(max_month_df)


main()