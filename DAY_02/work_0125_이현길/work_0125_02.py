import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


def draw_bar_graph(title, x_data, max_people):
    plt.figure(figsize=(8, 6))
    plt.title(title)
    plt.bar(x_data, max_people, width=0.6)
    plt.xticks(x_data, rotation=80)
    plt.tight_layout()
    plt.show()


def main():
    file = 'subwaytime.csv'
    subwaytime_df = pd.read_csv(file, encoding='utf-8', header=[0, 1])
    subwaytime_df = subwaytime_df.iloc[:, [3, 35, 37]]
    subwaytime_df.columns = ['지하철역', '19시 하차', '20시 하차']
    subwaytime_df['총 하차'] = subwaytime_df['19시 하차'] + subwaytime_df['20시 하차']
    station_dict = {}
    check_num = 5

    for station in subwaytime_df['지하철역'].unique():
        station_df = subwaytime_df[subwaytime_df['지하철역'] == station]
        station_dict[station] = sum(station_df['총 하차'].to_list())
    station_dict = dict(sorted(station_dict.items(), key=lambda x: x[1], reverse=True)[:check_num])

    for k, v in station_dict.items():
        print(f'{k}: {v:,}')

    draw_bar_graph("서울 지하철 퇴근 시간대 하차 인원 비교",
                   list(station_dict.keys()), list(station_dict.values()))


if __name__ == '__main__':
    main()
