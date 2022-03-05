def bezout_coeffs(a, b):
    s = 0
    s0 = 1
    t = 1
    t0 = 0
    b = b
    a = a
    dict = {'a':a,'b':b}
    if b < 0:
        while b != 0:
            quotient = a//b 
            a, b = b, a - quotient*b
            s0, s = s, s0 - quotient*s
            t0, t = t, t0 - quotient*t
        return {dict.get('a'):(s0*-1),dict.get('b'):(t0*-1)}

    else:
        while b != 0:
            quotient = a//b 
            a, b = b, a - quotient*b
            s0, s = s, s0 - quotient*s
            t0, t = t, t0 - quotient*t
        return {dict.get('a'):s0,dict.get('b'):t0}

def gcd(a,b):
    dict = bezout_coeffs(a, b)
    return abs((a * dict.get(a) + b * dict.get(b)))

def digits2letters(digits):
    letters = ""
    start = 0  #initializing starting index of first digit
    while start <= len(digits) - 2:
        digit = digits[start : start + 2]  # accessing the double digit
        letters += chr( int(digit) +65)   # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    return letters

def letters2digits(letters):
    digits = ""
    for c in letters:
        if c.isalpha():
            letter = c.upper()  #converting to uppercase  
            d = ord(letter)-65
            if d < 10:
                digits += "0" + str(d)     # concatenating to the string of digits
            else:
                digits += str(d)
    return digits

print(3**2)


