import csv


def get_minmax_temp(data):
    """
        최고 기온 및 최고 기온의 날짜 구하기
        ['날짜', '지점', '평균기온(℃)', '최저기온(℃)', '최고기온(℃)']
          [0]     [1]        [2]           [3]             [4]
    """
    fout = open('temp_print.csv', 'w', newline='', encoding='utf-8-sig')
    wr = csv.writer(fout, delimiter=',')
    wr.writerow(('최저 기온 날짜', '최저 기온', '최고 기온 날짜', '최고 기온'))
    header = next(data)

    min_temp = 100  # 최저 기온값을 저장할 변수 초기화(가장 큰 값)
    min_date = ''  # 최고 기온의 날짜를 저장할 변수 초기화

    max_temp = -999  # 최고 기온을 저장할 변수 초기화(가장 작은 값)
    max_date = ''  # 최고 기온의 날짜를 저장할 변수 초기화

    for row in data:
        if row[3] == '':
            row[3] = 100
        row[3] = float(row[3])

        if row[4] == '':
            row[4] = -999
        row[4] = float(row[4])

        # 최저 기온 계산
        if row[3] < min_temp:
            min_temp = row[3]
            min_date = row[0]

        # 최고 기온 계산
        if row[4] > max_temp:
            max_temp = row[4]
            max_date = row[0]  # 날짜: index[0]

        wr.writerow((min_date, min_temp, max_date, max_temp))

    print('-' * 50)
    print(f'대구 최저 기온 날짜: {min_date}, 온도: {min_temp}')
    print(f'대구 최고 기온 날짜: {max_date}, 온도: {max_temp}')


def main():
    f = open('daegu-utf8.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    get_minmax_temp(data)
    f.close()


if __name__ == '__main__':
    main()
