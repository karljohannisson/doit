todo_list = []
def add_something_to_do():
    todo_list.append(input("your action to add: "))

def list_doit_items():
    counter = 1
    for item in todo_list:
        print(str(counter) + ". " + item)
        counter +=1

def remove_item():
    i_to_remove = input("item id to remove: ")
    todo_list.pop(int(i_to_remove)-1)

print("doit")
print("this is the doit app. it will make you do stuff.")

while True:
    print("[1. add something to do]")
    print("[2. list doit items]")
    print("[3. check done item]")
    print("[4. exit]")

    user_choice = input("your choice")
    match int(user_choice):
        case 1:
            add_something_to_do()
        case 2:
            list_doit_items()
        case 3:
            remove_item()
        case 4:
            print("exiting")
            break

