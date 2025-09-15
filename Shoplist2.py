##trial 2 

def item_info():
    item_name = input("Name: ")
    item_price = int(input("Price: "))
    return item_name, item_price


question_1 = input("What do you want to do? ")
if question_1 == "new entry":
    new_entry = item_info()
else:
    print("Okay!")


question_2 = input("Anything else? ")
while question_2 != "end":  
    if question_2 == "yes":
        question_3 = input("new entry? ")
        if question_3 == "yes":
            new_entry = item_info()
        else:
            print("oh...")
    elif question_2 == "list":
        print(new_entry)
        
    question_2 = input("Anything else? ")


