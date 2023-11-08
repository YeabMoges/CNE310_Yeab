# fizzbuzz divisible by 3 and 5
# fizz divisible by 3
# buzz divisible by 5
# i if not divisible by both

for fizzbuzz in range(100):
    str_1 = ""
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        str_1 = "fizzbuzz"
        print(str_1)
    elif fizzbuzz % 3 == 0:
        str_1 = "fizz"
        print(str_1)
    elif fizzbuzz % 5 == 0:
        str_1 = "buzz"
        print(str_1)
    else:
        print(fizzbuzz)