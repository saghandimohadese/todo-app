
from modules.functions import get_todos, set_todos
import time

user_prompt = "enter a todo:"
todos = []
# while True:
#     todo =input(user_prompt)
#     todos.append(todo)
#     print(todos)
#
#
# while True:
#     user_action = input("type add,show,edit,complate or exit:").strip()
#     match user_action:
#         case "add":
#             todo=input("enter a todo:")+"\n"
#
#     with open("todos.txt","a") as file:
#        file=file.write(todo)
#
#
#        case "show":
#     with open("todos.txt", "r") as file:
#              todos=file.readlines()
#              for index,todo input()
#      enumerate(todos):
#     print(index+1,"_")
#         case "edit":
#             number=input("enter number of todo to edit:")
#             number=int(number)
#             todos[number-1]=input("new todo:")
#           #todos.__setitem__(number-1,input("new todo:"))
#         case"complete":
#             number=input("enter number of todo to complate:")
#             todos.pop(int(number)-1)
#         case "exit":
#             break

#      # index=عددوشمارش
#    # ساختار اصلی=for index in rznge
#    # print(indes)
# # ساختار for todo in todos
# # print(todo)
# for index,todo in enumerate(todos):
#     print(index+1,"_",todos)

#
#
# for i in  range(1,50):
#      print(i)
#
#
# for i in  range(0,4):
#     for j in range(i+1):
#          print("*",end="")
#     print()


# m=input("enter a number:")
# # print(type)(int(m))
# for i in range(1,int(m)+1):
#    for j in range(1,i+1):
#      print("*",end="")
#      print=()

#
# while True:
#     user_action=input("type add,show,edit,complate or exit")


# menu=["pasta","pizza","salad"]
# user_choice=int(input("enter the index of the item:"))
# message=f"you choice {menu[user_choice]}."
# print(message)

#                     7       تمرین روز
# menu=["pasta","pizza","salad"]
# for i, j in enumerate(menu):
#     print(f"{i}.{j} ")

#
#
# filenames=["1.raw data.txt","2.reports.txt","3.presentations.txt"]
#
# for filename in filenames:
#     filename= filename.replace("."," - ",1)
#     print(filename)

#
# for i in  range(1,50):
#    print(i)
#
# for j in  range(4):
#     print("*" * (i+1))

# dth=10
# height=5
#
# for i in range(height):
#     if i==0 or i==height-1:
#         print("*" * width)
#     else:
# #         print("*" + " " * (width-2)+"*")
# wi
# text = "\n \
# salam be hamegi\n \
# python yek zaban barname nevisi sathe bala hast\n \
# ke baraye web,application,game,ai va sakht robat\n \
# hamchenin amniat karbord darad\n \
# "

now = time.strftime("%a, %d %b %Y %H:%M:%S")
print("It is ", now)
while True:

    user_action = input("type add, show, edit, complete or exit: ").strip()
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos("todos.txt")

        todos.append(todo)

        set_todos(todos, "todos.txt")
    elif user_action.startswith("show"):
        todos = get_todos("todos.txt")

        for todo in todos:
            todo = todo.strip("\n")

        todos = [todo.strip("\n") for todo in todos]

        for index, todo in enumerate(todos):
            print(f"{index+1} - {todo}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todos = get_todos("todos.txt")
            todos[number-1] = input("new todo:") + "\n"
            set_todos(todos, "todos.txt")
        except ValueError:
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])-1
            todos = get_todos("todos.txt")

            todo_to_remove = todos[number].strip("\n")
            todos.pop(number)
            todos = get_todos("todos.txt")
            message = f"todo {todo_to_remove} has been complete."
            print(message)
        except IndexError:
            print("todos not found (number out  of range!)")
    elif user_action.startswith("exit"):
        break
    else:
        print("invalid input")
