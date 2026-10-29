def fizzbuzz(n):
    array_fizzbuzz = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            array_fizzbuzz.append("FizzBuzz")
        elif i % 3 == 0:
            array_fizzbuzz.append("Fizz")
        elif i % 5 == 0:
            array_fizzbuzz.append("Buzz")
        else:
            array_fizzbuzz.append(str(i))
    return array_fizzbuzz

n = int(input("n= "))
result = fizzbuzz(n)
print(result)