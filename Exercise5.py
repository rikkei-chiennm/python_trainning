def FizzBuzz():
    for i in range(1, 100):
        if i % 15 == 0:
            print(i, "FizzBuzz")
        elif i % 3 == 0:
            print(i, "Fizz")
        elif i % 5 == 0:
            print(i, "Buzz")

FizzBuzz()

