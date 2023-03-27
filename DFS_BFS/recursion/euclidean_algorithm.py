# -*- coding: utf-8 -*-

# 유클리드 호제법 (최대공약수 알고리즘)
# GCD(A, B) = GCD(B, A%B)
# A%B 가 0 일 때까지 반복하여 재귀
# a, b 순서 상관 없음

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

print(gcd(192, 162))