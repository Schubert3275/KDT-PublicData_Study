import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib


def draw_graph_on_date(month, day):
    f = open('daegu-utf8.csv', encoding='utf-8-sig')
    data = csv.reader(f)
    next(data)
    result = []
    for row in data:
        if row[-1] != '':
            date_string = row[0].split('-')
            if date_string[1] == month and date_string[2] == day:
                result.append(float(row[-1]))  # 최고 기온을 실수형으로 변환 후 리스트에 추가
    f.close()
    plt.figure(figsize=(15, 2))
    plt.plot(result, 'royalblue')
    plt.rc('axes', unicode_minus=False)
    plt.rc('font', family='Malgun Gothic')
    plt.title(f'매년 {month}년 {day}일 최고 기온 변화')
    plt.show()


def main():
    month, day = input('날짜(월 일)를 입력하세요: ').split()  # 입력된 문자열을 공백을 기준으로 분리
    draw_graph_on_date(month, day)


if __name__ == '__main__':
    main()
