#This Version of app.py is implemented using the PysimpleGUi instead of plane tkinter for better UI.
""".
Description : python file which  controls the GUI 
Version : v.04dv 
Status : Under Development
"""
import PySimpleGUI as gui
import logic_fetch 

#Theme 
gui.theme('BlueMono')

#Layout 
layout = [
    [gui.Text('날씨[Nalssi] - Weather Application v-0.4dv',size=(50,2),background_color="#BBB5F1")],
    [gui.Text("Enter City"),gui.Input(default_text="New Delhi",key="City")],
    [gui.Button('Search')],
    [gui.Text("Result"),gui.Text("Condition")],
    [gui.Text("City : \n Time: \n Temperature :  \n Real Feel : \n Condition : \n Humidity : \n Clouds \n  ",key='-Result-',background_color="#ece8dd"),gui.Image("cdn.weatherapi.com/weather/64x64/day/113.png",key="-Weather_Icon-")]

]

#Window Declaration 
window = gui.Window("날씨[Nalssi] - Weather Application",layout,size=(650,390),icon=r"Resources/icon.ico")


#Event loop
while True :
    event,values = window.read()
    if event == gui.WIN_CLOSED or event == "Exit" :
        break
    if event == 'Search':
        city = values["City"]
        logic_fetch.get_weather(city)
        results = (f'''
        City : {logic_fetch.city_name}
        Time : {logic_fetch.time}
        Temperature : {logic_fetch.temp_C}
        Real Feel : {logic_fetch.feelsLikeTemp_C}
        Condition : {logic_fetch.condition}
        Humidity : {logic_fetch.humidity}
        Clouds : {logic_fetch.cloud}

        ''')
        path = logic_fetch.icon
        final_path = path[2:]
        window["-Result-"].update(results)
        window["-Weather_Icon-"].update(final_path)
        
        

window.close()
