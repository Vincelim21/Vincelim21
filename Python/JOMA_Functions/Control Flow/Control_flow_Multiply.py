#Write a Python function which multiplies two values (a and b) 
# without using the multiplication symbol *. 
# Use addition and a while loop to write your function.

def multiply(a,b):
    times = 0
    added = a
    # loops b times a is added to itself 
    while times < b-1:
        a += added
        times += 1

    print(a)
    return


multiply(3,5)
multiply(-4,5)
multiply(-4,2)
    