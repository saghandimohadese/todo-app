import PySimpleGUI as sg


def km_to_miles(km):
    return km * 0.621371


layout = [
    [sg.Text("kilometers:"), sg.InputText(key="kms")],
    [sg.Button("Convert"), sg.Text("", key='output')],
]

window = sg.Window("Kilometers to Miles Converter", layout)

while True:
 event, values = window.read()

 match event:
    case "Convert":
        try:
            km = float(values["kms"])
            result = km_to_miles(km)
            window['output'].update(value=f"{result:.2f} miles")
        except ValueError:
            window['output'].update(value="Please enter a valid number.")
    case sg.WIN_CLOSED:
        break

window.close()