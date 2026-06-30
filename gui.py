import PySimpleGUI as sg

tab1_layout = [
    [sg.Text("Welcome")]
]

tab2_layout = [
    [sg.Text("PySimpleGUI Project")]
]

layout = [
    [
        sg.TabGroup([
            [
                sg.Tab("Home", tab1_layout),
                sg.Tab("About", tab2_layout)
            ]
        ])
    ],
    [sg.Button("Exit")]
]

window = sg.Window("Tabs", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

window.close()