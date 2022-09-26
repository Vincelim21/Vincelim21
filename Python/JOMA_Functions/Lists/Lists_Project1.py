def generate_list(start,end,step):
    # your code here
    new_list = []
    if start < end:
        while start < end:
            new_list.append(start) 
            start += step
    #if start is larger than end
    else:
        while start > end:
            new_list.append(start)
            start += step
    return new_list

print(generate_list(0,5,1))
print(generate_list(0,0,1))
print(generate_list(5,10,2))
print(generate_list(10,5,-2))
