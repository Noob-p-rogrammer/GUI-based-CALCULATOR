from tkinter import*

calc = Tk()
calc.title("gui calc")
calc.minsize(width=364, height=523)
calc.maxsize(width=364, height=523)

def displaybox(source, side):
    storeobj = Frame (source, borderwidth=4 , bg ="#566573")
    storeobj.pack(side=side, expand=YES, fill=BOTH)
    return storeobj

def button(source, side, text, command=None):
    storeobj = Button(source, bg="black", fg="cyan", text=text, command=command)
    storeobj.pack(side=side, expand=YES, fill=BOTH)
    return storeobj

class app(Frame):
   def __init__(self):
        Frame. __init__(self)
        self.option_add('Font', 'Digital-7 Mono')
        self.option_add('size', '500')
        self.pack(expand=YES, fill=BOTH)

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display,justify='right',bd=26,fg='cyan',bg='black').pack(side=TOP, expand=YES, fill=BOTH)

        for clearBut in(["CLEAR"],):
            erase = displaybox(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar, lambda storeobj=display, q=ichar:storeobj.set(''))

        for Numbut in ("789/", "456", "123-", "0.+"):
            FunctionNum = displaybox(self, TOP)
            for char in Numbut:
                button(FunctionNum, LEFT, char, lambda  storeobj=display, q=char:storeobj.set(storeobj.get() + q))

        Equalsbutton = displaybox(self, TOP)
        for Equals in "=":
            if Equals == '=':
                btnequals = button(Equalsbutton, LEFT, Equals)
                btnequals.bind('<ButtonRelease-1>', lambda e, s=self, storeobj=display: s.calc(storeobj), '+')
            else:
                btnequals = button(Equalsbutton, LEFT, Equals, lambda  storeobj=display, s=' %s '%Equals: storeobj.set(storeobj.get()+s))

   def calc(self, display):
       try:
           display.set(eval(display.get()))
       except:
           display.set("ERORR")

if __name__ == '__main__':
    app().mainloop()