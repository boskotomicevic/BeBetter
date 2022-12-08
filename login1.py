import tkinter
import tkinter.messagebox


import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")


WIDTH = 780
HEIGHT = 520

app = customtkinter.CTk()
app.title("BeBetter")
app.geometry(f"{WIDTH}x{HEIGHT}")
#self.protocol("WM_DELETE_WINDOW", self.on_closing)

app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
################$ LOGIN ##############################
#ime i prezime
app.loginFrame = customtkinter.CTkFrame(master=app,
                       width=250,
                       height=500,
                       corner_radius=10)
app.loginFrame.pack(padx = 100, pady = 170)

#Unos Imena
def stringUnos():

   name= app.unos1.get()
   surname = app.unos2.get()
   print(name,'',surname)
   if(name=='Bosko' and surname == 'Tomicevic'):
       print('login success')
   else:
       print('login failed')

app.unos1 = customtkinter.CTkEntry(master=app,

                       placeholder_text="Ime",
                       width=120,
                       height=30,
                       border_width=2,
                       corner_radius=10)
                       #command=stringUnos)
app.unos1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
#Unos Prezimena
app.unos2 = customtkinter.CTkEntry(master=app,

                                    placeholder_text="Prezime",
                                    width=120,
                                    height=30,
                                    border_width=2,
                                    corner_radius=10)
                                    #command=stringUnos)
app.unos2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

#dugme za pristup samom programu
def button_event():
    print("button pressed")
dugme = customtkinter.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Pristupi",
                                 command=stringUnos)
dugme.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)



app.mainloop()