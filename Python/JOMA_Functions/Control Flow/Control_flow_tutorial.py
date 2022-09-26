#Control flow

# welcomes people legal
def website_welcome(name,age):
    if age >= 18: 
        print("Welcome " + name + "!")
        print("You are very old: " + str(age))
    else:
         print("You are not welcome, you are too young!")
         years_left = 18 - age
         print("Wait another " + str(years_left) + " years")

# prints eat apples
def eat_apples():
    print("Eating Apples")

# defines if eligigle to watch movies
def can_watch_movie(age, with_parents):
    if age >= 17 or with_parents:
        return True
    else:
        return False

#call function
website_welcome("Jason", 16)
can_watch_movie(16, False)

