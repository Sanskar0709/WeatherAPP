import tkinter
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import requests
import pytz
import json
from datetime import *
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

root=Tk()
root.title("weather app")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")

# Create a photoimage object of the image in the path
image1 = Image.open("taj.jpg")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

label1.place(x=0, y=0)
root.resizable(False, False)


def getWeather():
    city = text.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}  {round(location.latitude,4)}")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M:%p")
    clock.config(text=current_time)


    api=f"https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&exclude=current,minutely,hourl&units=metric&appid=f98e05c57cda5ac59df8743cf497154b"
    api2=f"https://api.openweathermap.org/data/2.5/forecast?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&exclude=current,minutely,hourl&units=metric&appid=f98e05c57cda5ac59df8743cf497154b"

    json_data = requests.get(api).json()
    json_data2 = requests.get(api2).json()
    print(json_data)
    print(json_data2)
    temp = json_data['main']['temp']
    humidity = json_data['main']['humidity']
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']
    description = json_data['weather'][0]['description']
    # print(temp)
    # print(humidity)
    # print(pressure)
    # print(wind)
    # print(description)

    t.config(text = ( temp,"°C"))
    h.config(text = (humidity, "%"))
    p.config(text = (pressure, "hPa") )
    w.config(text = (wind, "m/s"))
    d.config(text = (description))



    #first cell
    firstdayimage=json_data2["list"][0]["weather"][0]["icon"]

    photo1=ImageTk.PhotoImage(file=f"icon/{firstdayimage}@2x.png")
    firstimagee.config(image=photo1)
    firstimagee.image=photo1

    tempday1 = json_data2["list"][0]["main"]["temp_min"]
    tempnight1 = json_data2["list"][0]["main"]["temp_max"]

    day1temp.config(text=f"MIN:{tempday1}°C\n MAX:{tempnight1}°C",fg="#57adff")



    #second cell
    seconddayimage = json_data2["list"][1]["weather"][0]["icon"]

    img=(Image.open(f"icon/{seconddayimage}@2x.png"))
    resized_image = img.resize((25,25))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2

    minday2 = json_data2["list"][1]["main"]["temp_min"]
    maxday2 = json_data2["list"][1]["main"]["temp_max"]

    day2temp.config(text=f"MIN:{tempday1}°C\n MAX:{tempnight1}°C", fg="#57adff")

    #third cell
    thirddayimage= json_data2["list"][2]["weather"][0]["icon"]

    img = (Image.open(f"icon/{thirddayimage}@2x.png"))
    resized_image = img.resize((25, 25))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3

    minday3 = json_data2["list"][2]["main"]["temp_min"]
    maxday3 = json_data2["list"][2]["main"]["temp_max"]

    day3temp.config(text=f"MIN:{tempday1}°C\n MAX:{tempnight1}°C", fg="#57adff")

    #fourth cell
    fourthdayimage = json_data2["list"][3]["weather"][0]["icon"]
    img = (Image.open(f"icon/{fourthdayimage}@2x.png"))
    resized_image = img.resize((25, 25))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4

    minday4 = json_data2["list"][3]["main"]["temp_min"]
    maxday4 = json_data2["list"][3]["main"]["temp_max"]

    day4temp.config(text=f"MIN:{minday4}°C\n MAX:{maxday4}°C", fg="#57adff")

    #fifth cell
    fifthdayimage= json_data2["list"][4]["weather"][0]["icon"]
    img = (Image.open(f"icon/{fifthdayimage}@2x.png"))
    resized_image = img.resize((25, 25))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5

    minday5 = json_data2["list"][4]["main"]["temp_min"]
    maxday5 = json_data2["list"][4]["main"]["temp_max"]

    day5temp.config(text=f"MIN:{minday5}°C\n MAX:{maxday5}°C", fg="#57adff")

    #sixth cell
    sixthdayimage = json_data2["list"][5]["weather"][0]["icon"]
    img = (Image.open(f"icon/{sixthdayimage}@2x.png"))
    resized_image = img.resize((25, 25))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6

    minday6 = json_data2["list"][5]["main"]["temp_min"]
    maxday6 = json_data2["list"][5]["main"]["temp_max"]

    day6temp.config(text=f"MIN:{minday6}°C\n MAX:{maxday6}°C", fg="#57adff")

    #SEVENTH CELL
    seventdayhimage = json_data2["list"][6]["weather"][0]["icon"]
    img = (Image.open(f"icon/{seventdayhimage}@2x.png"))
    resized_image = img.resize((25, 25))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image = photo7

    minday7 = json_data2["list"][6]["main"]["temp_min"]
    maxday7 = json_data2["list"][6]["main"]["temp_max"]

    day7temp.config(text=f"MIN:{minday7}°C\n MAX:{maxday7}°C", fg="#57adff")

    #days

    first=datetime.now()
    day1.configure(text=first.strftime("%A"))

    second=first+timedelta(days=1)
    day2.configure(text=second.strftime("%A"))

    third = first + timedelta(days=2)
    day3.configure(text=third.strftime("%A"))

    fourth = first + timedelta(days=3)
    day4.configure(text=fourth.strftime("%A"))

    fifth = first + timedelta(days=4)
    day5.configure(text=fifth.strftime("%A"))

    sixth = first + timedelta(days=5)
    day6.configure(text=sixth.strftime("%A"))

    seventh = first + timedelta(days=6)
    day7.configure(text=seventh.strftime("%A"))

#image api
iapi=f"https://maps.googleapis.com/maps/api/place/autocomplete/json?input=TEXT_INPUT_VALUE&types=(cities)&key=YOUR_API_KEY "


#icon
image_icon = PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)


Rectangle = PhotoImage(file="Images/Rounded Rectangle 1.png")
Label(root, image=Rectangle,bg="#57adff").place(x=45, y=115)

label1 = Label(root, text="Temperature", font=("Helvetica",11), fg="white", bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Humidity", font=("Helvetica",11), fg="white", bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="Wind", font=("Helvetica",11), fg="white", bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="Pressure", font=("Helvetica",11), fg="white", bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Description", font=("Helvetica",11), fg="white", bg="#203243")
label5.place(x=50, y=200)
#
# thermo = PhotoImage(file="C:/Users/sansk/Downloads/New folder/Thermometer.png",height=50, width=50)
# Label(root, image=thermo).place(x=32, y=200)
search=PhotoImage(file="Images/Rounded Rectangle 3.png")
Label(root, image=search,bg="#57adff").place(x=300, y=150)

weicon = PhotoImage(file="Images/Layer 7.png")
Label(root, image=weicon, bg="#203243").place(x=320, y=155)

text=tkinter.Entry(root, justify="center",width=18, font=('poppins', 25,'bold'),border=0, fg="white", bg="#203243")
text.place(x=390, y=160)
text.focus()

sric = PhotoImage(file="Images/Layer 6.png")
srchbttn = Button(root,image=sric,bg="#203243",border=0, command=getWeather)
srchbttn.place(x=677,y=155)

frame = Frame(root,width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

box = PhotoImage(file="Images/Rounded Rectangle 2 copy.png")
boxbig = PhotoImage(file="Images/Rounded Rectangle 2.png")

Label(frame,image=boxbig,bg="#212120").place(x=30, y=20)
Label(frame,image=box,bg="#212120").place(x=300, y=20)
Label(frame,image=box,bg="#212120").place(x=400, y=20)
Label(frame,image=box,bg="#212120").place(x=500, y=20)
Label(frame,image=box,bg="#212120").place(x=600, y=20)
Label(frame,image=box,bg="#212120").place(x=700, y=20)
Label(frame,image=box,bg="#212120").place(x=800, y=20)

#clock
clock=Label(root, font=("Helvetica",30,'bold'),fg="white",bg="#57adff")
clock.place(x=30, y=20)
#timezone
timezone=Label(root, font=("Helvetica",30),fg="white",bg="#57adff")
timezone.place(x=650, y=20)


long_lat=Label(root, font=("Helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=650, y=60)

#thpwd

t=Label(root,font=('Helvetica',11), fg='white',bg='#203243')
t.place(x=150, y=120)

h=Label(root,font=('Helvetica',11), fg='white',bg='#203243')
h.place(x=150, y=140)

p=Label(root,font=('Helvetica',11), fg='white',bg='#203243')
p.place(x=150, y=160)

w=Label(root,font=('Helvetica',11), fg='white',bg='#203243')
w.place(x=150, y=180)

d=Label(root,font=('Helvetica',11), fg='white',bg='#203243')
d.place(x=150, y=200)


#first cell
firstf = Frame(root, width=230, height=132, bg="#282829")
firstf.place(x=35, y=315)

day1=Label(firstf,font="arial 20",fg="white", bg='#282829')
day1.place(x=100, y=5)

firstimagee = Label(firstf,bg='#282829')
firstimagee.place(x=1, y=5)

day1temp = Label(firstf,bg="#282829",font='arial')
day1temp.place(x=100,y=45)

#second cell
secondf = Frame(root,width=70,height=115, bg="#282829")
secondf.place(x=305, y=315)

day2=Label(secondf, font="arial 10", fg="white", bg='#282829')
day2.place(x=0, y=5)

secondimage = Label(secondf,bg='#282829')
secondimage.place(x=10, y=30)

day2temp = Label(secondf,bg="#282829",font='arial 8')
day2temp.place(x=0,y=60)


#third cell
thirdf= Frame(root,width=70,height=115, bg="#282829")
thirdf.place(x=405, y=315)

day3=Label(thirdf,font="arial 10",fg="white", bg='#282829')
day3.place(x=00, y=5)

thirdimage = Label(thirdf,bg='#282829')
thirdimage.place(x=10, y=30)

day3temp = Label(thirdf,bg="#282829",font='arial 8 ')
day3temp.place(x=0,y=60)



#fourth cell
fourthf= Frame(root,width=70,height=115, bg="#282829")
fourthf.place(x=505, y=315)

day4=Label(fourthf,font="arial 10",fg="white", bg='#282829')
day4.place(x=00, y=5)

fourthimage = Label(fourthf,bg='#282829')
fourthimage.place(x=10, y=30)

day4temp = Label(fourthf,bg="#282829",font='arial 8 ')
day4temp.place(x=0,y=60)



#fifth cell
fifthf= Frame(root,width=70,height=115, bg="#282829")
fifthf.place(x=605, y=315)

day5=Label(fifthf,font="arial 10",fg="white", bg='#282829')
day5.place(x=00, y=5)
fifthimage = Label(fifthf,bg='#282829')
fifthimage.place(x=10, y=30)

day5temp = Label(fifthf,bg="#282829",font='arial 7 ')
day5temp.place(x=0,y=60)


#sixth cell
sixthf= Frame(root,width=70,height=115, bg="#282829")
sixthf.place(x=705, y=315)

day6=Label(sixthf,font="arial 10",fg="white", bg='#282829')
day6.place(x=00, y=5)

sixthimage = Label(sixthf,bg='#282829')
sixthimage.place(x=10, y=30)

day6temp = Label(sixthf,bg="#282829",font='arial 8 ')
day6temp.place(x=0,y=60)



#seventh cell
seventhf= Frame(root,width=70,height=115, bg="#282829")
seventhf.place(x=805, y=315)

day7=Label(seventhf,font="arial 10",fg="white", bg='#282829')
day7.place(x=00, y=5)

seventhimage = Label(seventhf,bg='#282829')
seventhimage.place(x=10, y=30)

day7temp = Label(seventhf,bg="#282829",font='arial 8 ')
day7temp.place(x=0,y=60)










root.mainloop()