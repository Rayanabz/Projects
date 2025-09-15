##trial 2 


#New entry function
def item_info():
    f = open("shoplist.txt", "a")
    item_name = input("Name: ")
    item_price = str(input("Price: "))
    item = item_name + " " + item_price
    f.write (f"{item}\n")
    return item


#List function
def item_entry():
    f = open("shoplist.txt")
    contents = f.read()
    f.close
    print(contents)


#Beginning question
question_1 = input("What do you want to do? ")
if question_1 == "new entry":
    new_entry = item_info()
else:
    print("Okay!")

##End loop
question_2 = input("Anything else? ")
while question_2 != "end":  
    if question_2 == "yes":
        question_3 = input("new entry? ")
        if question_3 == "yes":
            new_entry = item_info()
        else:
            print("oh...")
    elif question_2 == "list":
        new_entry = item_entry()
    question_2 = input("Anything else? ")


