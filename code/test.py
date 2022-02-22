# def prime_eratosthenes(a,b):
#     prime_list = []
#     prime = []
#     for i in range(a, b+1):
#         if i not in prime_list:
#             prime.append(i)
#             for j in range(i*i, b+1, i):
#                 prime_list.append(j)
#     print(prime)
#     print(prime_list)

# print(prime_eratosthenes(50,100));


# def extended_gcd(a, b):
#     if a == 0:
#         return b, 0, 1
#     else:
#         gcd, x, y = extended_gcd(b % a, a)
#         return gcd, y - (b // a) * x, x

# print(extended_gcd(26,7))
# k=int(input('lower bounds: '))
# n=int(input("upper bounds: "))
# primes = []
# for i in range (k+1, n+1):
#     for j in range(2, i):
#         if i%j == 0:
#             break
#     else:
#         primes.append(i)
# print(primes)

def bezout_coeffs(a, b):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a
    while r != 0:
        temp = 0
        quotient = old_r//r 
        print(quotient)
        temp = old_r
        old_r = r
        r = temp - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
        print(old_r,r,old_s,s,old_t,t)
    return {'a':old_s, 'b':old_t}
   

print(bezout_coeffs(414,662))


'"',a,'"'