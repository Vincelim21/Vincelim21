# Reverse a list

def reverse_list(mylist):
    # your code here
    i = 0
    j = len(mylist) - 1
    myReverse = []
    temp = 0
    while i < len(mylist):
        temp = mylist[j]
        myReverse.append(temp)
        i += 1
        j -= 1
    return myReverse

print(reverse_list([1,2,3,4,5]))
print(reverse_list([9,8,7,6,5]))
