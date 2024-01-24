import csv

f = open('daegu.csv', 'r', encoding='utf-8')
data = csv.reader(f, delimiter=',')
print(data)  # csv_reader 객체 출력
f.close()  # 파일 닫기
