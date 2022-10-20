from tkinter import *
from tkinter import messagebox
import logic_fetch
import webbrowser

#Initilazing tk window in the starting 
root = Tk() 

#resources
app_icon = PhotoImage(file='Resources/icon.png')
app_background = PhotoImage(file='Resources/bg.png')
icon_default = PhotoImage(file='cdn.weatherapi.com/weather/64x64/day/176.png')


def search():
    """Finds the Weather Using login_fetch Module and return to create_app"""
    try:
        city = city_entry.get()
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
        icon_default.config(file=final_path) #updated the default image to result icon 
        final_result.set(results)


    except : 
        messagebox.showerror('Erorr','City Not Found!!')
        final_result.set('City Not Found - Please Try Again !!')

def callback(url): #Giving credits to weather Api
   webbrowser.open_new_tab(url)

def create_app():
   
    global final_result,city_entry
    final_result = StringVar()

    #main_geomtry
    root.geometry('650x360')
    root.iconphoto(True,app_icon)
    root.title(" 날씨[Nalssi] - Weather Applcation (version - v0.3-dv)")
    bg_image = Label(root,image=app_background)
    bg_image.place(x=0,y=0,relwidth=1,relheight=1)


    #widgets
    title_text = Label(text='날씨[Nalssi] - Weather Applcation',font=('Times Regular',28),bg='#BBB5F1')
    title_text.pack()
    
    #Menue Bar 
    menubar = Menu(root)
    #Adding Menue Items
    window = Menu(menubar,tearoff=0)
    menubar.add_cascade(label='window',menu=window)
    window.add_command(label='Other',command=None)

    Help = Menu(menubar,tearoff=0)
    menubar.add_cascade(label='Help',menu=Help)
    Help.add_command(label='Help',command=None)
    Help.add_separator()
    Help.add_command(label="Licence",command=None)
 
    #Main Frame 
    win = Frame(root,bg='#ACFAE5',relief=SUNKEN)
    win.pack()

    #Main Frame Widgets 
    empty_label = Label(win,text="",bg='#ACFAE5').grid(row=1,column=2)
    City_Text = Label(win,text='Enter City').grid(row=2,column=1)
    city_entry = Entry(win)
    city_entry.insert(0,'New Delhi')
    city_entry.grid(row=2,column=2)
    empty_label_2 = Label(win,text="",bg='#ACFAE5').grid(row=2,column=3)
    Search_Button = Button(win,text='Search',command=search,relief=RAISED)
    Search_Button.grid(row=3,column=2,padx=10,pady=10)
    result_text = Label(win,text='Results').grid(row=5,column=1)
    result_area = Label(win,textvariable=final_result,bg='#ACFAE5',fg='#1D1A31',width=35,height=10, relief=FLAT)
    result_area.grid(row=6,column=1)
    icon_text = Label(win,text='Condition').grid(row=5,column=2)
    icon_area = Label(win,image=icon_default)
    icon_area.grid(row=6,column=2)
   
    #Credits Page 
    credits = Frame(root,relief=SUNKEN)
    credits.pack()
    #Credits Page Widgets 
    heading_text = Label(credits,text="Credits").grid()
    main_text_area = Label(credits,text="Credits will be displayed here ").grid()


    #Credits Area
    credit_area = Label(root,text=" | Build By: Rahid Mondal ©2022 || Under Development || v0.3-dv ").pack()
    weather_api_text = Label(root,text='Powered by WeatherAPI.com :)',font=('Helveticabold', 8), fg="blue", cursor="hand2")
    weather_api_text.pack()
    weather_api_text.bind("<Button-1>", lambda e:
    callback("https://www.weatherapi.com/"))

    #Final Call
    root.config(menu=menubar)
    mainloop()

    root.mainloop()


if __name__ == '__main__':
    create_app()




