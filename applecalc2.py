
from ast import operator
from tkinter import *
from tkinter import ttk
from functools import partial




class Calculator():
    
    def __init__(self):
        self.root = Tk()
        self.root.title('Calculator')

        buttonlist = []

        


        self.result = StringVar()
        self.result.set("0")
        self.current_number = "0"
        self.current_operator = None
        self.temp = "0"

        self.font=("Myriad Pro", 50)
        self.fontsmall = ("Myriad Pro", 25)
        self.answerFont = ("Myriad Pro", 50)
        self.opfont = ("Myriad Pro", 15)


        self.mainframe = Frame(self.root, background="black")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1) 


        operator_label = ttk.Label(self.root, background="black", foreground="white", font= self.opfont, text= self.current_operator)
        operator_label.grid(column=0, row=0)


        button_clear = Button(self.root, bg="#D4D4D2", fg="#505050", text="AC", command=self.clear, font=self.fontsmall, width=4)
        button_clear.grid(column=0, row=1)

        button_inverse = Button(self.root, bg="#D4D4D2", fg="#505050", text = "+/-", font= self.fontsmall, width = 4, command= self.inverse)
        button_inverse.grid(column= 1, row = 1)

        button_percent = Button(self.root, bg="#D4D4D2", fg="#505050", text="%", font = self.fontsmall, command= self.takePercent, width = 4)
        button_percent.grid(column = 2, row = 1)

        button_zero = Button(self.root, bg="#505050", fg="#D4D4D2", text="0", font= self.fontsmall, command= partial(self.num, 0), width=5)
        button_zero.grid(row=5, column=0 ,columnspan=2)

        button_equals = Button(self.root, bg="#FF9500", fg="#D4D4D2", text="=", font= self.fontsmall, width=6, command=self.equalsFunction)
        button_equals.grid(row=5, column=2, columnspan=2)

        for i in range(4):
            signVar = "+"
            
            if i == 0:
                signVar = "÷"
            elif i == 1:
                signVar = "x"
            elif i == 2:
                signVar = "-"
            elif i == 3:
                signVar = "+"
            
            signButton = Button(self.root, 
                                bg="#FF9500", 
                                fg="#D4D4D2", 
                                width = 2,
                                text=signVar,
                                font= self.fontsmall,
                                command= partial(self.storeTemp, signVar)
                                ).grid(column=3, row=i+1)
            buttonlist.append(signButton)

            


        for i in range(9,0,-1):
            newButton = Button(self.root, 
                                bg="#505050", 
                                fg="#D4D4D2", 
                                text=str(i), 
                                command= partial(self.num, i), 
                                font=self.fontsmall, 

                                width = 4
                                ).grid(column=(i+2)%3, row=(2-(i-1)//3)+2 )



        self.answerDisplay = ttk.Label(self.root, font=self.font, foreground="white", background="black", textvariable=self.result, anchor='e', width=6)
        self.answerDisplay.grid(column=1, row=0, columnspan=10)  
              

        

        self.root.mainloop()


            
    def storeTemp(self, operator):
        print(self.current_number)
        self.current_operator = operator
        print(self.current_operator)
        self.temp = self.current_number
        print(self.temp)
        self.result.set("0")

    def clear(self):
        self.result.set("0")
        self.temp = 0
        self.current_number = "0"



  
    def num(self, aNum):
        if len(self.result.get()) < 6:
            if (self.result.get() == "0"):
                self.current_number = str(aNum)
            else:
                self.current_number += str(aNum)
            self.result.set(self.addComma(self.current_number, ","))

        print(len(str(self.result.get())), '"'+str(self.result.get())+'"')
       
        ##if len(str(self.result.get())) % 4 == 0 and len(str(self.result.get())) != 0:
        
        

    def one(self):  
        if (self.result.get() == "0"):
            self.current_number = "1"
        else:
            self.current_number += "1"
        self.result.set(self.current_number)

    def takePercent(self):
        self.result
        
    def currentOperator(self, operator):
        print(operator)
        

        print(self.current_operator)
    
    def inverse(self):
        output = self.current_number
        if self.current_number[0] == "-":
            self.current_number[0] == ""
        elif self.current_number[0] != "-":
            output
        

    def equalsFunction(self):
        if self.current_operator == "+":
            self.result.set(int(self.temp) + int(self.current_number))
            self.result.set(self.addComma(self.result.get(), ","))
        if self.current_operator == "-":
            self.result.set(int(self.temp) - int(self.current_number))
            self.result.set(self.addComma(self.result.get(), ","))
        if self.current_operator == "x":
            self.result.set(int(self.temp) * int(self.current_number))
            self.result.set(self.addComma(self.result.get(), ","))
        if self.current_operator == "÷":
            self.result.set(int(int(self.temp) / int(self.current_number)))
            self.result.set(self.addComma(self.result.get(), ","))
        self.current_number = self.result.get()
        print(self.current_number)
        
    def addComma(self, num, sepChar):
        output = num
        if len(num) % 4 == 0:
            output =  num[:1] + "," + num[1:]
        elif len(num) % 5 == 0:
            output =  num[:2] + "," + num[2:]
        return output

if __name__ == "__main__":
    calc = Calculator()