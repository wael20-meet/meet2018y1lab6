for i in range(100):
    count = i + 1
    print(count)


for i in range(101):
    count = i + 1
    if count %3==0 and count %5==0:
        print("FizzBuzz")
    elif count % 3 == 0:
        print("fizz")
    elif count %5==0:
        print("buzz") 
    else:
        print(count)
