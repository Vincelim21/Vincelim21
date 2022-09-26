# Lists

# Return the same list, but all numbers square

def square_list(nums):
    i = 0
    while i < len(nums):
        nums[i] = nums[i] * nums[i]
        i += 1
    return nums

print(square_list([1,2,3,4,5]))

# Return the sum of all numbers in the list
def sum_list(nums):
    i=0
    temp = 0
    while i < len(nums):
        temp += nums[i]
        i += 1
    return temp

print(sum_list([1,3,4,5,6]))
