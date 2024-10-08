import modules.functions as functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkPurple2")

clock = sg.Text('',  key='clock')
lebel = sg.Text("type in a to_do")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add", size=14, mouseover_colors="Green")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[
                       [clock],
                       [lebel], [input_box, add_button],
                       [list_box, edit_button, complete_button],
                       [exit_button]
                   ],
                   font=("helvetica", 20))

while True:
    event, values = window.read(timeout=20)

    # print(1, event)
    # print(2, values)
    # print(3, values["todos"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.set_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"
                print(todo_to_edit, new_todo)
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.set_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                print("Your index is out of range")
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.set_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                print("Your index is out of range")
        case "Exit":
            break

        case sg.WINDOW_CLOSED:
            break
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))


window.close()
