# prime number checker function

factors = []    # extra code, not important, just for fun

def prime_check():
    is_prime = True
    number = int(input("Enter any positive integer: "))

    for num in range(2, number):
        if number % num == 0:
            factors.append(num)
            is_prime = False
            print(f"{num} divides into {number}")
    if is_prime:
        factors.append(1)
        factors.append(number)
        print("Its a bloody prime dawg")
    print(f"Factors are: {factors}")
prime_check()
