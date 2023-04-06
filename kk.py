from tkinter import *
import requests
def get_calender():
    date = '1399/12/11'
    api_response=requests.get("https://persiancalapi.ir/jalali/"+date)
    api_json = api_response.json()
    print(api_json)
    
get_calender()

window = Tk()
window.update_idletasks()

window.geometry()
window.resizable(width=False, height=False)

Label_entry = Label(window , text = ': تاریخ را وارد کنید ')
Label_entry.grid(row = 0 , sticky= E )
Label_entry.configure(justify =RIGHT)


entry_date = Entry(window )
entry_date.grid(row = 1  , sticky=E)
entry_date.configure(justify =RIGHT)


list_box = Listbox(window  , height=20 , width=60)
list_box.grid(row = 2)
list_box.configure(justify =RIGHT)


button = Button(window  , text = 'دریافت اطلاعات')
button.grid( row = 3 , sticky=E+W )


window.mainloop()
