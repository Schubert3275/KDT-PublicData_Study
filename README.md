## 공공데이터

<details>
<summary>사용 교재</summary>

![](./images/모두의%20데이터%20분석%20with%20파이썬.png)

</details>

### DAY_01

---

<details>
<summary> 공공데이터 분석: 기온 데이터 분석 </summary>

> -   CSV 파일 활용
> -   대구 기온 데이터 분석

</details>

---

| 파일명                                | 내용                                              |
| ------------------------------------- | ------------------------------------------------- |
| `DAY_01\day1_temp_01.py`              | csv 파일에서 데이터 읽어오기                      |
| `DAY_01\day1_temp_02_header.py`       | csv 파일에서 한 라인씩 데이터 출력                |
| `DAY_01\day1_temp_02_remove_tab.py`   | csv 파일에서 utf-8-sig 및 \t 제거                 |
| `DAY_01\day1_temp_03.py`              | next() 함수로 데이터 헤더 출력                    |
| `DAY_01\day1_temp_04_header.py`       | 헤더 및 5개의 데이터만 출력                       |
| `DAY_01\day1_temp_05_minmax.py`       | 최저, 최고 기온 날짜와 온도 구하기                |
| `DAY_01\day1_temp_06_numpy_minmax.py` | numpy를 이용한 최저, 최고 기온 날짜와 온도 구하기 |
| `DAY_01\day1_temp_07_max_list.py`     | 데이터를 리스트에 저장                            |
| `DAY_01\day1_temp_08_hist_example.py` | hist() 함수로 주사위 시뮬레이션 작성              |
| `DAY_01\day1_temp_09_max_hist.py`     | 최고 기온 데이터를 히스토그램으로 표현            |
| `DAY_01\day1_temp_10_date_split.py`   | 날짜 정보 분리                                    |
| `DAY_01\day1_temp_10_aug_hightemp.py` | 8월의 기온 히스토그램                             |
| `DAY_01\day1_temp_11_jan_aug.py`      | 1월과 8월의 기온 데이터 히스토그램                |
| `DAY_01\day1_temp_12_day.py`          | 매년 특정 날짜의 최고 기온 찾기                   |
| `DAY_01\day1_temp_13_day_minmax.py`   | 일정 연도 이후 특정일의 최저, 최고 기온 찾기      |
| `DAY_01\day1_temp_14_pandas.py`       | pandas를 활용한 기온 데이터 처리                  |
| `DAY_01\day1_temp_15_month_avg.py`    | 1990년대와 2010년대 최고 기온 비교                |

#### DAY_01 실습과제

---

    1. 과거 10년 동안의 대구 날씨 데이터에서 1년 중 일교차가 가장 큰 달은 각각 몇 월인지 그래프로 표시
    2. 대구 기온 데이터에서 시작 연도, 마지막 연도를 입력하고 특정 월의 최고 기온 및 최저 기온의 평균값을 구하고 그래프로 표현

### DAY_02

---

<details>
<summary> 공공데이터 분석: 대중교통 데이터 </summary>

> -   승하차 인원 분석
> -   시간대별 데이터 분석

</details>

---

| 파일명                               | 내용                                                |
| ------------------------------------ | --------------------------------------------------- |
| `DAY_02\day2_subwayfee_01.py`        | 대중교통 데이터 읽어오기                            |
| `DAY_02\day2_subwayfee_02.py`        | 전체 탑승 인원 대비 유임 승차 비율이 가장 높은 역   |
| `DAY_02\day2_subwayfee_03.py`        | 무임승차 인원이 0인 역                              |
| `DAY_02\day2_subwayfee_04.py`        | 최대 무임 승차 비율 확인                            |
| `DAY_02\day2_subwayfee_05.py`        | 최대 유임 승차 인원이 있는 역                       |
| `DAY_02\day2_subwayfee_06.py`        | 유임 승차 비율이 50% 이하인 역                      |
| `DAY_02\day2_subwayfee_07.py`        | 승·하차 인원이 가장 많은 역                         |
| `DAY_02\day2_subwayfee_08.py`        | 전체 지하철 역 파이차트 분석                        |
| `DAY_02\day2_subwaytime_01.py`       | 새벽 4시 지하철 승차 전체 인원                      |
| `DAY_02\day2_subwaytime_02.py`       | 새벽 4시 지하철                                     |
| `DAY_02\day2_subwaytime_03.py`       | 출근 시간대 지하철 이용 현황                        |
| `DAY_02\day2_subwaytime_04.py`       | 시간대별 가장 많이 승차하는 역 정보 분석            |
| `DAY_02\day2_subwaytime_05.py`       | 모든 지하철역에서 시간대별 승하차 인원              |
| `DAY_02\lambda_operator.py`          | lambda 함수와 operator 모듈을 활용한 정렬방법       |
| `DAY_02\day2_subwaytime_excel_01.py` | 지하철 시간대별 이용 현황: 엑셀 파일 및 Pandas 활용 |

#### DAY_02 실습과제

---

    1. 지하철 각 노선별 최대 하차 인원을 막대그래프로 표시하고, 하차인원 출력
    2. 지하철 각 노선별 퇴근 시간대 최대 하차 인원을 막대그래프로 표시하고, 하차인원 출력

### DAY_03

---

<details>
<summary> 공공데이터 분석: 인구 데이터 </summary>

> -   대구시 인구 분석
> -   투표 가능 인구수 분석
> -   학령 인구 분석
> -   성별 데이터 분석

</details>

---

| 파일명                         | 내용                                        |
| ------------------------------ | ------------------------------------------- |
| `DAY_03\day3_age_01.py`        | 대구 산격동 인구 현황                       |
| `DAY_03\day3_age_02.py`        | 인구수 출력                                 |
| `DAY_03\day3_age_03.py`        | 대구시 산격3동의 인구 분포 그래프 그리기    |
| `DAY_03\day3_age_04.py`        | 인구 구조 그래프 함수 구현                  |
| `DAY_03\day3_age_05.py`        | 투표 가능 인구수 분석                       |
| `DAY_03\day3_age_06.py`        | 학령 인구 비율 분석                         |
| `DAY_03\day3_gender_01.py`     | gender.csv 헤더 정보                        |
| `DAY_03\day3_gender_02.py`     | 연령별 성별 데이터 시각화 1                 |
| `DAY_03\day3_gender_02_fix.py` | 연령별 성별 데이터 시각화 2                 |
| `DAY_03\day3_gender_03.py`     | 특정 지역의 남녀 인구 비율                  |
| `DAY_03\day3_gender_04.py`     | 서울특별시 및 5대 광역시의 남녀 인구수 비교 |
| `DAY_03\day3_gender_05.py`     | 제주도의 연령대별 성별 비율 산점도          |
| `DAY_03\scatter_colorbar.py`   | 색상 범례 추가                              |

#### DAY_03 실습과제

---

    1. 대구광역시 전체 및 8개 구,군별 (중구, 동구, 서구, 남구, 북구, 수성구, 달서구, 달성군)
     남녀 비율을 각각의 파이 차트로 구현하세요.
    2. 화면상에서 홀수를 입력 받고 해당하는 n x n 형태의 마방진을 구현하시오.

### DAY_04

---

<details>
<summary> 공공데이터 분석: 공공보건의료기관 데이터 </summary>

> -   공공보건의료기관 현황 분석

</details>

---

| 파일명                     | 내용                       |
| -------------------------- | -------------------------- |
| `DAY_04\day4_health.ipynb` | 공공보건의료기관 현황 분석 |
