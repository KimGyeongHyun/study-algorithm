# -*- coding: utf-8 -*-

# ��Ŭ���� ȣ���� (�ִ����� �˰���)
# GCD(A, B) = GCD(B, A%B)
# A%B �� 0 �� ������ �ݺ��Ͽ� ���
# a, b ���� ��� ����

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

print(gcd(192, 162))