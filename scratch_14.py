import tkinter as tk
from tkinter import *
import csv
from tkinter import messagebox
window=tk.Tk()
window.config(background="black")

Label(window,text="COVID-19 HOTSPOT AREA ALERT",font=("Algerian",24,"bold"),bg="black",fg="red").pack()
entry=tk.Entry(window)
entry.pack()
window.geometry("1020x1020")
tk.Label(text="Welcome!!")


'''CSV FILE READING AND IMPLEMENTATION'''


cssv=open('covid_19_india.csv')
lines=cssv.readlines()
def button_click():
    count=0
    t=entry.get()
    if t=="":
        messagebox.showinfo("Oops!!!!","You did'nt enter the location!")
    else:
        k=0
        for i in range(1,1223,1):
            txt=lines[i].split(",")
            if t==txt[3]:
                count=1
                k=int(k)+int(txt[8])
        if count!=0:
            if k==0:
                answer1=messagebox.showinfo("Alert",t+" is a safe area with"+str(k)+"cases")
                if(answer1):
                    window.quit()
            if k<15:
                answer2=messagebox.showinfo("Alert!!",t+" is under moderate danger.\nYou are in orange zone.\nThere are total"+str(k)+"cases.")
                if (answer2):
                    window.quit()

            if k>15:
                answer3=messagebox.showinfo("Alert",t+" is having exploding no. of Covid-19 cases.\nYou are in red zone.\nThere are total "+str(k)+"cases.")
                if (answer3):
                    window.quit()

label1=tk.Label(window,text="Enter The State You Want To Check In\n#example:Assam,West Bengal,etc...",fg="white",font=("Britannic bold",13,"bold"),bg="black")
submit_button=Button(window,text="SUBMIT",command=button_click,bg="#E6E914",fg="black").pack()


label1.pack()

'''IMAGE'''

c=Canvas(window,width=220,height=120,bg='#C0C0C0')
c.pack()

photo=PhotoImage(file=r"Screenshot (62).png")
c.create_image(0,0,image=photo,anchor=NW)

'''CAPTION'''

tk.Label(window,text="Stay at home,a wise man said.\n Vijay did'nt obey this and went out like a nicompoop.\nHe is dead now.\nDon't be like Vijay.",font=("chiller",40,),bg="black",fg="#E6E914").pack()

'''CLOSE WINDOW'''

window.mainloop()