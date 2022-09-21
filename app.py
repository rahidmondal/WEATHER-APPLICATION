from tkinter import *
from logic_fetch import *
import logic_fetch




def search():
    city = city_entry.get()
    get_weather(city)

    
    results = (f'''
    City = {logic_fetch.city_name}
    Time = {logic_fetch.time}
    Temperature = {logic_fetch.temp_C}
    Real Fell = {logic_fetch.feelsLikeTemp_C}
    Condition = {logic_fetch.condition}
    Humidity = {logic_fetch.humidity}
    Clouds = {logic_fetch.cloud}

     ''')
    final_result.set(results)




    
def create_app():
    root = Tk()
    global final_result
    final_result = StringVar()

    #resources
    app_icon = PhotoImage(file='Resources/icon.png')
    app_background = PhotoImage(file='Resources/bg.png')

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

    Search_Button = Button(win,text='Search',command=search)
    Search_Button.grid(row=3,column=2)
    
    result_text = Label(win,text='Results').grid(row=4,column=0)

    result_area = Label(win,textvariable=final_result,bg='White',fg='Black')
    result_area.grid(row=5,column=0)






    #Final Call
    root.mainloop()


if __name__ == '__main__':
    create_app()




