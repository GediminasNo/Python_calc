from tkinter import *
from tkinter import font
from PIL import ImageTk, Image

class Simple_calculator:

    def __init__(self,Master):
        Master.title("Simple Calculator")

        Master.resizable(False, False)

        Master.iconbitmap('C:/Users/Gediminas/PycharmProjects/pythonProject2Projektasnamudarbai2023/pitonas/calc.png')


        self.entry_1 = Entry(Master)
        # Master.configure(bg='#856ff8')

        myfont = font.Font(size=12)



        def Click(numbers):
            self.first_number = self.entry_1.get()
            self.entry_1.delete(0,END)
            self.entry_1.insert(0,str(self.first_number)+str(numbers))



        def C():
            self.entry_1.delete(0,END)

        def divided():
            self.first_number = self.entry_1.get()


            self.f_num = self.first_number
            self.math = "Divided"
            self.entry_1.delete(0,END)

        def multiplying():
            self.first_number = self.entry_1.get()


            self.math = "Multiply"
            self.f_num = self.first_number
            self.entry_1.delete(0,END)

        def add():
            self.first_number = self.entry_1.get()


            self.math = "Adding"
            self.f_num = self.first_number
            self.entry_1.delete(0,END)

        def minus():
            self.first_number = self.entry_1.get()
            global f_num

            self.f_num = self.first_number
            self.math = "Minus"
            self.entry_1.delete(0,END)

        def equal():
            self.second_number = self.entry_1.get()
            self.entry_1.delete(0,END)

            if self.math == "Minus":
                self.entry_1.insert(0,float(self.f_num)-float(self.second_number))

            if self.math == "Adding":
                self.entry_1.insert(0, float(self.f_num) + float(self.second_number))

            if self.math == "Multiply":
                self.entry_1.insert(0,float(self.f_num) * float(self.second_number))

            if self.math == "Divided":
                self.entry_1.insert(0, float(self.f_num) / float(self.second_number))




        # Set Buttons


        self.buton_1 = Button(Master,text=1,padx=30,pady=15, bg='#0052cc',fg='#ffffff',command=lambda: Click(1))
        self.buton_1['font']=myfont
        self.buton_2 = Button(Master, text=2,padx=30,pady=15,bg='#0052cc',fg='#ffffff',  command=lambda: Click(2))
        self.buton_2['font'] = myfont
        self.buton_3 = Button(Master, text=3,padx=30,pady=15,bg='#0052cc',fg='#ffffff', command=lambda: Click(3))
        self.buton_3['font'] = myfont

        self.buton_4 = Button(Master, text=4,padx=30,pady=15,bg='#0052cc',fg='#ffffff',  command=lambda: Click(4))
        self.buton_4['font'] = myfont
        self.buton_5 = Button(Master, text=5,padx=30,pady=15,bg='#0052cc',fg='#ffffff',  command=lambda: Click(5))
        self.buton_5['font'] = myfont
        self.buton_6 = Button(Master, text=6,padx=30,pady=15,bg='#0052cc',fg='#ffffff',  command=lambda: Click(6))
        self.buton_6['font'] = myfont

        self.buton_7 = Button(Master, text=7,padx=30,pady=15, bg='#0052cc',fg='#ffffff', command=lambda: Click(7))
        self.buton_7['font'] = myfont
        self.buton_8 = Button(Master, text=8,padx=30,pady=15, bg='#0052cc',fg='#ffffff', command=lambda: Click(8))
        self.buton_8['font'] = myfont
        self.buton_9 = Button(Master, text=9,padx=30,pady=15,bg='#0052cc',fg='#ffffff', command=lambda: Click(9))
        self.buton_9['font'] = myfont

        self.buton_0 = Button(Master, text=0, padx=30,pady=15 ,bg='#0052cc',fg='#ffffff',command=lambda: Click(0))
        self.buton_0['font'] = myfont

        self.divide= Button(Master,text='/',padx=29,pady=15,bg='#FF4040',command=divided )
        self.divide['font'] = myfont

        self.multiply = Button(Master,text="*",padx=29,pady=15,bg='#FF4040',command=multiplying )
        self.multiply['font'] = myfont

        self.adding = Button(Master,text="+",padx=28,pady=15,bg='#FF4040',command=add )
        self.adding['font'] = myfont

        self.minus = Button(Master, text='-',padx=30,pady=15,bg='#FF4040',command=minus )
        self.minus['font'] = myfont

        self.clear=Button(Master,text="C",padx=28,pady=15,bg='#FF4040',command=C)
        self.clear['font'] = myfont

        self.equal = Button(Master, text='=',padx=30,pady=15,bg='#FF4040',command=equal )
        self.equal['font'] = myfont

        # Set Buttons


        # Set button in  places

        self.entry_1.grid(row=0,column=1,columnspan=2,padx=15,pady=30)

        self.buton_1.grid(row=4,column=0)
        self.buton_2.grid(row=4,column=1)
        self.buton_3.grid(row=4,column=2)

        self.buton_4.grid(row=3,column=0)
        self.buton_5.grid(row=3,column=1)
        self.buton_6.grid(row=3,column=2)

        self.buton_7.grid(row=2,column=0)
        self.buton_8.grid(row=2,column=1)
        self.buton_9.grid(row=2,column=2)

        self.buton_0.grid(row=5,column=1)

        self.clear.grid(row=5,column=0)
        self.equal.grid(row=5,column=2)
        self.minus.grid(row=5,column=3)
        self.adding.grid(row=4,column=3)
        self.multiply.grid(row=3,column=3)
        self.divide.grid(row=2,column=3)

        # Set button in  places


root = Tk()
calculator = Simple_calculator(root)
root.mainloop()













