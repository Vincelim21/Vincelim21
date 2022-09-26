# prints a list of numbers individually
def print_list(lst):
    i = 0
    while i< len(lst):
        print(lst[i])
        i += 1
    print("done")

    return

# print_list([2,2,2,3])

#appends a list of numbers from 0 to n
def list_numbers(n):
    i = 0
    new_list = []
    while i <= n:
        new_list.append(i)
        i += 1
    return new_list

#appends a list of even numbers from 0 to n
def list_numbers2(n):
    i = 0
    new_list = []
    while i <= n:
        if i % 2 == 0:
            new_list.append(i)
        i += 1
    return new_list

print(list_numbers2(29))

