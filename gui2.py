import PySimpleGUI as sg
menu = [["file",["New","Open","Exit"] ],[ "Help",["About"]]]
table = [["Gmail" , "yahya@gmail.com"],
["Github" , "yahya123"],["discord" , "Yahya_dis"]]
frame1 = [[sg.Text("Website") , sg.Input()], 
[sg.Text("User name") , sg.Input()],
[sg.Text("Password") , sg.Input(password_char="*")] , 
[sg.Button("ADD") , sg.Button("UPDATE") , sg.Button("DELETE")]]
tab1 = [[sg.Frame("",frame1)]]
tab2 = [[sg.Text("Coming Soon")]]
layout = [[sg.Menu(menu)],
[sg.Text("Password Manager 1.0v")],
[sg.TabGroup([[sg.Tab("Home" , tab1) , sg.Tab("Setting" , tab2)]])],
[sg.Table(values=table,headings=["website","username"], auto_size_columns=True , justification= "Left" , num_rows= 3)],
[sg.StatusBar("READY")],
[sg.Button("Exit")]
]
window = sg.Window("first project", size=(320 , 320) ,layout=layout)
while True:
   event, values =window.read()
   if event == "About":
     sg.popup("Password Manager v1.0")
   elif event == sg.WINDOW_CLOSED or event == "Exit":
      break
window.close()