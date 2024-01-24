import pandas as pd

# pandas의 read_csv() 함수 호출
weather_df = pd.read_csv('daegu-utf8.csv', encoding='utf-8-sig')
print(weather_df.columns)
print(weather_df['날짜'].dtype)  # 날짜 컬럼은 object 타입

# DataFrame의 column 이름 변경: 특수문자(최고기온(℃)) 제거
weather_df.columns = ['날짜', '지점', '평균기온', '최저기온', '최고기온']
print(weather_df.columns)

# 날짜 컬럼의 데이터 타입을 datetime 타입으로 변경
# - to_datetime(df['컬럼명'], format='%Y-%m-%d')
weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')
print(weather_df['날짜'].dtype)

# 누락값 개수 구하기
print(weather_df.head(5))
print(weather_df.shape)
num_rows = weather_df.shape[0]  # shape(row, col), shape[0]:  row의 개수
num_missing = num_rows - weather_df.count()  # count(): 정상값의 갯수
print(num_missing)

# 누락값(NaN) 처리
# - dropna(axis): 누락값 제거
#   - axis=0: NaN이 포함된 행 제거, axis=1: NaN이 포함된 열 제거
# - fillna(0): 누락값을 0으로 변경
# - fillnm(method='ffill'): 이전 값으로 변경(forward fill)
# - fillnm(method='bfill'): 이후 값으로 변경(backward fill)
# - interpolate(): 누락값 양쪽의 값으로 중간값 계산
weather_df = weather_df.dropna(axis=0)
print(weather_df.count())
print(weather_df.head(5))

# 누락값을 제거한 최종 데이터를 csv파일로 저장
# - index = False: 인덱스 항목 저장 안함
# - encoding='utf-8-sig': (euc-kr이 아닌 utf-8로 저장)
weather_df.to_csv('daegu-utf8-df.csv', index=False, mode='w', encoding='utf-8-sig')

# 특정 연도와 달의 최고, 최저 기온 평균값 계산
# - 해당 연도와 달의 DataFrame 가져오기
# - datetime 객체 접근
#   - dt.year, dt.month, dt.day
year_df = weather_df[weather_df['날짜'].dt.year == 2023]
month_df = year_df[year_df['날짜'].dt.month == 8]
print(month_df.head())

# 특정 연도와 달의 최저 기온 및 최고 기온의 평균 계산
max_temp_mean = round(month_df['최고기온'].mean(), 1)
min_temp_mean = round(month_df['최저기온'].mean(), 1)
print(f'2023년 8월 최저기온 평균: {min_temp_mean}, 최고기온 평균: {max_temp_mean}')
