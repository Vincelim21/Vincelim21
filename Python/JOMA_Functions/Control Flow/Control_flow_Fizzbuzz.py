def fizzbuzz(n):
    # your code here
    vars = 0

    while vars <= n:
        if vars %3 == 0 and vars % 5 == 0:
            print("fizzbuzz")
        elif vars % 3 == 0:
            print("fizz")
        elif vars % 5 == 0:
            print("buzz")
        else:
            print(vars)
        
        vars += 1
    return

fizzbuzz(15)