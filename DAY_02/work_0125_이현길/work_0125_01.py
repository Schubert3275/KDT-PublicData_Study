import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


def draw_bar_graph(title, x_data, max_people):
    plt.figure(figsize=(12, 8))
    plt.title(title)
    plt.bar(x_data, max_people)
    plt.xticks(x_data, rotation=80)
    plt.tight_layout()
    plt.show()


def main():
    file = 'subwaytime.csv'
    subwaytime_df = pd.read_csv(file, encoding='utf-8', header=[0, 1])
    subwaytime_df = subwaytime_df.iloc[:, [1, 3, 11, 13]]
    subwaytime_df.columns = ['호선명', '지하철역', '07시 하차', '08시 하차']
    subwaytime_df['총 하차'] = subwaytime_df['07시 하차'] + subwaytime_df['08시 하차']
    line_list = []

    for i in range(1, 7 + 1):
        line_df = subwaytime_df[subwaytime_df['호선명'] == f'{i}호선']
        line_list.append(line_df.sort_values(by='총 하차', ascending=False).iloc[0].to_list())

    line_name_list = [f'{line_list[i][0]} {line_list[i][1]}' for i in range(7)]
    people_list = [line_list[i][-1] for i in range(7)]

    for i in range(7):
        print(f'출근시간대 {line_list[i][0]} 최대 하차역: {line_list[i][1]}, 하차인원: {people_list[i]:,}명')

    draw_bar_graph("출근 시간대 지하철 노선별 최대 하차 인원 및 하차역", line_name_list, people_list)


if __name__ == '__main__':
    main()
