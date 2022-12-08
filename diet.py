import customtkinter
import tkinter
import tkinter.messagebox

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

def button_event():
    print("Button pressed")

'''def on_closing():
    destroy()'''

WIDTH = 780
HEIGHT = 520

app = customtkinter.CTk()

app.title("BeBetter")
app.geometry(f"{WIDTH}x{HEIGHT}".format(width = WIDTH, height = HEIGHT))

#app.protocol("WM_DELETE_WINDOW", app.on_closing)  # call .on_closing() when app gets closed

# ============ two frames ============

# configure grid layout (2x1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

app.frame_left = customtkinter.CTkFrame(master=app,
                                         width=180,
                                         corner_radius=0)
app.frame_left.grid(row=0, column=0, sticky="nswe")

app.frame_right = customtkinter.CTkFrame(master=app)
app.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

# ============ frame_left ============

# configure grid layout (1x11)
app.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
app.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
app.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
app.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

app.label_1 = customtkinter.CTkLabel(master=app.frame_left,
                                      text="BeBetter")  # font name and size in px
app.label_1.grid(row=1, column=0, pady=10, padx=10)

app.button_1 = customtkinter.CTkButton(master=app.frame_left,
                                        text="Training plan",
                                        command=button_event)
app.button_1.grid(row=2, column=0, pady=30, padx=10)

app.button_2 = customtkinter.CTkButton(master=app.frame_left,
                                        text="Diet",
                                        command=button_event)
app.button_2.grid(row=3, column=0, pady=30, padx=10)

app.button_3 = customtkinter.CTkButton(master=app.frame_left,
                                        text="Daily Tasks",
                                        command=button_event)
app.button_3.grid(row=4, column=0, pady=30, padx=10)

app.button4 = customtkinter.CTkButton(master=app.frame_left,
                                       text="Stats",
                                       command=button_event)
#app.button4.grid(row=5, column=0, pady=30, padx=10)
app.button4.place(x=10, y=350)
## =================settings===================
app.settings = customtkinter.CTkLabel(master=app.frame_left,
                                 corner_radius=0,
                                 height=50,
                                 width=170,
                                 text='Settings',
                                 fg_color='white')
app.settings.place(x=0, y=470)
# =================right frame+===================
app.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
app.frame_right.rowconfigure(7, weight=10)
app.frame_right.columnconfigure((0, 1), weight=1)
app.frame_right.columnconfigure(2, weight=0)

#========diet labels===========
app.enterlabel  = customtkinter.CTkLabel(master=app.frame_right,
                                         corner_radius=6,
                                         height=400,
                                         width= 200,
                                         fg_color=("white", "gray38"),
                                         justify=tkinter.LEFT)

app.enterlabel.place(relx = 0.4,
           rely = 0.5,
           anchor = 'e')

app.outPutlabel = customtkinter.CTkLabel(master=app.frame_right,
                                        corner_radius=6,
                                        height=400,
                                        width=200,
                                        fg_color=("white", "gray38"),
                                        text='',
                                        justify=tkinter.LEFT)

app.outPutlabel.place(relx=0.55,
                     rely=0.5,
                     anchor='w')

#================== diet entering ====================
def userData():

   userAge= app.age.get()
   userHeight = app.height.get()
   userWeight = app.weight.get()
   userActivity = app.activity.get()
   print(f"Age:{userAge}\n Sex: \n Height:{userHeight}\n Weight:{userWeight}\n Activity: \n{userActivity}")
   app.mWL.configure(text=app.mWL.cget('text') + '\ntest')
   #print(userWeight,'',userHeight,'',userWeight)

app.age = customtkinter.CTkEntry(master=app.enterlabel,
                        placeholder_text = "Age",
                        width = 120,
                        height = 30,
                        border_width = 2,
                        corner_radius = 10)
app.age.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

#male
radioDug = tkinter.IntVar(app,0)
def radiobutton():
    print('kliknuto dugme: ', radioDug.get())
app.genderM = customtkinter.CTkRadioButton(master=app.enterlabel,
                                           corner_radius=10,
                                           text="Male",
                                           command=radiobutton,
                                           variable= radioDug,
                                           value=1)
app.genderM.place(relx=0.5, rely=0.3, anchor='e')

#female
app.genderF = customtkinter.CTkRadioButton(master=app.enterlabel,
                                            corner_radius=10,
                                            text="Female",
                                            command=radiobutton,
                                            variable= radioDug,
                                            value=2)
app.genderF.place(relx=0.57, rely=0.4, anchor='e')

#height
app.height = customtkinter.CTkEntry(master=app.enterlabel,
                                  placeholder_text="Height",
                                  width=120,
                                  height=30,
                                  border_width=2,
                                  corner_radius=10)
app.height.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

#weight
app.weight = customtkinter.CTkEntry(master=app.enterlabel,
                                  placeholder_text="Weight",
                                  width=120,
                                  height=30,
                                  border_width=2,
                                  corner_radius=10)
app.weight.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

#physical activity
app.activity = customtkinter.CTkOptionMenu(master=app.enterlabel,
                                            width=20,
                                            height=10,
                                            #border_width=2,
                                            corner_radius=1,
                                            values=['Sedentary: little or no exercise',
                                            'Light: exercise 1-3 times/week',
                                            'Moderate: exercise 4-5 times/week',
                                            'Active: daily exercise or intense exercise 3-4 times/week',
                                            'Very Active: intense exercise 6-7 times/week',
                                            'Extra Active: very intense exercise daily, or physical job'])
app.activity.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
calculateButton = customtkinter.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Calculate",
                                 command=userData)
calculateButton.place(relx=0.4, rely=0.8, anchor=tkinter.CENTER)

#======================diet output==============================

# mW --> maintain weight
app.mW = customtkinter.CTkLabel(master=app.frame_right, # mW --> maintain weight
                                          corner_radius=6,
                                          height=80,
                                          width=150,
                                          fg_color=("white", "black"),
                                          text='Maintain weight',
                                          anchor='n')
                                          #justify=tkinter.CENTER)

app.mW.place(relx=0.59,rely=0.21,
                       anchor='w')
#mwl -> Mild weight loss
app.mWL = customtkinter.CTkLabel(master=app.frame_right,
                                 corner_radius=6,
                                 height=80,
                                 width=150,
                                 fg_color=("white", "black"),
                                 text='Mild weight loss \n0.25kg/w',
                                 anchor='n')
                                 #justify=tkinter.CENTER)

app.mWL.place(relx=0.59, rely=0.4,
              anchor='w')

# wl -> Weight loss
app.Wl = customtkinter.CTkLabel(master=app.frame_right,
                                  corner_radius=6,
                                  height=80,
                                  width=150,
                                  fg_color=("white", "black"),
                                  text='Mild weight loss \n0.5kg/w',
                                  anchor='n')
                                  #justify=tkinter.CENTER)

app.Wl.place(relx=0.59, rely=0.6,
              anchor='w')
# ewl -> Extreme weight loss
app.Wl = customtkinter.CTkLabel(master=app.frame_right,
                                 corner_radius=6,
                                 height=80,
                                 width=150,
                                 fg_color=("white", "black"),
                                 text='Mild weight loss \n1kg/w',
                                 anchor='n')
                                #justify=tkinter.CENTER)

app.Wl.place(relx=0.59, rely=0.79,
              anchor='w')



app.mainloop()



