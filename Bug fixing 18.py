import PySimpleGUI as sg

label = sg.Text("What are dolphins?")
option1 = sg.Radio("Amphibians", group_id="question1")
option2 = sg.Radio("Fish", group_id="question1")
option3 = sg.Radio("Mammals", group_id="question1")
option4 = sg.Radio("Birds", group_id="question1")

layout = [
    [label],
    [option1], [option2], [option3], [option4],
    [sg.Button("Submit"),
     sg.Button("Cancel")]
]

window = sg.Window("Dolphin Quiz", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Cancel":
        break
    elif event == "Submit":
        selected_option = None
        for option in [option1, option2, option3, option4]:
            if option.get():
                selected_option = option.get_text()
        break
sg.popup(f"You selected: {selected_option}")

window.close()
