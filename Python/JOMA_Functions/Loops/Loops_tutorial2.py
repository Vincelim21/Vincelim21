#break and continue

#Break Example:

# This function determines if the list contains at
# least one number that is even
def has_even_number(lst):
    has_even = False
    for num in lst:
        print("Now looking at " + str(num))
        if num % 2 == 0:
            has_even = True
            break
    return has_even

"""
> has_even_number([1,3,5])
False

> has_even_number([1,2,3])
True
"""

# Continue Example

# This function determines how much tips you received and print
# and print "thank you" for the people who tipped 5 dollars or more

def receive_tips(tips):
    tipTotal = 0
    for num in tips:
        tipTotal += num
        if num < 5:
            continue
        print("Thanks for $" + str(num))
    print(str(tipTotal))


receive_tips([10,5,2])
receive_tips([3,4,2])
"""
> receive_tips([10,5,2])
Thanks for $10
Thanks for $5
17

> receive_tips([3,4,2])
9
"""
