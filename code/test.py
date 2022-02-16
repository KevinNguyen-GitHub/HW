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
    """
    Returns a list `result` of size 3 where:
    Referring to the equation ax + by = gcd(a, b)
        result[0] is gcd(a, b)
        result[1] is x
        result[2] is y 
    """
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r//r # In Python, // operator performs integer or floored division
        # This is a pythonic way to swap numbers
        # See the same part in C++ implementation below to know more
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
        
    return {'a':old_s, 'b':old_t}
    #return dict
   

def gcd(a,b):
    dict = bezout_coeffs(a,b)
    return (a * dict['a'] + b * dict['b'])



print(gcd(2349, 36))
print(bezout_coeffs(26,7))

def prac():
    #this is me trying out random shit
    pass