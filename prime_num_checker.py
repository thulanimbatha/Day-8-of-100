# prime number checker function

def prime_check():
    is_prime = True
    number = int(input("Enter any positive integer: "))

    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            print(f"{num} divides into {number}")
    if is_prime:
        print("Its a bloody prime dawg")
prime_check()
