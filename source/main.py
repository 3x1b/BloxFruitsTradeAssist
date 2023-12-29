import tkinter as tk
import tkinter.font as tkFont
from pyautogui import alert

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
	"dough": 1.15,
	"control": 1.05,
	"dragon": 1.3,
	"robux": 1.05
}

def calc(s1, s2, dm):
	t1 = 0
	for i in range(len(s1)):
		if s1[i] in hype.keys() and dm == 1:
			t1 += fruits[s1[i].lower()] * hype[s1[i].lower()]
		else:
			if s1[i].lower() not in fruits.keys():
				return "error 1"
			t1 += fruits[s1[i].lower()]
	t2 = 0
	for i in range(len(s2)):
		if s2[i] in hype.keys() and dm == 1:
			t2 += fruits[s2[i].lower()] * hype[s2[i].lower()]
		else:
			if s2[i].lower() not in fruits.keys():
				return "error 1"
			t2 += fruits[s2[i].lower()]
	si = ""
	if t1 == t2:
		si = "="
	elif t1 < t2:
		si = "<"
	elif t1 > t2:
		si = ">"
	return f"{str(s1)} {si} {str(s2)}\n{t1}|{t2}"

class App:
    def __init__(self, root):
        #setting title
        root.title("TradeAssist")
        Checkbox_HypeAdjust_variable = tk.IntVar()
        #setting window size
        width=600
        height=300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        Label_Left=tk.Label(root)
        ft = tkFont.Font(family='Times',size=24)
        Label_Left["font"] = tkFont.Font(family='Consolas',size=15)
        Label_Left["fg"] = "#333333"
        Label_Left["justify"] = "center"
        Label_Left["text"] = "Left Side"
        Label_Left.place(x=50,y=30,width=115,height=51)

        Label_Right=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        Label_Right["font"] = tkFont.Font(family='Consolas',size=15)
        Label_Right["fg"] = "#333333"
        Label_Right["justify"] = "center"
        Label_Right["text"] = "Right Side"
        Label_Right.place(x=400,y=30,width=115,height=51)

        Textbox_1_1=tk.Entry(root)
        Textbox_1_1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Consolas',size=10)
        Textbox_1_1["font"] = ft
        Textbox_1_1["fg"] = "#333333"
        Textbox_1_1["justify"] = "center"
        Textbox_1_1["text"] = ""
        Textbox_1_1.place(x=72,y=110,width=70,height=25)
        self.Textbox_1_1 = Textbox_1_1

        Textbox_1_2=tk.Entry(root)
        Textbox_1_2["borderwidth"] = "1px"
        ft = tkFont.Font(family='Consolas',size=10)
        Textbox_1_2["font"] = ft
        Textbox_1_2["fg"] = "#333333"
        Textbox_1_2["justify"] = "center"
        Textbox_1_2["text"] = ""
        Textbox_1_2.place(x=72,y=140,width=70,height=25)
        self.Textbox_1_2 = Textbox_1_2

        Textbox_1_3=tk.Entry(root)
        Textbox_1_3["borderwidth"] = "1px"
        ft = tkFont.Font(family='Consolas',size=10)
        Textbox_1_3["font"] = ft
        Textbox_1_3["fg"] = "#333333"
        Textbox_1_3["justify"] = "center"
        Textbox_1_3["text"] = ""
        Textbox_1_3.place(x=72,y=170,width=70,height=25)
        self.Textbox_1_3 = Textbox_1_3

        Textbox_1_4=tk.Entry(root)
        Textbox_1_4["borderwidth"] = "1px"
        ft = tkFont.Font(family='Consolas',size=10)
        Textbox_1_4["font"] = ft
        Textbox_1_4["fg"] = "#333333"
        Textbox_1_4["justify"] = "center"
        Textbox_1_4["text"] = ""
        Textbox_1_4.place(x=72,y=200,width=70,height=25)
        self.Textbox_1_4 = Textbox_1_4

        Textbox_2_1=tk.Entry(root)
        Textbox_2_1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Consolas',size=10)
        Textbox_2_1["font"] = ft
        Textbox_2_1["fg"] = "#333333"
        Textbox_2_1["justify"] = "center"
        Textbox_2_1["text"] = ""
        Textbox_2_1.place(x=422,y=110,width=70,height=25)
        self.Textbox_2_1 = Textbox_2_1

        Textbox_2_2=tk.Entry(root)
        Textbox_2_2["borderwidth"] = "1px"
        ft = tkFont.Font(family='Consolas',size=10)
        Textbox_2_2["font"] = ft
        Textbox_2_2["fg"] = "#333333"
        Textbox_2_2["justify"] = "center"
        Textbox_2_2["text"] = ""
        Textbox_2_2.place(x=422,y=140,width=70,height=25)
        self.Textbox_2_2 = Textbox_2_2

        Textbox_2_3=tk.Entry(root)
        Textbox_2_3["borderwidth"] = "1px"
        ft = tkFont.Font(family='Consolas',size=10)
        Textbox_2_3["font"] = ft
        Textbox_2_3["fg"] = "#333333"
        Textbox_2_3["justify"] = "center"
        Textbox_2_3["text"] = ""
        Textbox_2_3.place(x=422,y=170,width=70,height=25)
        self.Textbox_2_3 = Textbox_2_3

        Textbox_2_4=tk.Entry(root)
        Textbox_2_4["borderwidth"] = "1px"
        ft = tkFont.Font(family='Consolas',size=10)
        Textbox_2_4["font"] = ft
        Textbox_2_4["fg"] = "#333333"
        Textbox_2_4["justify"] = "center"
        Textbox_2_4["text"] = ""
        Textbox_2_4.place(x=422,y=200,width=70,height=25)
        self.Textbox_2_4 = Textbox_2_4

        Checkbox_HypeAdjust=tk.Checkbutton(root, variable=Checkbox_HypeAdjust_variable)
        ft = tkFont.Font(family='Times',size=10)
        Checkbox_HypeAdjust["font"] = tkFont.Font(family='Consolas',size=10)
        Checkbox_HypeAdjust["fg"] = "#333333"
        Checkbox_HypeAdjust["justify"] = "center"
        Checkbox_HypeAdjust["text"] = "Adjust for hype?"
        Checkbox_HypeAdjust.place(x=225,y=240,width=155,height=25)
        Checkbox_HypeAdjust["offvalue"] = "0"
        Checkbox_HypeAdjust["onvalue"] = "1"
        Checkbox_HypeAdjust["command"] = self.Checkbox_HypeAdjust_command
        self.Checkbox_HypeAdjust_variable = Checkbox_HypeAdjust_variable

        Calculate_Button=tk.Button(root)
        Calculate_Button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Consolas',size=17)
        Calculate_Button["font"] = tkFont.Font(family='Consolas',size=10)
        Calculate_Button["fg"] = "#000000"
        Calculate_Button["justify"] = "center"
        Calculate_Button["text"] = "Calculate"
        Calculate_Button.place(x=260,y=270,width=70,height=25)
        Calculate_Button["command"] = self.Calculate_Button_command

    def Checkbox_HypeAdjust_command(self):
        pass

    def Calculate_Button_command(self):
        alert(calc([self.Textbox_1_1.get(), self.Textbox_1_2.get(), self.Textbox_1_3.get(), self.Textbox_1_4.get()], [self.Textbox_2_1.get(), self.Textbox_2_2.get(), self.Textbox_2_3.get(), self.Textbox_2_4.get()], self.Checkbox_HypeAdjust_variable.get()))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()