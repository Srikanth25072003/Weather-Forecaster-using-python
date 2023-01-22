import tkinter as tk
import pip._vendor.requests
from PIL import Image,ImageTk 


root=tk.Tk()

root.title("Weather Application")
root.geometry("800x600")

#Key: 2f5e50542ef3c6e0bce1bc1f239de81f
#Api url: api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
def format_response(weather):
    try: 
        #Information that is collected is diplayed in the following format
        city=weather['name']
        condition=weather['weather'][0]['description']
        temp=weather['main']['temp']
        real_feel=weather['main']['feels_like']
        temp1=weather['main']['temp_min']
        temp2=weather['main']['temp_max']
        temp3=weather['main']['humidity']
        temp4=weather['main']['pressure'] 
        wind=weather['wind']['speed']       
        coordination1=weather['coord']['lon']
        coordination2=weather['coord']['lat']
        timezone=weather['timezone']
        country=weather['sys']['country']
        final_str='City : %s\nCondition : %s\nTemprature (°F) : %s\nReal Feel (°F) : %s\nMinimum (°F) : %s\nMaximum (°F) : %s\nHumidity : %s\nPressure : %s\nWind Speed (Kmph) : %s\nLongnitude : %s\nLatitude : %s\nTimezone (UTC) : %s\nCountry : %s'%(city,condition,temp,real_feel,temp1,temp2,temp3,temp4,wind,coordination1,coordination2,timezone,country)
    except:
        #Reply for not entering the correct or required information
        final_str='There was a problem in retrieving that information'
    return final_str

def get_weather(city):
    weather_key='2f5e50542ef3c6e0bce1bc1f239de81f'
    url= 'https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'imperial'}
    response=pip._vendor.requests.get(url,params)
    #print(response.json())
    weather=response.json()

    #print(weather['name'])
    #print(weather['weather'][0]['description'])
    #print(weather['main']['temp'])
    
    result['text']=format_response(weather)

    icon_name=weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size=int(frame_two.winfo_height()*0.25)
    img=ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size,size)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0,anchor='nw',image=img)
    weather_icon.image=img


#the background image is being called here.
img=Image.open('./bg.jpg')
img=img.resize((800,600),Image.ANTIALIAS)
img_photo=ImageTk.PhotoImage(img)
#BG Label
bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=800,height=600)
#title
heading_title=tk.Label(bg_lbl,text='Search over 200,000 cities!',fg='black',bg='lightgray',font=('times new roman',18,'bold'))
heading_title.place(x=155,y=70)

frame_one=tk.Frame(bg_lbl,bg="#555555",bd=5)
frame_one.place(x=150,y=110,width=500,height=60)
#Text box for the city name to be entered
txt_box=tk.Entry(frame_one, font=('times new roman',30),width=17)
txt_box.grid(row=0,column=0,sticky='W')
#button used to obtain the information
btn=tk.Button(frame_one,text='Get Weather',fg='black',font=('times new roman',16,'bold'),command=lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=10)


frame_two=tk.Frame(bg_lbl,bg="#555555",bd=5)
frame_two.place(x=150,y=200,width=500,height=320)

result=tk.Label(frame_two,font=40,bg='white',justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)


weather_icon=tk.Canvas(result,bg='white',bd=0,highlightthickness=0)
weather_icon.place(x=300,y=20,relwidth=1,relheight=0.50)



root.mainloop()



