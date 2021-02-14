for n in range(2, 10) :
    for x in range(2, n) :
        if n % x == 0:
            print(f"{n} is not prime number")
            break
    else:
        print(f"{n} is  prime number")