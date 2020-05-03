import tkinter as tk
import webbrowser
from tkinter import *
import csv
import webbrowser
from tkinter import messagebox
window=tk.Tk()
window.config(background="BLACK")

Label(window,text="COVID-19 HOTSPOT AREA ALERT",font=("Algerian",45,"bold"),bg="black",fg="red").pack()
entry=tk.Entry(window,borderwidth=5)
entry.pack()
window.title("Covid Alert")
window.geometry("1020x1020")
tk.Label(text="Welcome!!")
window.iconbitmap('icon.ico')


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
                k=int(txt[8])
        if count!=0:
            if k==0:
                messagebox.showinfo("Alert",t+" is a safe area with"+str(k)+" cases")
            if k<15:
                messagebox.showinfo("Alert",t+" is under moderate danger.\n\nYou are in orange zone.\n\nThere are total "+str(k)+" cases.")
            if k>15:
                messagebox.showinfo("Alert",t+" is having exploding no. of Covid-19 cases.\n\nYou are in red zone.\n\nThere are total "+str(k)+" cases.")
        if count==0:
            messagebox.showinfo("Alert","OOPS!!\n This location not found.")
label1=tk.Label(window,text="Enter The State You Want To Check In\n#example:Assam,West Bengal,etc...\n",fg="white",font=("Britannic bold",13,"bold"),bg="black")
submit_button=Button(window,text="SUBMIT",command=button_click,bg="#E6E914",fg="black").pack()


label1.pack()

'''IMAGE'''

c=Canvas(window,width=220,height=120,bg='#C0C0C0')
c.pack()

photo=PhotoImage(file=r"Screenshot (62).png")
c.create_image(0,0,image=photo,anchor=NW)

'''CAPTION'''

tk.Label(window,text="Stay at home,a wise man said.\n Vijay did'nt obey this and went out like a nicompoop.\nHe is dead now.\nDon't be like Vijay.",font=("chiller",60,),bg="black",fg="#E6E914").pack()


'''EXITING WINDOW'''



'''CLOSE WINDOW'''
url='https://www.cdc.gov/coronavirus/2019-ncov/symptoms-testing/symptoms.html'
def Button1():
	webbrowser.open_new(url)
Button1=Button(window,text="SYMPTOMS",font=("Algerian",20),bg="#1B2631",fg="WHITE",command=Button1)
Button1.pack(side=LEFT)

url1='https://www.cdc.gov/coronavirus/2019-ncov/prevent-getting-sick/prevention.html'
def Button2():
	webbrowser.open_new(url1)
Button2=Button(window,text="PRECAUTIONS",font=("Algerian",20),bg="#1B2631",fg="WHITE",command=Button2)
Button2.pack(side=LEFT)

#url2='https://www.worldometers.info/coronavirus/#countries'
#def Button3():
#	webbrowser.open_new(url2)
 #   Button3.pack()
url2='https://www.worldometers.info/coronavirus/#countries'
def Button3():
	webbrowser.open_new(url2)
Button3=Button(window,text="Covid-19 Updated Data",font=("Algerian",20),bg="#1B2631",fg="WHITE",command=Button3)
Button3.pack(side=LEFT)


def ask1():
    answer0=messagebox.askyesnocancel("Exit","Do You Really Want To Exit?")
    if answer0==True:
        window.quit()
b2=Button(window,text="EXIT",command=ask1,font=("Algerian",20),bg="#1B2631",fg="WHITE").pack(side=LEFT)

window.mainloop()
