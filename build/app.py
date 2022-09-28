from tkinter import *
from tkinter import messagebox
import logic_fetch
import webbrowser

root = Tk() 

#resources
app_icon = PhotoImage(file='Resources/icon.png')
app_background = PhotoImage(file='Resources/bg.png')
icon = PhotoImage(file='cdn.weatherapi.com/weather/64x64/day/113.png')
def search():
    try:
        city = city_entry.get()
        logic_fetch.get_weather(city)

        
        results = (f'''
        City = {logic_fetch.city_name}
        Time = {logic_fetch.time}
        Temperature = {logic_fetch.temp_C}
        Real Feel = {logic_fetch.feelsLikeTemp_C}
        Condition = {logic_fetch.condition}
        Humidity = {logic_fetch.humidity}
        Clouds = {logic_fetch.cloud}

        ''')
        final_result.set(results)
        icon_path = logic_fetch.icon
        global final_icon_path
        final_icon_path = icon_path[2:]
        icon_update(final_icon_path)
        




    except : 
        messagebox.showerror('Erorr','City Not Found!!')
        final_result.set('City Not Found - Please Try Again !!')

def callback(url): #Giving credits to weather Api
   webbrowser.open_new_tab(url)
    
def icon_update(path:str):
    icon_updated = PhotoImage(file=path)
    root.config(icon=icon_updated)
    updated_icon_area = Label(win,image=icon_updated)

    win.config(icon_area=updated_icon_area)
    
def create_app():
   
    global final_result,icon_photo,icon_area,win
    final_icon_path = StringVar()
    final_result = StringVar()




    #main_geomtry
    root.geometry('650x350')
    root.iconphoto(True,app_icon)
    root.title(" 날씨[Nalssi] - Weather Applcation (version - 0.1dv)")
    bg_image = Label(root,image=app_background)
    bg_image.place(x=0,y=0,relwidth=1,relheight=1)


    #widgets
    title_text = Label(text='날씨[Nalssi] - Weather Applcation',font=('Times Regular',28),bg='#BBB5F1')
    title_text.pack()

    win = Frame(root,bg='#ACFAE5',relief=SUNKEN)
    win.pack()

    City_Text = Label(win,text='Enter City').grid(row=2)
    
    global city_entry
    city_entry = Entry(win)
    city_entry.insert(0,'New Delhi')
    city_entry.grid(row=2,column=2)


    result_text = Label(win,text='Results').grid(row=5,column=0)

    result_area = Label(win,textvariable=final_result,bg='White',fg='#1D1A31')
    result_area.grid(row=6,column=0)

    icon_text = Label(win,text='Condition').grid(row=5,column=2)
    icon_area = Label(win,image=icon)
    icon_area.grid(row=6,column=2)

    Search_Button = Button(win,text='Search',command=search)
    Search_Button.grid(row=3,column=2)

    



    



#Credits Area
    credit_area = Label(root,text=" | Build By: Rahid Mondal ©2022 || Under Development || v-0.2dv ").pack()
    weather_api_text = Label(root,text='Powered by WeatherAPI.com :)',font=('Helveticabold', 8), fg="blue", cursor="hand2")
    weather_api_text.pack()
    weather_api_text.bind("<Button-1>", lambda e:
    callback("https://www.weatherapi.com/"))









    #Final Call
    root.mainloop()


if __name__ == '__main__':
    create_app()




