def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {
        "firstname": "Sample",
        "lastname": "Test"
    }

    super_dict = {
        "integers": [1, 2, 3, 4, 5],
        "floats": [1.1, 2.2, 3.3],
    }

    for key, value in super_dict.items():
        print(key, " = ", value)


if __name__ == "__main__":
    run()
