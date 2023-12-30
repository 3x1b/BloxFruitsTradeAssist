from customtkinter import *
from pyautogui import alert

app = CTk()
app.geometry("550x350")
app.title("TradeAssist 1.2.0")

deactivate_automatic_dpi_awareness()
set_appearance_mode("dark")

app.resizable(False, False)


fruits = {
    "": 0,
    "none": 0,
    "kilo": 0,
    "rocket": 0,
    "spin": 0,
    "chop": 0,
    "spring": 0,
    "bomb": 0,
    "smoke": 0,
    "spike": 0,
    "flame": 0,
    "falcon": 0,
    "ice": 0,
    "sand": 0,
    "dark": 0,
    "diamond": 0,
    "rubber": 0.25,
    "light": 0.5,
    "barrier": 0.25,
    "ghost": 0.25,
    "magma": 1.5,
    "quake": 3,
    "buddha": 7,
    "love": 4,
    "spider": 4,
    "sound": 5,
    "phoenix": 4,
    "portal": 6,
    "rumble": 5,
    "pain": 5,
    "blizzard": 6,
    "gravity": 4.5,
    "mammoth": 8,
    "trex": 7.5,
    "t-rex": 7.5,
    "dough": 19.5,
    "shadow": 8,
    "venom": 9.5,
    "control": 9,
    "spirit": 10.5,
    "dragon": 40,
    "leopard": 75,
    "kitsune": 100,
    "robux": 0.05
}

hype = {
    "buddha": 1.1,
    "trex": 0.95,
    "t-rex": 0.95,
    "dough": 1.15,
    "control": 1.05,
    "dragon": 1.3,
    "leopard": 1.15,
    "kitsune": 1.25,
    "robux": 1.05
}

gamepasses = {
    
}

perm = {
    
}

def calc(s1, s2, dm):
    t1 = 0
    for i in range(len(s1)):
        if s1[i].lower() in hype.keys() and dm == 1:
            t1 += fruits[s1[i].lower()] * hype[s1[i].lower()]
        else:
            if s1[i].lower() not in fruits.keys():
                return "error 1"
            t1 += fruits[s1[i].lower()]
    t2 = 0
    for i in range(len(s2)):
        if s2[i].lower() in hype.keys() and dm == 1:
            t2 += fruits[s2[i].lower()] * hype[s2[i].lower()]
        else:
            if s2[i].lower() not in fruits.keys():
                return "error 1"
            t2 += fruits[s2[i].lower()]
    return [t1,t2]


left_frame = CTkFrame(master=app, width=150, height=200)
left_frame.place(relx=0.2, rely=0.4, anchor="center")

right_frame = CTkFrame(master=app, width=150, height=200)
right_frame.place(relx=0.8, rely=0.4, anchor="center")

entry_1_1 = CTkEntry(master=app)
entry_1_1.place(relx=0.2, rely=0.17, anchor="center")

entry_1_2 = CTkEntry(master=app)
entry_1_2.place(relx=0.2, rely=0.32, anchor="center")

entry_1_3 = CTkEntry(master=app)
entry_1_3.place(relx=0.2, rely=0.47, anchor="center")

entry_1_4 = CTkEntry(master=app)
entry_1_4.place(relx=0.2, rely=0.62, anchor="center")

entry_2_1 = CTkEntry(master=app)
entry_2_1.place(relx=0.8, rely=0.17, anchor="center")

entry_2_2 = CTkEntry(master=app)
entry_2_2.place(relx=0.8, rely=0.32, anchor="center")

entry_2_3 = CTkEntry(master=app)
entry_2_3.place(relx=0.8, rely=0.47, anchor="center")

entry_2_4 = CTkEntry(master=app)
entry_2_4.place(relx=0.8, rely=0.62, anchor="center")

left_value = CTkLabel(app, text="", fg_color="transparent", font=("Roboto Mono", 50))
left_value.place(relx=0.2, rely=0.85, anchor="center")

right_value = CTkLabel(app, text="", fg_color="transparent", font=("Roboto Mono", 50))
right_value.place(relx=0.8, rely=0.85, anchor="center")

def hype_switch_event():
    pass

hype_switch_var = IntVar(value=0)
hype_switch = CTkSwitch(app, text="Adjust for hype?", command=hype_switch_event,
    progress_color = "#2056e8",
    variable=hype_switch_var, onvalue=1, offvalue=0)
hype_switch.place(relx=0.5, rely=0.8, anchor="center")

def calculate_button_event():
    vals = calc([entry_1_1.get(), entry_1_2.get(), entry_1_3.get(), entry_1_4.get()], 
                [entry_2_1.get(), entry_2_2.get(), entry_2_3.get(), entry_2_4.get()], 
                hype_switch_var.get())
    if vals == "error 1":
        alert("Error 1: Invalid Fruit!")
    else:
        rvals = []
        rvals.append(round(vals[0]*10)/10)
        rvals.append(round(vals[1]*10)/10)

        cols = ["", ""]

        if rvals[0] == rvals[1]:
            cols = ["yellow", "yellow"]
        elif rvals[0] > rvals[1]:
            cols = ["green", "red"]
        elif rvals[0] < rvals[1]:
            cols = ["red", "green"]
        else:
            cols = ["red", "red"]

        left_value.configure(text=str(rvals[0]), text_color=cols[0])
        right_value.configure(text=str(rvals[1]), text_color=cols[1])


calculate_button = CTkButton(master=app, text="Calculate!", command=calculate_button_event, corner_radius=6, border_width=2,
    fg_color="#2056e8", hover_color="#1630b6", border_color="#113085")
calculate_button.place(relx=0.5, rely=0.9, anchor="center")


app.mainloop()
