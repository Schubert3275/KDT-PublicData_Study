'''
    출근 시간대(07:00 ~ 08:59) 노선별 최대 하차 인원 계산
     - 1 ~ 7호선 정보만 출력

'''

import pandas as pd
import matplotlib.pyplot as plt
import platform
import koreanize_matplotlib

def draw_bar_chart(max_station_info):
    max_station_number = []
    max_station_name = []

    ### 각 지하철 노선별 최대 하차 인원 막대 그래프로 그리기
    for i in range(len(max_station_info)):
        # [0]: 노선번호, [1]: 역이름, [2]: 최대 하차 인원
        print('출근 시간대 {0} 최대 하차역: {1}역, 하차인원: {2:,}명'.
              format(max_station_info[i][0] , max_station_info[i][1], max_station_info[i][2]))
        max_station_name.append(max_station_info[i][0] + ' ' + max_station_info[i][1])
        max_station_number.append(max_station_info[i][2])

    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic')
    elif platform.system() == 'Darwin':
        plt.rc('font', family='AppleGothic')
    else:
        print('지원하지 않는 시스템입니다. ')

    plt.figure(dpi=100)
    plt.bar(range(7), max_station_number)
    plt.xticks(range(7), max_station_name, rotation=80)
    plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역')
    plt.tight_layout()
    plt.show()


def get_subway_line_max_number():
    df = pd.read_excel('subway.xls', sheet_name='지하철 시간대별 이용현황',
                       header=[0, 1])

    # 출근 시간대 정보만 추출 후 시간대 정보를 int64로 변경
    commute_df = df.iloc[:, [1, 3, 11, 13]]

    for i in [2, 3]:
        commute_df.iloc[:, i] = commute_df.iloc[:, i].apply(lambda x: x.replace(',', ''))
        commute_df.iloc[:, i] = commute_df.iloc[:, i].astype('int64')
    print(commute_df.head())

    commute_df.columns = ['호선명', '지하철역', '7시하차', '8시하차']
    #commute_df['총하차인원'] = commute_df.sum(axis=1, numeric_only=True)
    commute_df['총하차인원'] = commute_df[['7시하차', '8시하차']].sum(axis=1)
    print(commute_df.head())

    # 노선 정보를 리스트로 만듬
    line_list = [str(n) + '호선' for n in range(1, 8)]
    max_station_info =[] # [[노선번호, 지하철역, 하차인원]]

    for line in line_list:
        line_df = commute_df[commute_df['호선명'] == line]
        line_max_num = line_df['총하차인원'].max()
        line_max_index = line_df['총하차인원'].idxmax()
        line, line_max_station = commute_df.iloc[line_max_index, [0, 1]]
        max_station_info.append([line, line_max_station, line_max_num])

    #print(max_station_info)

    # bar 차트 그리기
    draw_bar_chart(max_station_info)

get_subway_line_max_number()
