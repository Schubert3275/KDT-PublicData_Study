"""
    산점도에 color bar 추가하기
    - colorbar() 함수
        * 그래프 우측에 color bar를 추가함
    - scatter() 함수 속성 추가
        * c=range(색상 개수)
            - 각 데이터에 해당하는 color bar의 색으로 정해짐
        * cmap: 컬러맵 속성 사용 (cmap='jet') - 무지개색
"""
import matplotlib.pyplot as plt
y_value = [10, 50, 20, 10]
x_value = [1, 2, 3, 4]
size = []
for y in  y_value:
    size.append(y * 5)

plt.scatter(x_value, y_value, s=size, c=range(4), cmap='jet')
plt.colorbar()
plt.show()
