import customtkinter
import tkinter

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

# ============ create two frames ============

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
                                      text="CustomTkinter",
                                      text_font=("Roboto Medium", -16))  # font name and size in px
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


app.labelStat1 = customtkinter.CTkLabel(master=app.label_1,
                                      text="CustomTkinter",
                                      text_font=("Roboto Medium", -16),
                                      height=50,
                                      width=170,
                                      fg_color='white'
                                     )
app.labelStat2 = customtkinter.CTkLabel(master=app.label_1,
                                      text="CustomTkinter",
                                      text_font=("Roboto Medium", -16),
                                      height=50,
                                      width=170,
                                      fg_color='white'
                                     )
app.labelStat3 = customtkinter.CTkLabel(master=app.label_1,
                                      text="CustomTkinter",
                                      text_font=("Roboto Medium", -16),
                                      height=50,
                                      width=170,
                                      fg_color='white'
                                     )





app.mainloop()


