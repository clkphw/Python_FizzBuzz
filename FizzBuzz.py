#Loop through for loop 100 times and print FIZZ if div by 3, BUZZ if div by 5, and FIZZBUZZ if div by both
#If not Divisible print the number
for test_num in range(1,101):
    if(test_num % 3 ==0 and test_num % 5 == 0):
        print("FIZZBUZZ")
        continue
    if (test_num % 3 == 0):
        print("FIZZ")
    elif (test_num % 5 == 0):
        print("BUZZ")
    else:
        print (test_num)