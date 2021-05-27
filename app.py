

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import StringVar
from tkinter import *

app = tk.Tk()

user = []

app.title("Flight Reservation App")

HEIGHT = 650
WIDTH = 800


window = tk.Canvas(app, height=HEIGHT, width=WIDTH)
window.pack()

frame = tk.Frame(app, bg="#6cb5f9")
frame.place(relheight=1, relwidth=1)


titlelabel = tk.Label(frame, text="Flight Reservation App")
titlelabel.config(bg="#6cb5f9", fg="#FFFFFF", font="Garamond 25 bold")
titlelabel.pack()


# Label
class label:
    nameLabel = tk.Label(app, text="Your Name:")
    nameLabel.place(x=630, y=70, anchor='w')
    nameLabel.config(bg="#6cb5f9")

    DOBLabel = tk.Label(app, text="Date of Birth:")
    DOBLabel.place(x=630, y=100, anchor='w')
    DOBLabel.config(bg="#6cb5f9")

    fromLabel = tk.Label(app, text="From:")
    fromLabel.place(x=630, y=130, anchor='w')
    fromLabel.config(bg="#6cb5f9")


    toLabel = tk.Label(app, text="To:")
    toLabel.place(x=630, y=160, anchor='w')
    toLabel.config(bg="#6cb5f9")

    seatClassLabel = tk.Label(app, text="Seat Class:")
    seatClassLabel.place(x=630, y=190, anchor='w')
    seatClassLabel.config(bg="#6cb5f9")

    classLabel = tk.Label(app, text="Class:")
    classLabel.place(x=630, y=220, anchor='w')
    classLabel.config(bg="#6cb5f9")

    seatLabel = tk.Label(app, text="Seat:")
    seatLabel.place(x=630, y=250, anchor='w')
    seatLabel.config(bg="#6cb5f9")

    PIDLabel = tk.Label(app, text="PID:")
    PIDLabel.place(x=630, y=280, anchor='w')
    PIDLabel.config(bg="#6cb5f9")


# entry
nameEntry = tk.Entry(app)
window.create_window(500, 70, window=nameEntry)

DOBEntry = tk.Entry(app)
window.create_window(500, 100, window=DOBEntry)

# storing info

nameVar = StringVar(app)
DOBVar = StringVar(app)
fromVar = StringVar(app)
toVar = StringVar(app)
typeVar = StringVar(app)
seatClassVar = StringVar(app)
seatVar = StringVar(app)
PIDVar = StringVar(app)


# combobox

fromCb = ttk.Combobox(app, textvariable=fromVar, width=17)
fromCb['values'] = ['NEW YORK', 'HANOI', "TOKYO", "BANGKOK", "PARIS", "LONDON"]
fromCb.pack(ipadx=1, ipady=1, side=BOTTOM)
fromCb.place(x=745, y=130, anchor='w')
# fromCb.current(0)


toCb = ttk.Combobox(app, textvariable=toVar, width=17)
toCb['values'] = ['NEW YORK', 'HANOI', "TOKYO", "BANGKOK", "PARIS", "LONDON"]
toCb.pack(ipadx=1, ipady=1, side=BOTTOM)
toCb.place(x=745, y=160, anchor='w')
# toCb.current(0)

typeCb = ttk.Combobox(app, textvariable=typeVar, width=17)
typeCb['values'] = ['SILVER', 'GOLD', "PLATINIUM"]
typeCb.pack(ipadx=1, ipady=1, side=BOTTOM)
typeCb.place(x=745, y=190, anchor='w')
# typeCb.current(0)


seatClassCb = ttk.Combobox(app, textvariable=seatClassVar, width=17)
seatClassCb['values'] = ['A', 'B', "C", "S"]
seatClassCb.pack(ipadx=1, ipady=1, side=BOTTOM)
seatClassCb.place(x=745, y=220, anchor='w')
# seatClassCb.current(0)

seatCb = ttk.Combobox(app, textvariable=seatVar, width=17)
seatCb['values'] = ['111', '222', "333", "444", "555",
                    "666", "777", "888", "999", "1000",
                    "1000", "1111", "2222", "3333", "4444", "5555",
                    "6666", "7777"]
seatCb.pack(ipadx=1, ipady=1, side=BOTTOM)
seatCb.place(x=745, y=250, anchor='w')


PIDCb = ttk.Combobox(app, textvariable=PIDVar, width=17)
PIDCb['values'] = ['VietNam Airline', 'Pacific Airlines', "VASCO", "VietJet Air", "Vietstar Airlines",
                   "Bamboo Airways", "Vietravel Airlines", "Thai Airways",
                   "Philippine Airlines", "Garuda Indonesia", "Singapore Airlines", "Malaysia Airlines",
                   "Air China", "Japan Airlines", "Air Canada", "Air France",
                   "Air India", "Asiana Airlines", "Aero Contractors"]
PIDCb.pack(ipadx=1, ipady=1, side=BOTTOM)
PIDCb.place(x=745, y=280, anchor='w')
# PIDCb.current(0)


def submit():
    # name = nameVar.get()
    # DOBs = DOBVar.get()
    # fromPlace = fromVar.get()
    # toPlace = toVar.get()
    # type = typeVar.get()
    # seatClass = seatClassVar.get()
    # seat = seatVar.get()
    # pID = PIDVar.get()
    
    
    
    name = nameEntry.get()
    print(name)

    DOBs = DOBEntry.get()
    print(DOBs)
    
    fromPlace = fromCb.get()
    print(fromPlace)
    
    toPlace = fromCb.get()
    print(toPlace)
    
    type = typeCb.get()
    print(type)
    
    seatClass = seatClassCb.get()
    print(seatClass)
    
    seat = seatCb.get()
    print(seat)
    
    pID = PIDCb.get()
    print(pID) 

    user.append({'name': name , 'DOB': DOBs , 'from' : fromPlace, "To":toPlace, 'type' : type,
                 'Seat Class': seatClass , 'Seat': seat, 'PID': pID })

    msg.showinfo("Your Information", "Your Information recorded")



    
buttonSrc = tk.Button(app, text="Submit", command= submit)

buttonSrc.pack()


app.mainloop()
