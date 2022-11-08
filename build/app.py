#This Version of app.py is implemented using the PysimpleGUi instead of plane tkinter for better UI.
""".
Description : python file which  controls the GUI 
Version : v.04dv 
Status : Under Development
"""
import PySimpleGUI as gui

#Theme 
gui.theme('BlueMono')

#Layout 
layout = [
    [gui.Text('날씨[Nalssi] - Weather Application',size=(50,2),background_color="#BBB5F1")],
    [gui.Text("Enter City"),gui.Input(default_text="New Delhi",key="City")],
    [gui.Button('Search')],
    [gui.Text("Result"),gui.Text("Condition")],
    [gui.Text("",key='Result'),gui.Image("")]

]

#Window Declaration 
window = gui.Window("날씨[Nalssi] - Weather Application",layout,icon="Resources\\bg.png",titlebar_icon="Resources\\bg.png")


#Event loop
while True :
    event,values = window.read()
    print(event,values)
    if event == gui.WIN_CLOSED or event == "Exit" :
        break
    if event == 'Button':
        print("You Pressed the button")

window.close()
