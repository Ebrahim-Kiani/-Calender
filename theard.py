from tkinter import *
import tkinter
import requests
from rtl import rtl
import threading
from tkinter import messagebox

def get_calender():
    my_thread = threading.Thread(target=get_data)
    my_thread.start()
    
    
    
def get_data():
    entry_date['state'] = DISABLED    
    button['state']  = DISABLED
      
    date = entry_date.get()
    api_response=requests.get("https://pholiday.herokuapp.com/date/"+date)
    api_json = api_response.json()
    
    
    list_box.delete(0 , 'end')
    
    if (api_response.status_code)==200:
        
        for item in api_json['events']:    
            event = (item['event'])        
            
            event_holiday =''
            
            if item['isHoliday']==True:
                
                event_holiday = '(تعطیل)'
                list_box.insert(END , event+event_holiday )
                list_box.itemconfig(END ,  {'fg':'red'})
            else:
                list_box.insert(END , event+event_holiday )
    else:
        messagebox.showerror(title='Error!!'  , message= 'Status Code : %d'%(api_response.status_code))
    
        
    entry_date['state'] = NORMAL
    button['state'] = NORMAL


    

window = Tk()
window.update_idletasks()

window.geometry()
window.resizable(width=False, height=False)

Label_entry = Label(window , text = ' تاریخ را وارد کنید: (روز-ماه-سال)')
Label_entry.grid(row = 0 , sticky= E )
Label_entry.configure(justify =RIGHT)


entry_date = Entry(window )
entry_date.grid(row = 1  , sticky=E)



list_box = Listbox(window  , height=20 , width=60)
list_box.grid(row = 2)
list_box.configure(justify =RIGHT)


button = Button(window  , text = 'دریافت اطلاعات' , command= get_calender)
button.grid( row = 3 , sticky=E+W )



window.mainloop()