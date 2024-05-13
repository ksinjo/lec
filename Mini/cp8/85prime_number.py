# 소수 판단하는 함수 정의하기 
def prime_checker(number):
    is_prime = True
    for e in range(2,number):
        if number % e == 0:
            is_prime = False
    if is_prime:
        print("It's a PrimeNum")
    else:
        print(" [[[[ Is's not!!!! a PrimeNum]]]]]")

n = int(input())
prime_checker(number=n)
