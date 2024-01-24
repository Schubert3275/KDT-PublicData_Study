import csv
import numpy as np


def get_min_max_numpy(data):
    next(data)

    max_temp_list = list()
    min_temp_list = list()
    date_list = list()

    for row in data:
        if row[3] == '':
            row[3] = 100

        if row[4] == '':
            row[4] = -999

        min_temp_list.append(float(row[3]))
        max_temp_list.append(float(row[4]))
        date_list.append(row[0])

    max_temp_array = np.array(max_temp_list)
    max_temp_array = max_temp_array.astype(float)
    max_temp = max_temp_array.max()
    max_index = max_temp_array.argmax()

    min_temp_array = np.array(min_temp_list)
    min_temp_array = min_temp_array.astype(float)
    min_temp = min_temp_array.min()
    min_index = min_temp_array.argmin()

    print(f'대고 최저 기온 날짜 : {date_list[min_index]}, 온도: {min_temp}')
    print(f'대고 최고 기온 날짜 : {date_list[max_index]}, 온도: {max_temp}')


def main():
    f = open('daegu-utf8.csv', 'r', encoding='utf-8-sig')
    data = csv.reader(f)
    get_min_max_numpy(data)
    f.close()


if __name__ == "__main__":
    main()
