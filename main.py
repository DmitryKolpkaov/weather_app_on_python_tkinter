from tkinter import *
import requests

root = Tk()

def get_weather():
    city = cityField.get()
    key = '726cd28290d8937a0d5b8b22167e4b11'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units':  'metric'}
    result = requests.get(url, params=params)
    weather = result.json()

    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}' + '°C'


#Настройки окна
root['bg'] = '#CACF85'
root.title('Weather')
root.geometry('300x250')
root.resizable(width=False, height=False)

#Разметка
frame_top = Frame(root, bg='#658E9C', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#658E9C', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.2)

#Поля и кнопки
cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

btn = Button(frame_top, text="Посмотреть погоду", command=get_weather)
btn.pack()

#Строчка
info = Label(frame_bottom, text="Информация о погоде", bg='#658E9C', font=30)
info.pack()

root.mainloop()
