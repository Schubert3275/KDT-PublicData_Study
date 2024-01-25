"""
    lambda와 operator를 사용한 dictionary 정렬
"""
import operator

names = {'Mary': 10999, 'Sams': 2111, 'Aimy': 9778, 'Tom': 20245, 'Michale': 27115, 'Bob': 5887, 'Kelly': 7855}

# ---------------------------------------------------------
# lambda를 사용한 정렬
# ---------------------------------------------------------
# Key를 기준으로 정렬 (기본: 오름차순)
print("[lambda] dict 정렬: key 기준 오름차순")
res = sorted(names.items(), key=lambda x: x[0])
print(res)
print()

# Value를 기준으로 정렬, 내림차순: reverse=True
print("[lambda] dict 정렬: value 기준, 내림차순")
res = sorted(names.items(), key=lambda x: x[1], reverse=True)
print(res)
print()

# ---------------------------------------------------------
# operator 모듈
# - 파이썬 내장 연산자에 대한 많은 함수들을 포함
#   * add(), lt(), le(), itemgetter(), attrgetter() 등
# ---------------------------------------------------------
# Key를 기준으로 정렬 (기본: 오름차순)
sorted_x = sorted(names.items(), key=operator.itemgetter(0))
print("[operator] dict 정렬: key 기준 오름차순")
print(sorted_x)
print()

# Value를 기준으로 정렬, 내림차순: reverse=True
sorted_x = sorted(names.items(), key=operator.itemgetter(1), reverse=True)
print("[operator] dict 정렬: value 기준, 내림차순")
print(sorted_x)
