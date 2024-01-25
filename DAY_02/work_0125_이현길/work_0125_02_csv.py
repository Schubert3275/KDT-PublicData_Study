import csv
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
    with open(file, encoding='utf-8-sig') as f:
        data = csv.reader(f)
        next(data)
        next(data)
        station_dict = {}

        for row in data:
            if row[3] in station_dict:
                station_dict[row[3]] += (int(row[35]) + int(row[37]))
            else:
                station_dict[row[3]] = (int(row[35]) + int(row[37]))

    station_dict = dict(sorted(station_dict.items(), key=lambda x: x[1], reverse=True)[:5])

    for k, v in station_dict.items():
        print(f'{k}: {v:,}')

    draw_bar_graph("서울 지하철 퇴근 시간대 하차 인원 비교",
                   list(station_dict.keys()), list(station_dict.values()))


if __name__ == '__main__':
    main()
