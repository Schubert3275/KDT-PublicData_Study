import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


def draw_bar_graph(title, x_data, day_temp_rate):
    plt.figure(figsize=(10, 6))
    plt.bar(x_data, day_temp_rate)
    plt.xticks(x_data)

    plt.title(title)
    plt.xlabel('Year/Month')
    plt.ylabel('일교차')
    plt.show()


def main():
    file = 'daegu-utf8-df.csv'
    weather_df = pd.read_csv(file, encoding='utf-8')
    weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')
    weather_df['일교차'] = (weather_df['최고기온'] - weather_df['최저기온']).round(1)

    years = list(range(2014, 2024))
    temp_rate_max_month_list = []
    temp_rate_max_list = []

    pd.set_option('display.max_rows', None)

    for year in years:
        year_df = weather_df[(weather_df['날짜'].dt.year == year)]
        temp_rate_dict = {}
        for month in range(1, 13):
            month_df = year_df[(year_df['날짜'].dt.month == month)]
            temp_rate_dict[month] = month_df['일교차'].mean().round(1)
        temp_sort = sorted(temp_rate_dict.items(), key=lambda x: x[1], reverse=True)[0]
        temp_rate_max_month_list.append(f'{year}.{temp_sort[0]}')
        temp_rate_max_list.append(temp_sort[1])

    draw_bar_graph('지난 10년간 대구의 일교차가 가장 큰 달', temp_rate_max_month_list, temp_rate_max_list)
    print(temp_rate_max_month_list)
    print(temp_rate_max_list)


if __name__ == '__main__':
    main()
