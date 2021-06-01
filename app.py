

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import StringVar
from tkinter import *

app = tk.Tk()

user = []

app.title("Flight Reservation App")



userWindow = tk.Canvas(app)
userWindow.pack()


# frame = tk.Frame(app)
# frame.place(relheight=50, relwidth=50)



# titlelabel = tk.Label(frame, text="Flight Reservation App")
# titlelabel.config(bg="#FFFFFF", fg="#000000")
# titlelabel.pack()


# Label

nameLabel = tk.Label(app, text="Name:")
nameLabel.place(x=220, y=70, anchor='w')
    

DOBLabel = tk.Label(app, text="Date of Birth:")
DOBLabel.place(x=220, y=100, anchor='w')
# # DOBLabel.config(bg="#6cb5f9")

fromLabel = tk.Label(app, text="From:")
fromLabel.place(x = 220, y=130, anchor='w')
  


toLabel = tk.Label(app, text="To:")
toLabel.place(x=220, y=160, anchor='w')
    

seatClassLabel = tk.Label(app, text="Seat Class:")
seatClassLabel.place(x=220, y=190, anchor='w')
    

classLabel = tk.Label(app, text="Class:")
classLabel.place(x=220, y=220, anchor='w')
    

seatLabel = tk.Label(app, text="Seat:")
seatLabel.place(x=220, y=250, anchor='w')
  

PIDLabel = tk.Label(app, text="PID:")
PIDLabel.place(x=220, y=280, anchor='w')
   


# entry
nameEntry = tk.Entry(app)
userWindow.create_window(90, 70, window=nameEntry)

DOBEntry = tk.Entry(app)
userWindow.create_window(90, 100, window=DOBEntry)



# combobox

fromCb = ttk.Combobox(app , width=17)
fromCb['values'] = ['NEW YORK', 'HANOI', "TOKYO", "BANGKOK", "PARIS", "LONDON"]
fromCb.pack(ipadx=1, ipady=1, side=BOTTOM)
fromCb.place(x=335, y=130, anchor='w')



toCb = ttk.Combobox(app, width=17)
toCb['values'] = ['NEW YORK', 'HANOI', "TOKYO", "BANGKOK", "PARIS", "LONDON"]
toCb.pack(ipadx=1, ipady=1, side=BOTTOM)
toCb.place(x=335, y=160, anchor='w')


typeCb = ttk.Combobox(app, width=17)
typeCb['values'] = ['SILVER', 'GOLD', "PLATINIUM"]
typeCb.pack(ipadx=1, ipady=1, side=BOTTOM)
typeCb.place(x=335, y=190, anchor='w')



seatClassCb = ttk.Combobox(app, width=17)
seatClassCb['values'] = ['A', 'B', "C", "S"]
seatClassCb.pack(ipadx=1, ipady=1, side=BOTTOM)
seatClassCb.place(x=335, y=220, anchor='w')


seatCb = ttk.Combobox(app, width=17)
seatCb['values'] = ['111', '222', "333", "444", "555",
                    "666", "777", "888", "999", "1000",
                    "1000", "1111", "2222", "3333", "4444", "5555",
                    "6666", "7777"]
seatCb.pack(ipadx=1, ipady=1, side=BOTTOM)
seatCb.place(x=335, y=250, anchor='w')


PIDCb = ttk.Combobox(app, width=17)
PIDCb['values'] = ['VietNam Airline', 'Pacific Airlines', "VASCO", "VietJet Air", "Vietstar Airlines",
                   "Bamboo Airways", "Vietravel Airlines", "Thai Airways",
                   "Philippine Airlines", "Garuda Indonesia", "Singapore Airlines", "Malaysia Airlines",
                   "Air China", "Japan Airlines", "Air Canada", "Air France",
                   "Air India", "Asiana Airlines", "Aero Contractors"]
PIDCb.pack(ipadx=1, ipady=1, side=BOTTOM)
PIDCb.place(x=335, y=280, anchor='w')



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
    DOBs = DOBEntry.get()
    fromPlace = fromCb.get()
    toPlace = fromCb.get()
    type = typeCb.get()
    seatClass = seatClassCb.get()
    seat = seatCb.get()
    pID = PIDCb.get()
        
    
    
        
        
    tv.insert(parent='', index=0, iid=1, values=(name,DOBs,fromPlace,toPlace,type,seatClass,seat,pID)) 
    

   

    
    

    
    




    
buttonSrc = tk.Button(app, text="Submit", command= submit)

buttonSrc.pack()























tv = ttk.Treeview(app)
tv['columns']=('Name', 'DOBs','From','To','Seat Class', 'Class','Seat','PID')
tv.column('#0', width=0, stretch=NO)
# tv.column('Rank', anchor=CENTER, width=80)
tv.column('Name', anchor=CENTER, width=100)
tv.column('DOBs', anchor=CENTER, width=100)
tv.column('From', anchor=CENTER, width=100)
tv.column('To', anchor=CENTER, width=100)
tv.column('Seat Class', anchor=CENTER, width=100)
tv.column('Class', anchor=CENTER, width=100)
tv.column('Seat', anchor=CENTER, width=100)
tv.column('PID', anchor=CENTER, width=100)




# tv.heading('#0', text='', anchor=CENTER)
tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('DOBs', text='DOBs', anchor=CENTER)
tv.heading('From', text='From', anchor=CENTER)
tv.heading('To'  , text='To'  , anchor=CENTER)
tv.heading('Seat Class', text='Seat Class', anchor=CENTER)
tv.heading('Class', text='Class', anchor=CENTER)
tv.heading('Seat', text = 'Seat' ,anchor=CENTER)
tv.heading('PID',  text = "PID",anchor=CENTER)




def delAllCustomer ():
    for i in tv.get_children():
        tv.delete(i)





btnDelAll = tk.Button(app, text = "Delete All",command = delAllCustomer)
btnDelAll.pack()










tv.pack()

app.mainloop()
