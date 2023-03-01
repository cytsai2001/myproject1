def input_to_int():
    try:
        num = int(float(input("Please input a number: ")))
        print(num)
    except ValueError:
        input_to_int()


input_to_int()

# or use while True + try except + else break
