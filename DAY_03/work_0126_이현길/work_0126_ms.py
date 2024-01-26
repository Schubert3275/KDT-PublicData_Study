"""
    화면상에서 홀수를 입력 받고 해당하는 n x n 형태의 마방진을 구현하시오.
"""
while True:
    input_size = int(input("홀수차 배열의 크기를 입력하세요: "))
    if input_size % 2 == 1:
        break
    else:
        print("짝수를 입력하였습니다. 다시 입력하세요.")
print(f'Magic Square ({input_size}x{input_size})')

y, x = 0, input_size//2
digit = len(str(input_size**2))
magic_square = [[0 for _ in range(input_size)] for _ in range(input_size)]

for i in range(input_size**2):
    magic_square[y][x] = i+1
    y_new = (y - 1) if y > 0 else (input_size - 1)
    x_new = (x + 1) if x < (input_size - 1) else 0
    if magic_square[y_new][x_new] != 0:
        y += 1
    else:
        y, x = y_new, x_new

for i in range(input_size):
    for j in range(input_size):
        print(f'{magic_square[i][j]:{digit}}', end=' ' if j+1 != input_size else '\n')
