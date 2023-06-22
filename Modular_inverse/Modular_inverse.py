from EED.EED import eed


def mod_inverse(a, mod):

    g, a, b = eed(a, mod)

    # a, N 이 서로소가 아니라면 모듈러 곱셈 역원을 구할 수 없음
    if g > 1:
        return -1
    
    # a 가 정답
    # mod size 에 맞춤
    return (a + mod) % mod

a, mod = 3, 11
print("a:", a, ", mod:", mod)
print("modular_inverse")
print("a**-1 =", mod_inverse(a, mod))  # 모듈러 곱셈 역원 구하기
print("fermat's little theorem")
print("a**(mod-1) % mod=", a**(mod-1) % mod)     # 페르마의 소정리 (mod 가 소수라면 1이 나옴)
