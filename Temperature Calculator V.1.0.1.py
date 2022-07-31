from cProfile import label
from calendar import c
from re import T
import tkinter as tk
from tkinter import CENTER, LEFT, RIGHT, Frame, ttk
from turtle import left
from typing import Text

from setuptools import Command
window = tk.Tk()
window.title("Temperature Calculator V.1.0.0")
window.geometry("1100x600")
labeltotal = tk.Label(window, text="TEMPERATURE & HEAT CALCULLATOR", font=('Helvetica', 12, "bold"))
labeltotal.pack(side=tk.TOP, pady=25)


#Celcius TEMPT-----------------------------------------------------------
def celfahh():
    drjcf = txtbox1.get()
    celfah = (float(drjcf)*9/5)+32
    txtoutput.set(f"From {drjcf} °C to "+str(celfah) + "°F")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="green")
def celrea():
    drjcr = txtbox1.get()
    celrea = float(drjcr)*4/5
    txtoutput.set(f"From {drjcr} °C to "+str(celrea) + "°R")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="green")
def celkel():
    drjck = txtbox1.get()
    celkel = float(drjck)+273
    txtoutput.set(f"From {drjck} °C to "+str(celkel) + "°K")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="green")
def celall():
    drjcall = txtbox1.get()
    celfah = float(drjcall)+273
    celrea = float(drjcall)*4/5
    celkel = float(drjcall)+273
    txtoutput.set(f"From {drjcall} °C to: \n"f"        Fahrenheit = {str(celfah)}°F \n"f"        Reamur      = {str(celrea)}°R\n"f"        Kelvin         = {str(celkel)}°K\n")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="green", justify=LEFT)
#Fahrenheit Tempt--------------------------------------------------------
def fahcel():
    drj = txtbox2.get()
    fahcel = (float(drj)-32)*5/9
    txtoutput.set(f"From {drj} °F to "+str(fahcel) + "°C")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="brown")
def fahrea():
    drj = txtbox2.get()
    fahcel = (float(drj)-32)*4/9
    txtoutput.set(f"From {drj} °F to "+str(fahcel) + "°R")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="brown")
def fahkel():
    drj = txtbox2.get()
    fahcel = ((float(drj)-32)*5/9)+273
    txtoutput.set(f"From {drj} °F to "+str(fahcel) + "°K")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="brown")
def fahall():
    drj = txtbox2.get()
    fahcel1 = (float(drj)-32)*5/9
    fahrea = (float(drj)-32)*4/9
    fahkel = ((float(drj)-32)*5/9)+273
    txtoutput.set(f"From {drj} °F to: \n"f"        Celcius       = {str(fahcel1)}°C \n"f"        Reamur      = {str(fahrea)}°R\n"f"        Kelvin         = {str(fahkel)}°K\n")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="brown", justify=LEFT)
#Reamur TEMPT------------------------------------------------------------
def reacel():
    drj = txtbox3.get()
    reacel = float(drj)*5/4
    txtoutput.set(f"From {drj} °R to "+str(reacel) + "°C")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="brown")
def reafah():
    drj = txtbox3.get()
    reafah = (float(drj)*9/4)+32
    txtoutput.set(f"From {drj} °R to "+str(reafah) + "°F")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="brown")
def reakel():
    drj = txtbox3.get()
    reakel = (float(drj)*5/4)+273
    txtoutput.set(f"From {drj} °R to "+str(reakel) + "°K")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="brown")
def reaall():
    drj = txtbox3.get()
    reacel = (float(drj))*5/4
    reafah = (float(drj)*9/4)+32
    reakel = (float(drj)*5/4)+273
    txtoutput.set(f"From {drj} °R to: \n"f"        Celcius       = {str(reacel)}°C \n"f"        Fahrenheit = {str(reafah)}°F\n"f"        Kelvin         = {str(reakel)}°K\n")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="brown", justify=LEFT)
#Kelvin TEMPT------------------------------------------------------------
def kelcel():
    drj = txtboxk.get()
    kelcel = float(drj)-273
    txtoutput.set(f"From {drj} °K to "+str(kelcel) + "°C")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="purple")
def kelfah():
    drj = txtboxk.get()
    kelfah = ((float(drj)-273)*9/5)+32
    txtoutput.set(f"From {drj} °R to "+str(kelfah) + "°F")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="purple")
def kelrea():
    drj = txtboxk.get()
    kelrea = (float(drj)-273)*4/5
    txtoutput.set(f"From {drj} °R to "+str(kelrea) + "°R")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="purple")
def kelall():
    drj = txtboxk.get()
    kelcel = float(drj)-273
    kelfah = ((float(drj)-273)*9/5)+32
    kelrea = (float(drj)-273)*4/5
    txtoutput.set(f"From {drj} °K to: \n"f"        Celcius        = {str(kelcel)}°C \n"f"        Fahrenheit  = {str(kelfah)}°F\n"f"        Reamur       = {str(kelrea)}°R\n")
    labeloutputtempt.config(font=('Helvetica', 12, "bold"),fg="purple", justify=LEFT)

#frametotal--------------------------------------------------------------
frametotal = tk.Frame(window)
frametotal.pack(fill=tk.BOTH, side=LEFT)
#judul atas untuk temptcalculator----------------------------------------
labeltempt = tk.Label(frametotal,text="Temperature Calculator", font=('Helvetica', 12, "bold"))
labeltempt.pack(pady=4)

#frame 1-----------------------------------------------------------------
frame1 = tk.Frame(frametotal)
frame1.pack(fill=tk.X, pady=7)
#Judul kiri
label1 = tk.Label(frame1,width=15,text="Celcius",font=('MS Sans Serif', 12, "bold"))
label1.pack(side=tk.LEFT, padx=8)
#TextBuatinput
txtbox1 = ttk.Entry(frame1,font=('MS Sans Serif', 10, "bold"))
txtbox1.pack(side=tk.LEFT, padx=5)
#Tombol1
btn1 = tk.Button(frame1, text= "F", font=('MS Sans Serif',12, "bold"), command=celfahh)
btn1.pack(side=tk.LEFT, padx=5)
btn2 = tk.Button(frame1, text= "R", font=('MS Sans Serif',12, "bold"), command=celrea)
btn2.pack(side=tk.LEFT, padx=5)
btn3 = tk.Button(frame1, text= "K", font=('MS Sans Serif',12, "bold"), command=celkel)
btn3.pack(side=tk.LEFT, padx=5)
btn4 = tk.Button(frame1, text= "All", font=('MS Sans Serif',12, "bold"), command=celall)
btn4.pack(side=tk.LEFT, padx=5)

#frame 2-----------------------------------------------------------------
frame2 = tk.Frame(frametotal)
frame2.pack(fill=tk.X, pady=7)
#Judul kiri
label2 = tk.Label(frame2,width=15 ,text="Fahrenheit",font=('MS Sans Serif', 12, "bold"))
label2.pack(side=tk.LEFT, padx=8)
txtbox2 = ttk.Entry(frame2,font=('MS Sans Serif', 10, "bold"))
txtbox2.pack(side=tk.LEFT, padx=5)
#Tombol2
btnf1 = tk.Button(frame2, text= "C", font=('MS Sans Serif',12, "bold"), command=fahcel)
btnf1.pack(side=tk.LEFT, padx=5)
btnf2 = tk.Button(frame2, text= "R", font=('MS Sans Serif',12, "bold"), command=fahrea)
btnf2.pack(side=tk.LEFT, padx=5)
btnf3 = tk.Button(frame2, text= "K", font=('MS Sans Serif',12, "bold"), command=fahkel)
btnf3.pack(side=tk.LEFT, padx=5)
btnf4 = tk.Button(frame2, text= "All", font=('MS Sans Serif',12, "bold"), command=fahall)
btnf4.pack(side=tk.LEFT, padx=5)

#frame 3-----------------------------------------------------------------
frame3 = tk.Frame(frametotal)
frame3.pack(fill=tk.X, pady=7)
#Judul kiri
label3 = tk.Label(frame3,width=15 ,text="Reamur",font=('MS Sans Serif', 12, "bold"))
label3.pack(side=tk.LEFT, padx=8)
txtbox3 = ttk.Entry(frame3,font=('MS Sans Serif', 10, "bold"))
txtbox3.pack(side=tk.LEFT, padx=5)
#Tombol2
btnr1 = tk.Button(frame3, text= "C", font=('MS Sans Serif',12, "bold"), command=reacel)
btnr1.pack(side=tk.LEFT, padx=5)
btnr2 = tk.Button(frame3, text= "F", font=('MS Sans Serif',12, "bold"), command=reafah)
btnr2.pack(side=tk.LEFT, padx=5)
btnr3 = tk.Button(frame3, text= "K", font=('MS Sans Serif',12, "bold"), command=reakel)
btnr3.pack(side=tk.LEFT, padx=5)
btnr4 = tk.Button(frame3, text= "All", font=('MS Sans Serif',12, "bold"), command=reaall)
btnr4.pack(side=tk.LEFT, padx=5)

#frame k-----------------------------------------------------------------
framek = tk.Frame(frametotal)
framek.pack(fill=tk.X, pady=7)
#Judul kiri
labelk = tk.Label(framek,width=15 ,text="Kelvin",font=('MS Sans Serif', 12, "bold"))
labelk.pack(side=tk.LEFT, padx=8)
txtboxk = ttk.Entry(framek,font=('MS Sans Serif', 10, "bold"))
txtboxk.pack(side=tk.LEFT, padx=5)
#Tombol2
btnr1 = tk.Button(framek, text= "C", font=('MS Sans Serif',12, "bold"), command=kelcel)
btnr1.pack(side=tk.LEFT, padx=5)
btnr2 = tk.Button(framek, text= "F", font=('MS Sans Serif',12, "bold"), command=kelfah)
btnr2.pack(side=tk.LEFT, padx=5)
btnr3 = tk.Button(framek, text= "K", font=('MS Sans Serif',12, "bold"), command= kelrea)
btnr3.pack(side=tk.LEFT, padx=5)
btnr4 = tk.Button(framek, text= "All", font=('MS Sans Serif',12, "bold"), command= kelall)
btnr4.pack(side=tk.LEFT, padx=5)

#frame output------------------------------------------------------------
frameoutput = tk.Frame(frametotal)
frameoutput.pack(fill=tk.X, pady=7)
#textoutput--------------------------------------------------------------
txtoutput = tk.StringVar() #biartext "OUTPUT" Bisa berubah
txtoutput.set(" ")
labeloutputtempt = tk.Label(frameoutput, font=('Helvetica', 12, "bold"), textvariable=txtoutput)
labeloutputtempt.pack(side=tk.LEFT, padx=15)


#HEAT CALCULATORRRR------------------------------------------------------
def heat():
    mazz = txt1.get()
    clow = txt4.get()
    deltat = txt5.get()
    heatzz = (float(mazz))*(float(clow))*(float(deltat))
    txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
    labeloutputtempt2.config(font=('Helvetica', 12, "bold"),fg="#953241")
def capacity1():
    heatz = txt3.get()
    deltat = txt5.get()
    capacityz1 = (float(heatz))/(float(deltat))
    txtoutput2.set(f"The Heat Capcity is "+ str(capacityz1) + " Joule/°C")
    labeloutputtempt2.config(font=('Helvetica', 12, "bold"),fg="#BF4095")
def capacity2():
    mazz = txt1.get()
    clow = txt4.get()
    capacityz2 = (float(mazz))*(float(clow))
    txtoutput2.set(f"The Heat Capacity is "+ str(capacityz2) + " Joule/°C")
    labeloutputtempt2.config(font=('Helvetica', 12, "bold"),fg="#BF4095")
def spcheat1():
    mazz = txt1.get()
    deltat = txt5.get()
    heatz = txt3.get()
    spcheatz1 = (float(heatz))/((float(mazz))*(float(deltat)))
    txtoutput2.set(f"The Specific Capacity is "+ str(spcheatz1) + " Joule/Kg°C")
    labeloutputtempt2.config(font=('Helvetica', 12, "bold"),fg="#C65BC8")
def spcheat2():
    mazz = txt1.get()
    cbig = txt2.get()
    spcheatz2 = (float(cbig))/(float(mazz))
    txtoutput2.set(f"The Specific Capcity is "+ str(spcheatz2) + " Joule/Kg°C")
    labeloutputtempt2.config(font=('Helvetica', 12, "bold"),fg="#C65BC8")
def deltaT1():
    heatz = txt3.get()
    mazz = txt1.get()
    clow = txt4.get()
    deltaTz1 = (float(heatz))/((float(mazz))*(float(clow)))
    txtoutput2.set(f"The Temperature Change is "+ str(deltaTz1) + " °C")
    labeloutputtempt2.config(font=('Helvetica', 12, "bold"),fg="#32957B")
def deltaT2():
    cbig = txt2.get()
    heatz = txt3.get()
    deltaTz2 = (float(heatz))/(float(cbig))
    txtoutput2.set(f"The Temperature Change is "+ str(deltaTz2) + " °C")
    labeloutputtempt2.config(font=('Helvetica', 12, "bold"),fg="#32957B")
def intructions():
    txtoutput2.set(f"Formula list: \nQ = mc△T\nC = Q/(△T)     or     C2 = mc\nc = Q/(m△T)     or     c2 = C/m\n△T= (T2 – T1)     or     △T1 = Q/mc     or      △T2 = Q/C\nNote: you only have to input numbers in the formula's variable!!")
    labeloutputtempt2.config(font=('Helvetica', 12, "bold"),fg="#826E2B")    

#FRAMETOTAL 2 FOR HEAT CALCULATOR----------------------------------------
frametotal2 = tk.Frame(window)
frametotal2.pack(fill=tk.BOTH, side=LEFT, padx=40)
#judul atas untuk temptcalculator----------------------------------------
labeltempt = tk.Label(frametotal2,text="Heat Calculator", font=('Helvetica', 12, "bold"), justify=CENTER)
labeltempt.pack()

#frame 4-----------------------------------------------------------------
frame4 = tk.Frame(frametotal2)
frame4.pack(fill=tk.X, pady=7)
#mass input
lbl1 = tk.Label(frame4,width=15,text="Mass (M)",font=('MS Sans Serif', 12, "bold"))
lbl1.pack(side=tk.LEFT, padx=8)
txt1 = ttk.Entry(frame4,font=('MS Sans Serif', 10, "bold"))
txt1.pack(side=tk.LEFT, padx=5)
lbl11 = tk.Label(frame4,text="(Kg)",font=('MS Sans Serif', 12, "bold"))
lbl11.pack(side=tk.LEFT, padx=8)
#frame 5-----------------------------------------------------------------
frame5 = tk.Frame(frametotal2)
frame5.pack(fill=tk.X, pady=7)
#heatcapacity input
lbl2 = tk.Label(frame5,width=15,text="Heat Capacity (C)",font=('MS Sans Serif', 12, "bold"))
lbl2.pack(side=tk.LEFT, padx=8)
txt2 = ttk.Entry(frame5,font=('MS Sans Serif', 10, "bold"))
txt2.pack(side=tk.LEFT, padx=5)
lbl12 = tk.Label(frame5,text="(Joule/°C)",font=('MS Sans Serif', 12, "bold"))
lbl12.pack(side=tk.LEFT, padx=8)
#frame 6-----------------------------------------------------------------
frame6 = tk.Frame(frametotal2)
frame6.pack(fill=tk.X, pady=7)
#heat input
lbl3 = tk.Label(frame6,width=15,text="Heat (Q)",font=('MS Sans Serif', 12, "bold"))
lbl3.pack(side=tk.LEFT, padx=8)
txt3 = ttk.Entry(frame6,font=('MS Sans Serif', 10, "bold"))
txt3.pack(side=tk.LEFT, padx=5)
lbl13 = tk.Label(frame6,text="(Joule)",font=('MS Sans Serif', 12, "bold"))
lbl13.pack(side=tk.LEFT, padx=8)
#frame 7-----------------------------------------------------------------
frame7 = tk.Frame(frametotal2)
frame7.pack(fill=tk.X, pady=7)
#specific heat input
lbl4 = tk.Label(frame7,width=15,text="Specific Heat (c)",font=('MS Sans Serif', 12, "bold"))
lbl4.pack(side=tk.LEFT, padx=8)
txt4 = ttk.Entry(frame7,font=('MS Sans Serif', 10, "bold"))
txt4.pack(side=tk.LEFT, padx=5)
lbl14 = tk.Label(frame7,text="(Joule/Kg°C)",font=('MS Sans Serif', 12, "bold"))
lbl14.pack(side=tk.LEFT, padx=8)
#frame 8-----------------------------------------------------------------
frame8 = tk.Frame(frametotal2)
frame8.pack(fill=tk.X, pady=7)
#delta t input
lbl5 = tk.Label(frame8,width=22,text="Temperature Change (△T)",font=('Helvetica', 9, "bold"))
lbl5.pack(side=tk.LEFT, padx=7.5)
txt5 = ttk.Entry(frame8,font=('MS Sans Serif', 10, "bold"))
txt5.pack(side=tk.LEFT, padx=3)
lbl15 = tk.Label(frame8,text="(°C)",font=('MS Sans Serif', 12, "bold"))
lbl15.pack(side=tk.LEFT, padx=8)

#frame 9-----------------------------------------------------------------
frame9 = tk.Frame(frametotal2)
frame9.pack(fill=tk.X, pady=7)
#text search
lbl9 = tk.Label(frame9,width=15,text="Search: ",font=('Helvetica', 12, "bold"))
lbl9.pack(side=tk.LEFT, padx=7.5)
#button in fram 8
bt1 = tk.Button(frame9, text= "Q", font=('Helvetica',12, "bold"), command=heat)
bt1.pack(side=tk.LEFT, padx=5)
bt2 = tk.Button(frame9, text= "C", font=('Helvetica',12, "bold"), command=capacity1)
bt2.pack(side=tk.LEFT, padx=5)
bt3 = tk.Button(frame9, text= "c", font=('Helvetica',12, "bold"), command=spcheat1)
bt3.pack(side=tk.LEFT, padx=5)
bt4 = tk.Button(frame9, text= "△T1", font=('Helvetica',12, "bold"), command=deltaT1)
bt4.pack(side=tk.LEFT, padx=5)

#frame 10-----------------------------------------------------------------
frame10 = tk.Frame(frametotal2)
frame10.pack(fill=tk.X, pady=7)
#text search
lbl10 = tk.Label(frame10,width=15,text=" ",font=('Helvetica', 12, "bold"))
lbl10.pack(side=tk.LEFT, padx=7.5)
#button in fram 8
bt5 = tk.Button(frame10, text= "C2", font=('Helvetica',12, "bold"), command=capacity2)
bt5.pack(side=tk.LEFT, padx=5)
bt6 = tk.Button(frame10, text= "c2", font=('Helvetica',12, "bold"), command=spcheat2)
bt6.pack(side=tk.LEFT, padx=5)
bt7 = tk.Button(frame10, text= "△T2", font=('Helvetica',12, "bold"), command=deltaT2)
bt7.pack(side=tk.LEFT, padx=5)
bt8 = tk.Button(frame10, text= "Instructions", font=('Helvetica',12, "bold"), command= intructions)
bt8.pack(side=tk.LEFT, padx=5)

#frame 11 OUTPUTTT----------------------------------------------------------
frame11 = tk.Frame(frametotal2)
frame11.pack(fill=tk.X, pady=7)
#textoutput
txtoutput2 = tk.StringVar() #biartext "OUTPUT" Bisa berubah
txtoutput2.set(" ")
labeloutputtempt2 = tk.Label(frame11, font=('Helvetica', 12, "bold"), textvariable=txtoutput2)
labeloutputtempt2.pack(side=tk.LEFT, padx=15)

#to RUNNN-------------------------------------------------------------------
window.mainloop()