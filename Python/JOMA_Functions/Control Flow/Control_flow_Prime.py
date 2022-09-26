#Write a Python function that outputs the first n
# prime numbers:

def prime_numbers(n):
    #loops prime
    for num in range(2,101):
        is_prime = True
    for i in range(2,num):
        if (num%i==0):
            is_prime = False
    if is_prime:
       print (num)
    return

