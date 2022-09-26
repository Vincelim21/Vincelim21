#Control flow

#Eat all apples and say thank you for each apples you eat
def eat_apples(num_of_apples, on_diet):
    apples_remaining = num_of_apples
    #Loop
    while apples_remaining > 0 and not on_diet:
        apples_remaining -= 1
        print("Thank you!")
    print("Done")
    return 


eat_apples(8,False)




    