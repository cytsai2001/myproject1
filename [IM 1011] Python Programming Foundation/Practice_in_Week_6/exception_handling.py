def input_to_int():
    try:
        num = int(float(input("Please input an number: ")))
        print(num)
    except ValueError:
        input_to_int()


input_to_int()
