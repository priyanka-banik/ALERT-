import tkinter as tk
from tkinter import *
import csv
from tkinter import messagebox
window=tk.Tk()
window.config(background="black")

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
                answer1=messagebox.showinfo("Alert",t+" is a safe area with"+str(k)+"cases")
                if(answer1):
                    window.quit()
            if k<15:
                answer2=messagebox.showinfo("Alert",t+" is under moderate danger.\nYou are in orange zone.\nThere are total "+str(k)+"cases.")
                if (answer2):
                    window.quit()

            if k>15:
                answer3=messagebox.showwarning("Alert",t+" is having exploding no. of Covid-19 cases.\nYou are in red zone.\nThere are total "+str(k)+"cases.")
                if (answer3):
                    window.quit()
        if count==0:
            answer4=messagebox.showinfo("Alert","OOPS!!\n This location not found.")
            if(answer4):
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

tk.Label(window,text="Stay at home,a wise man said.\n Vijay did'nt obey this and went out like a nicompoop.\nHe is dead now.\nDon't be like Vijay.",font=("chiller",60,),bg="black",fg="#E6E914").pack()


'''EXITING WINDOW'''



'''CLOSE WINDOW'''
def Button1():
	answer5=messagebox.showinfo("Symptoms","Common symptoms:\n->fever.\n->tiredness.\n->dry cough.\n**Some people may experience:\n->aches and pains.\n->nasal congestion.\n->runny nose.\n->sore throat.\n->diarrhoea.\nOn average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.People with mild symptoms who are otherwise healthy should isolate themselves. Seek medical attention if you have a fever, a cough, and difficulty breathing. Call ahead.")
	if(answer5):
		window.quit
tk.Label(window,text="Stay at home,a wise man said.\n Vijay did'nt obey this and went out like a nicompoop.\nHe is dead now.\nDon't be like Vijay.",font=("chiller",40,),bg="black",fg="#E6E914").pack()
tk.Label(window,text="",bg="black").pack()
Button1=Button(window,text="Symptoms",command=Button1)
Button1.pack()
def Button2():
	answer6=messagebox.showinfo("Precautions","*Wash your hands often with soap and water for at least 20 seconds, especially after going to the bathroom; before eating; and after blowing your nose, coughing, or sneezing.\n* If soap and water are not readily available, use an alcohol-based hand sanitizer with at least 60% alcohol. Always wash hands with soap and water if hands are visibly dirty.\n* Avoid touching your eyes, nose, and mouth with unwashed hands.Avoid close contact with people who are sick.\n* Stay home when you are sick.\n ")
tk.Label(window,text="",bg="black").pack()
Button2=Button(window,text="Precautions",command=Button2)
Button2.pack()
def ask1():
    answer0=messagebox.askyesnocancel("exit","Do You Really Want To Exit?")
    if answer0==True:
        window.quit()
b2=Button(window,text="EXIT",command=ask1,font=("Algerian",20),bg="GREY",fg="black").pack(side=BOTTOM)

window.mainloop()
