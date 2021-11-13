def run():

    #{key:value for value in iterable if condition}
    # challenge = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    challenge = {i: round(i**0.5, 2) for i in range(1, 1001)}
    print(challenge)


if __name__ == "__main__":
    run()