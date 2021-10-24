def euclid(a, b):
    if b==0:
        return a
    return euclid(b, a%b)
gcd = euclid(int(input("What's your first number?\n")), int(input("What's your second number?\n")))
print(f'GCD for your numbers is {gcd}')
