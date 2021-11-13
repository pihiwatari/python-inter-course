from math import sqrt


def prime_number(number):
    # Number should be greater than 1
    if number == 0:
        print("Zero is not a prime number")
        return

    # if the number is 1 then print result
    elif number == 1:
        print("1 prime")
        return

    # check if the number modulo by 2 is not equal to 0
    for i in range(2, int(sqrt(number))+1):
        if (number % i == 0):
            print(number, ": is not prime")
            return

    print(number, ": is prime")


if __name__ == "__main__":
    prime_number(17)
    prime_number(1)
    prime_number(2)
    prime_number(3)
    prime_number(155)
    prime_number(155689)
