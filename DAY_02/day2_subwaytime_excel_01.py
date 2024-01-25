"""
    지하철 시간대별 이용 현황: 엑셀 파일 및 Pandas 활용
    - Pandas에서 엑셀 파일 읽기
      * pd.read_excel('파일이름', sheet_name='엑셀시트이름', header=[0, 1])
    - 출퇴근 시간대 이용 현황
"""
import pandas as pd
# 지하철 시간대별 이용현황

df = pd.read_excel('subway.xls', sheet_name='지하철 시간대별 이용현황', header=[0, 1])
print(df.head())
print('-' * 100)

# 모든 컬럼 내용 확인
print(df.columns)
print('-' * 100)

# 특정 컬럼 데이터 가져오기: 호선명
# - MultiIndex의 경우, 튜플 형시으로 접근
#   -> df[('호선명', 'Unnamed: 1_level_1)]
print(df[('호선명', 'Unnamed: 1_level_1')])
print('-' * 100)

# 특정 컬럼 데이터 가져오기: 지하철역
print(df[('지하철역', 'Unnamed: 3_level_1')])
print('-' * 100)

# DataFrame에서 여러 컬럼 선택
# - iloc[row_index, col_index] (iloc: integer location)
# - iloc[:, [1, 3, 10, 12, 14]] : 모든 행과 1, 3, 10, 12, 14 열 선택
commute_time_df = df.iloc[:, [1, 3, 10, 12, 14]]
print(commute_time_df.head())
print('-' * 100)

# 모든 컬럼의 데이터 타입 확인
print(commute_time_df.dtypes)
print('-' * 100)

# 천 단위 콤마 제거
# - apply(lambda x: x.replace(',', ''))
df_copy = commute_time_df.copy()
df_copy[('07:00:00~07:59:59', '승차')] = df_copy[('07:00:00~07:59:59', '승차')].apply(lambda x: x.replace(',', ''))
df_copy[('08:00:00~08:59:59', '승차')] = df_copy[('08:00:00~08:59:59', '승차')].apply(lambda x: x.replace(',', ''))
df_copy[('09:00:00~09:59:59', '승차')] = df_copy[('09:00:00~09:59:59', '승차')].apply(lambda x: x.replace(',', ''))
commute_time_df = df_copy
print(commute_time_df)
print('-' * 100)

# 데이터 타입 변경: object에서 int64로 변경
# - df.astype({‘컬럼명’ : ‘변경타입’})
commute_time_df = commute_time_df.astype({('07:00:00~07:59:59', '승차'): 'int64'})
commute_time_df = commute_time_df.astype({('08:00:00~08:59:59', '승차'): 'int64'})
commute_time_df = commute_time_df.astype({('09:00:00~09:59:59', '승차'): 'int64'})
print(commute_time_df.dtypes)
print('-' * 100)

# 각 행(지하철 역)의 승차 인원 수 합 계산
# - 행(row)의 합: df.sum(axis=1)
# - 열(column)의 합: df.sum(axis=0)
row_sum_df = commute_time_df.sum(axis=1, numeric_only=True)
passenger_number_list = row_sum_df.to_list()
print(row_sum_df)
print('-' * 100)

# 최대값 및 최대값 인덱스 찾기
# - 최대 승차 수를 가지는 지하철 역 찾기
# - 최대값 계산: df.max(axis=0)
# - 최대값 인덱스: df.idxmax()
max_number = row_sum_df.max(axis=0)  # 해당 열에서 최대값 찾기
print(max_number)

max_index = row_sum_df.idxmax()
max_line, max_station = df.iloc[max_index, [1, 3]]  # 최대값의 [1]: 호선,[3]: 지하철역명
print(f'출근 시간대 최대 승차 인원역: {max_line} {max_station} {max_number:,}명')
print('-' * 100)

#  bar-chart 그리기
import matplotlib.pyplot as plt

passenger_number_list.sort(reverse=True)
plt.figure(dpi=100)
plt.bar(range(len(passenger_number_list)), passenger_number_list)
plt.show()

plt.rcParams['']