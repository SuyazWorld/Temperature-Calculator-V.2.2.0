from cgitb import text
from multiprocessing.sharedctypes import Value
from optparse import Option
import tkinter as tk
from tkinter import CENTER, LEFT, RIGHT, Frame, ttk
from tkinter import font
from turtle import left

#total frame
window = tk.Tk()
window.title("Temperature Calculator V.2.0.0")
window.geometry("800x770")

#judul atas
labeltotal = tk.Label(window, text="TEMPERATURE & HEAT CALCULLATOR", font=('Arial', 16, "bold"))
labeltotal.pack(side=tk.TOP, pady=18)

"""

TEMPERATUREEE CALCULATORRRRRRRRRRRRRRRRR

"""

#frametempttile------------------------------------------------------------
frametempt = tk.Frame(window)
frametempt.pack(fill=tk.BOTH, side=tk.TOP)
#judul atas untuk temptcalculator
labeltempt = tk.Label(frametempt,text="Temperature Calculator", font=('Arial', 14, "bold"), justify=CENTER, fg="green")
labeltempt.pack(pady=6)

#frame 1-----------------------------------------------------------------
frame1 = tk.Frame(window)
frame1.pack(fill=tk.Y, pady=7)
#text input number
labelinputnumber = tk.Label(frame1,width=15,text="Input Degree Here:",font=('Arial', 10, "bold"))
labelinputnumber.pack(side=tk.LEFT, padx=8)
#entry box paling awal
txtbox1 = ttk.Entry(frame1,width=6,font=('Arial ', 10, "bold"), justify=CENTER)
txtbox1.pack(side=tk.LEFT, padx=8)

#frame2-----------------------------------------------------------------
frame2 = tk.Frame(window)
frame2.pack(fill=tk.Y, pady=7)
#string variable 1 untuk menampung nilai variable 1
strvarcb1=tk.StringVar()
strvarcb1.set("Celcius")
#text from
labelfrom = tk.Label(frame2,width=4,text="From:",font=('Arial', 10, "bold"))
labelfrom.pack(side=tk.LEFT, padx=5)
#combobox1
option1 = ["Celcius", "Fahrenheit","Reamur","Kelvin"]
combo1 = ttk.Combobox(frame2, values=option1, textvariable=strvarcb1, font=("Arial",10,"bold")) #textvarible= fungsi untuk naruh strvar
combo1.pack(side=tk.LEFT, padx=5)
#string variable 1 untuk menampung nilai variable 1
strvarcb2=tk.StringVar()
strvarcb2.set("Celcius")
#text to
labelto = tk.Label(frame2,width=4,text="To:",font=('Arial', 10, "bold"))
labelto.pack(side=tk.LEFT, padx=5)
#combobox1
option2 = ["Celcius", "Fahrenheit","Reamur","Kelvin", "All"]
combo2 = ttk.Combobox(frame2, values=option2, textvariable=strvarcb2, font=("Arial",10,"bold"))
combo2.pack(side=tk.LEFT, padx=5)

#TEMPT FUNCTION-------------------------------------------------------------
def temptformula():
    #Celcius
    if(strvarcb1.get()=="Celcius" and strvarcb2.get()=="Fahrenheit"):
        tempt = txtbox1.get()
        celfah = (float(tempt)*9/5)+32
        txtoutput.set(f"From {tempt} °C to "+str(celfah) + "°F")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)
    elif(strvarcb1.get()=="Celcius" and strvarcb2.get()=="Reamur"):
        tempt = txtbox1.get()
        celrea = float(tempt)*4/5
        txtoutput.set(f"From {tempt} °C to "+str(celrea) + "°R")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)
    elif(strvarcb1.get()=="Celcius" and strvarcb2.get()=="Kelvin"):
        tempt = txtbox1.get()
        celkel = float(tempt)+273
        txtoutput.set(f"From {tempt} °C to "+str(celkel) + "°K")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)
    elif(strvarcb1.get()=="Celcius" and strvarcb2.get()=="All"):
        tempt = txtbox1.get()
        celfah = (float(tempt)*9/5)+32
        celrea = float(tempt)*4/5
        celkel = float(tempt)+273
        txtoutput.set(f"\nFrom {tempt}°C to:\n"f"Fahrenheit = {str(celfah)}°F \n"f"Reamur = {str(celrea)}°R\n"f"Kelvin = {str(celkel)}°K\n")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)
    #Reamur
    elif(strvarcb1.get()=="Reamur" and strvarcb2.get()=="Fahrenheit"):
        tempt = txtbox1.get()
        reafah = (float(tempt)*9/4)+32
        txtoutput.set(f"From {tempt} °R to "+str(reafah) + "°F")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)
    elif(strvarcb1.get()=="Reamur" and strvarcb2.get()=="Celcius"):
        tempt = txtbox1.get()
        reacel = (float(tempt))*5/4
        txtoutput.set(f"From {tempt} °R to "+str(reacel) + "°C")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)
    elif(strvarcb1.get()=="Reamur" and strvarcb2.get()=="Kelvin"):
        tempt = txtbox1.get()
        reakel = (float(tempt)*5/4)+273
        txtoutput.set(f"From {tempt} °R to "+str(reakel) + "°K")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)
    elif(strvarcb1.get()=="Reamur" and strvarcb2.get()=="All"):
        tempt = txtbox1.get()
        reacel = (float(tempt))*5/4
        reafah = (float(tempt)*9/4)+32
        reakel = (float(tempt)*5/4)+273
        txtoutput.set(f"\nFrom {tempt}°R to:\n"f"Fahrenheit = {str(reafah)}°F \n"f"Celcius = {str(reacel)}°C\n"f"Kelvin = {str(reakel)}°K\n")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)   
    #Fahrenheit
    elif(strvarcb1.get()=="Fahrenheit" and strvarcb2.get()=="Reamur"):
        tempt = txtbox1.get()
        fahrea = (float(tempt)-32)*4/9
        txtoutput.set(f"From {tempt} °F to "+str(fahrea) + "°R")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)
    elif(strvarcb1.get()=="Fahrenheit" and strvarcb2.get()=="Celcius"):
        tempt = txtbox1.get()
        fahcel = (float(tempt)-32)*5/9
        txtoutput.set(f"From {tempt} °F to "+str(fahcel) + "°C")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)
    elif(strvarcb1.get()=="Fahrenheit" and strvarcb2.get()=="Kelvin"):
        tempt = txtbox1.get()
        fahkel = ((float(tempt)-32)*5/9)+273
        txtoutput.set(f"From {tempt} °F to "+str(fahkel) + "°K")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)
    elif(strvarcb1.get()=="Fahrenheit" and strvarcb2.get()=="All"):
        tempt = txtbox1.get()
        fahcel = (float(tempt)-32)*5/9
        fahrea = (float(tempt)-32)*4/9
        fahkel = ((float(tempt)-32)*5/9)+273
        txtoutput.set(f"\nFrom {tempt}°F to:\n"f"Reamur = {str(fahrea)}°R \n"f"Celcius = {str(fahcel)}°C\n"f"Kelvin = {str(fahkel)}°K\n")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)  
    #Kelvin
    elif(strvarcb1.get()=="Kelvin" and strvarcb2.get()=="Reamur"):
        tempt = txtbox1.get()
        kelrea = (float(tempt)-273)*4/5
        txtoutput.set(f"From {tempt} °K to "+str(kelrea) + "°R")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)
    elif(strvarcb1.get()=="Kelvin" and strvarcb2.get()=="Celcius"):
        tempt = txtbox1.get()
        kelcel = float(tempt)-273
        txtoutput.set(f"From {tempt} °K to "+str(kelcel) + "°C")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)
    elif(strvarcb1.get()=="Kelvin" and strvarcb2.get()=="Fahrenheit"):
        tempt = txtbox1.get()
        kelfah = ((float(tempt)-273)*9/5)+32
        txtoutput.set(f"From {tempt} °K to "+str(kelfah) + "°F")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)
    elif(strvarcb1.get()=="Kelvin" and strvarcb2.get()=="All"):
        tempt = txtbox1.get()
        kelcel = float(tempt)-273
        kelfah = ((float(tempt)-273)*9/5)+32
        kelrea = (float(tempt)-273)*4/5
        txtoutput.set(f"\nFrom {tempt}°K to:\n"f"Reamur = {str(kelrea)}°R \n"f"Celcius = {str(kelcel)}°C\n"f"Fahrenheit = {str(kelfah)}°F")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER) 
    #Else
    else:
        txtoutput.set("Please use diffent unit!\nPlease input the unit that you want use!")
        labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green",justify=CENTER)

#delete output function-----------------------------------------------------
def clearoutput1():
    txtoutput.set("")
    labeloutputtempt.config(font=('Arial', 10, "bold"),fg="green", justify=CENTER)

#frame3---------------------------------------------------------------------
frame3 = tk.Frame(window)
frame3.pack(fill=tk.Y, pady=7)
#button submit to tempt
submittempt = tk.Button(frame3, text="Calculate", font=('Arial',10, "bold"), command=temptformula, justify=CENTER)
submittempt.pack(side=tk.LEFT, padx=7)
#button to clear output 1
cleartempt = tk.Button(frame3, text="Clear", font=('Arial',10, "bold"), command=clearoutput1, justify=CENTER)
cleartempt.pack(side=tk.LEFT, padx=7)

#frame output tempt---------------------------------------------------------
frameoutput = tk.Frame(window)
frameoutput.pack(fill=tk.X, pady=7)
#textoutput tempt
txtoutput = tk.StringVar() #biartext "OUTPUT" Bisa berubah
txtoutput.set(" ")
labeloutputtempt = tk.Label(frameoutput, font=('Helvetica', 12, "bold"), textvariable=txtoutput)
labeloutputtempt.pack(side=tk.TOP, padx=10)

"""

HEATTTTTTT CALCULATORRRRRRRRRRRRRRRRR

"""


#frameheattile------------------------------------------------------------
frameheat = tk.Frame(window)
frameheat.pack(fill=tk.BOTH, side=tk.TOP)
#judul atas untuk temptcalculator
labelheat = tk.Label(frameheat,text="Heat Calculator", font=('Arial', 14, "bold"), justify=CENTER, fg="red")
labelheat.pack(pady=20)

#frame 4 Mass(M)----------------------------------------------------------
frameM = tk.Frame(window)
frameM.pack(fill=tk.BOTH, pady=7, padx=100)
#mass input
lblM = tk.Label(frameM,width=23,text="Mass (M)",font=('Arial', 10, "bold"))
lblM.pack(side=tk.LEFT, padx=8)
txtM = ttk.Entry(frameM,width=6,font=('Arial', 10, "bold"), justify=CENTER)
txtM.pack(side=tk.LEFT, padx=5)
lblM2 = tk.Label(frameM,text="Unit:",font=('Arial', 10, "bold"))
lblM2.pack(side=tk.LEFT, padx=8)
#string variable M untuk menampung unit M
strvarcbm=tk.StringVar()
strvarcbm.set("Kg")
#comboboxM
optionM = ["Kg","Hg","Dag","gr","Dg","Cg","Mg"]
comboM = ttk.Combobox(frameM, values=optionM, width=6,textvariable=strvarcbm, font=("Arial",10,"bold"))
comboM.pack(side=tk.LEFT, padx=5)

#frame 5 Heat Capacity (C)-------------------------------------------------
frameC = tk.Frame(window)
frameC.pack(fill=tk.BOTH, pady=7, padx=100)
#heat capacity input
lblC = tk.Label(frameC,width=23,text="Heat Capacity (C)",font=('Arial', 10, "bold"))
lblC.pack(side=tk.LEFT, padx=8)
txtC = ttk.Entry(frameC,width=6,font=('Arial', 10, "bold"), justify=CENTER)
txtC.pack(side=tk.LEFT, padx=5)
lblC2 = tk.Label(frameC,text="Unit:",font=('Arial', 10, "bold"))
lblC2.pack(side=tk.LEFT, padx=8)
#string variable C untuk menampung unit C
strvarcbc1=tk.StringVar()
strvarcbc1.set("Joule")
strvarcbc2=tk.StringVar()
strvarcbc2.set("°C")
#comboboxC
optionC = ["Joule", "eV","cal","kwh","wh","liter-atmosfer","erg"] #unit pembilang
comboC = ttk.Combobox(frameC,values=optionC, width=6,textvariable=strvarcbc1, font=("Arial",10,"bold"))
comboC.pack(side=tk.LEFT, padx=5)
lblC3 = tk.Label(frameC,text="/",font=('Arial', 10, "bold"))
lblC3.pack(side=tk.LEFT, padx=8)
optionC2 = ["°C", "°R","°F","°K"] #unit penyebut
comboC2 = ttk.Combobox(frameC,values=optionC2, width=6,textvariable=strvarcbc2, font=("Arial",10,"bold"))
comboC2.pack(side=tk.LEFT, padx=5)

#frame 6 Heat (Q)-----------------------------------------------------------
frameQ = tk.Frame(window)
frameQ.pack(fill=tk.BOTH, pady=7, padx=100)
#heat capacity input
lblQ = tk.Label(frameQ,width=23,text="Heat (Q)",font=('Arial', 10, "bold"))
lblQ.pack(side=tk.LEFT, padx=8)
txtQ = ttk.Entry(frameQ,width=6,font=('Arial', 10, "bold"), justify=CENTER)
txtQ.pack(side=tk.LEFT, padx=5)
lblQ2 = tk.Label(frameQ,text="Unit:",font=('Arial', 10, "bold"))
lblQ2.pack(side=tk.LEFT, padx=8)
#string variable Q untuk menampung unit Q
strvarcbq=tk.StringVar()
strvarcbq.set("Joule")
#comboboxQ
optionQ = ["Joule", "eV","cal","kwh","wh","liter-atmosfer","erg"] 
comboQ = ttk.Combobox(frameQ,values=optionQ, width=6,textvariable=strvarcbq, font=("Arial",10,"bold"))
comboQ.pack(side=tk.LEFT, padx=5)

#frame 7 Specific Heat (c)-------------------------------------------------
framecc = tk.Frame(window)
framecc.pack(fill=tk.BOTH, pady=7, padx=100)
#heat capacity input
lblCC = tk.Label(framecc,width=23,text="Specific Heat (c)",font=('Arial', 10, "bold"))
lblCC.pack(side=tk.LEFT, padx=8)
txtCC = ttk.Entry(framecc,width=6,font=('Arial', 10, "bold"), justify=CENTER)
txtCC.pack(side=tk.LEFT, padx=5)
lblCC2 = tk.Label(framecc,text="Unit:",font=('Arial', 10, "bold"))
lblCC2.pack(side=tk.LEFT, padx=8)
#string variable C untuk menampung unit C
strvarcbcc1=tk.StringVar()
strvarcbcc1.set("Joule")
strvarcbcc2=tk.StringVar()
strvarcbcc2.set("Kg")
strvarcbcc3=tk.StringVar()
strvarcbcc3.set("°C")
#comboboxC
optionCC = ["Joule", "eV","cal","kwh","wh","liter-atmosfer","erg"] #unit pembilang
comboCC = ttk.Combobox(framecc,values=optionCC, width=6,textvariable=strvarcbcc1, font=("Arial",10,"bold"))
comboCC.pack(side=tk.LEFT, padx=5)
lblCC3 = tk.Label(framecc,text="/",font=('Arial', 10, "bold")) #text bagi
lblCC3.pack(side=tk.LEFT, padx=8)
optionCC2 = ["Kg","Hg","Dag","gr","Dg","Cg","Mg"] #unit penyebut
comboCC2 = ttk.Combobox(framecc,values=optionCC2, width=6,textvariable=strvarcbcc2, font=("Arial",10,"bold"))
comboCC2.pack(side=tk.LEFT, padx=5)
lblCC4 = tk.Label(framecc,text="*",font=('Arial', 10, "bold")) #text bagi
lblCC4.pack(side=tk.LEFT, padx=8)
optionCC3 = ["°C", "°R","°F","°K"] #unit penyebut
comboCC3 = ttk.Combobox(framecc,values=optionCC3, width=6,textvariable=strvarcbcc3, font=("Arial",10,"bold"))
comboCC3.pack(side=tk.LEFT, padx=5)

#frame 8 Temperature Change (△T)--------------------------------------------
framedt = tk.Frame(window)
framedt.pack(fill=tk.BOTH, pady=7, padx=100)
#heat capacity input
lbldt = tk.Label(framedt,width=23,text="Temperature Change (△T)",font=('Arial', 10, "bold"))
lbldt.pack(side=tk.LEFT, padx=8)
txtdt = ttk.Entry(framedt,width=6,font=('Arial', 10, "bold"), justify=CENTER)
txtdt.pack(side=tk.LEFT, padx=5)
lbldt = tk.Label(framedt,text="Unit:",font=('Arial', 10, "bold"))
lbldt.pack(side=tk.LEFT, padx=8)
#string variable Q untuk menampung unit Q
strvarcbdt=tk.StringVar()
strvarcbdt.set("°C")
#comboboxQ
optiondt = ["°C", "°R","°F","°K"] 
combodt = ttk.Combobox(framedt,values=optiondt, width=6,textvariable=strvarcbdt, font=("Arial",10,"bold"))
combodt.pack(side=tk.LEFT, padx=5)

#Heat FUNCTION-----------------------------------------------------------
def heatcalculated():
    heatbox = txtQ.get()
    heatcap = txtC.get()
    massbox = txtM.get()
    speheat = txtCC.get()
    deltat = txtdt.get()
    #Heat
    if(selectfromuavar.get()=="Q"):
        #joule & C tetap, kg di c
        if(strvarcbm.get()=="Kg" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbdt.get()=="°C"):
            heatzz = (float(massbox))*(float(speheat))*(float(deltat))
            txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
        elif(strvarcbm.get()=="Hg" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbdt.get()=="°C"):
            heatzz = (float(massbox)/10)*(float(speheat))*(float(deltat))
            txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
        elif(strvarcbm.get()=="Dag" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbdt.get()=="°C"):
            heatzz = (float(massbox)/100)*(float(speheat))*(float(deltat))
            txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
        elif(strvarcbm.get()=="gr" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbdt.get()=="°C"):
            heatzz = (float(massbox)/1000)*(float(speheat))*(float(deltat))
            txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
        elif(strvarcbm.get()=="Dg" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbdt.get()=="°C"):
            heatzz = (float(massbox)/10000)*(float(speheat))*(float(deltat))
            txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
        elif(strvarcbm.get()=="Cg" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbdt.get()=="°C"):
            heatzz = (float(massbox)/100000)*(float(speheat))*(float(deltat))
            txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
        elif(strvarcbm.get()=="Mg" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbdt.get()=="°C"):
            heatzz = (float(massbox)/1000000)*(float(speheat))*(float(deltat))
            txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
        #joule & C tetap, Hg di c
        if(strvarcbm.get()=="Kg" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbdt.get()=="°C"):
            heatzz = (float(massbox))*(float(speheat))*(float(deltat))
            txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
        elif(strvarcbm.get()=="Hg" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbdt.get()=="°C"):
            heatzz = (float(massbox)/10)*(float(speheat))*(float(deltat))
            txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
        elif(strvarcbm.get()=="Dag" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbdt.get()=="°C"):
            heatzz = (float(massbox)/100)*(float(speheat))*(float(deltat))
            txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
        elif(strvarcbm.get()=="gr" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbdt.get()=="°C"):
            heatzz = (float(massbox)/1000)*(float(speheat))*(float(deltat))
            txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
        elif(strvarcbm.get()=="Dg" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbdt.get()=="°C"):
            heatzz = (float(massbox)/10000)*(float(speheat))*(float(deltat))
            txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
        elif(strvarcbm.get()=="Cg" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbdt.get()=="°C"):
            heatzz = (float(massbox)/100000)*(float(speheat))*(float(deltat))
            txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
        elif(strvarcbm.get()=="Mg" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbdt.get()=="°C"):
            heatzz = (float(massbox)/1000000)*(float(speheat))*(float(deltat))
            txtoutput2.set(f"The Heat is "+ str(heatzz) + " Joule")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
        
    #heatcapacity1
    elif(selectfromuavar.get()=="C"):
        if(strvarcbq.get()=="Joule" and strvarcbdt.get()=="°C"):
            capacity1 = (float(heatbox))/(float(deltat))
            txtoutput2.set(f"The Heat Capcity is "+ str(capacity1) + " Joule/°C")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
    #heatcapacity2
    elif(selectfromuavar.get()=="C2"):
        if(strvarcbm.get()=="Kg" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C"):
            capacity2 = (float(massbox))*(float(speheat))
            txtoutput2.set(f"The Heat Capcity is "+ str(capacity2) + " Joule/°C")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
    #specificheat1
    elif(selectfromuavar.get()=="c"):
        if(strvarcbq.get()=="Joule" and strvarcbm.get()=="Kg" and strvarcbdt.get()=="°C"):
            spcheatz1 = (float(heatbox))/((float(massbox))*(float(deltat)))
            txtoutput2.set(f"The Specific Capacity is "+ str(spcheatz1) + " Joule/Kg°C")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
    #specificheat2
    elif(selectfromuavar.get()=="c2"):
        if(strvarcbc1.get()=="Joule" and strvarcbc2.get()=="°C"  and strvarcbm.get()=="Kg"):
            spcheatz2 = (float(heatcap))/(float(massbox))
            txtoutput2.set(f"The Specific Capcity is "+ str(spcheatz2) + " Joule/Kg°C")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
    #deltaT1
    elif(selectfromuavar.get()=="△T"):
        if(strvarcbm.get()=="Kg" and strvarcbcc1.get()=="Joule" and strvarcbcc2.get()=="Kg" and strvarcbcc3.get()=="°C" and strvarcbc2.get()=="°C" and strvarcbc2.get()=="°C"):
            deltaTz1 = (float(heatbox))/((float(massbox))*(float(speheat)))
            txtoutput2.set(f"The Temperature Change is "+ str(deltaTz1) + " °C")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
    #deltaT1
    elif(selectfromuavar.get()=="△T2"):
        if(strvarcbc1.get()=="Joule" and strvarcbc2.get()=="°C" and strvarcbq.get()=="Joule" ):
            deltaTz2 = (float(heatbox))/(float(heatcap))
            txtoutput2.set(f"The Temperature Change is "+ str(deltaTz2) + " °C")
            labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red", justify=CENTER)
    else:
        txtoutput2.set("Please enter numbers in the entry according to the formula!\nPlease also select the Right Fomula and Unit!")
        labeloutputtempt2.config(font=('Arial', 12, "bold"),fg="red", justify=CENTER)
def showinstruction():
    txtoutput2.set(f"Formula list: \nQ = mc△T\nC = Q/(△T)     or     C2 = mc\nc = Q/(m△T)     or     c2 = C/m\n△T= (T2 – T1)     or     △T1 = Q/mc     or      △T2 = Q/C\nNote:\nyou only have to input numbers in the formula's variable!!\nyou can see the unit in the show unit button")
    labeloutputtempt2.config(font=('Arial', 12, "bold"),fg="red")
def showunit():
    if (strvarcbt3.get()=="Heat"):
        txtoutput2.set(f"Heat = Joule\n1 joule = 10^7 erg   -------------------------------------------> 1 erg = 10^-7 Joule\n1 joule = 6.241506363 x 10^18 eV (elektronvolt) --------> 1 eV = 0.16021773 x 10^-18 Joule\n1 joule = 0.239 Cal (Calories) -----------------------------> 1 Cal= 4. 1841004 Joule\n1 joule = 2.7778 x 10^-7 kwh (kilowatt-hour) ------------->1 kwh = 0.35999712 x 10^-7 Joule\n1 joule = 2.7778 x 10^-4 wh (watt-hour) -------------------> 1 wh = 0.35999712 x 10^-4 Joule\n1 joule = 9.8692 x 10^-3 liter-atmosfer---------------------> 1 liter-atmosfer = 0.10132533 x 10^-3 Joule")
        labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red")
    elif (strvarcbt3.get()=="Mass"):
        txtoutput2.set(f"Mass = Kg\nHg = 10^-1 Kg\nDag = 10^-2 Kg\ngr = 10^-3 Kg\ndg = 10^-4 Kg\ncg = 10^-5 Kg\nmg = 10^-6 Kg")
        labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red")
    elif (strvarcbt3.get()=="Heat Capacity"):
        txtoutput2.set(f"Heat Capacity = Joule/°C\nYou can see another unit of Joule & °C in Heat & Mass unit")
        labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red")
    elif (strvarcbt3.get()=="Specific Heat"):
        txtoutput2.set(f"Specific Capacity = Joule/Kg°C\nYou can see another unit of Joule, Kg, & °C in Heat, Mass unit, & △T")
        labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red")
    elif (strvarcbt3.get()=="△T"):
        txtoutput2.set(f"Celsius to: Fahrenheit = (9/5) * C + 32, Reamur = (4/5) * C, Kelvin = 273 + C\nReamur to: Fahrenheit = (9/4) * R+ 32, Celsius = (5/4) * R, Kelvin = (5/4) * R + 273\nFahrenheit to: Reamur = (4/9) * (F - 32), Celsius = (5/9) * (F - 32), Kelvin = (5/9) * (F - 32) + 273\nKelvin to: Reamur = (4/5) * (K - 273), Celsius = K – 273, Fahrenheit = (9/5) * (K - 273) + 32")
        labeloutputtempt2.config(font=('Arial', 10, "bold"),fg="red")
    else:
        txtoutput2.set("Please select the Unit!")
        labeloutputtempt2.config(font=('Arial', 12, "bold"),fg="red")
def clearoutputheat():
    txtoutput2.set("")
    labeloutputtempt2.config(font=('Arial', 12, "bold"),fg="red")


#frame 9 button-------------------------------------------------------------
framebt = tk.Frame(window)
framebt.pack(fill=tk.Y, pady=7, padx=100)
#button1 to calculate
bt1 = tk.Button(framebt, text= "Calculate", font=('Arial',10, "bold"), command=heatcalculated)
bt1.pack(side=tk.LEFT, padx=5)
#str var for combobox below
selectfromuavar=tk.StringVar()
selectfromuavar.set("Select Formula")
#combobox of the unit that had been selected
optionbt4 = ["Q", "C","C2","c","c2","△T","△T2"] 
combobt4 = ttk.Combobox(framebt,values=optionbt4, width=14,textvariable=selectfromuavar, font=("Arial",10,"bold"))
combobt4.pack(side=tk.LEFT, padx=5)
#button to clear
btclearoutput = tk.Button(framebt, text= "Clear", font=('Arial',10, "bold"), command=clearoutputheat)
btclearoutput.pack(side=tk.LEFT, padx=5)


#frame 10 button-------------------------------------------------------------
framebt2 = tk.Frame(window)
framebt2.pack(fill=tk.Y, pady=7, padx=100)
#button2 to show instructions
bt2 = tk.Button(framebt2, text= "Instruction", font=('Arial',10, "bold"), command=showinstruction)
bt2.pack(side=tk.LEFT, padx=5)
#button3 to show units
bt3 = tk.Button(framebt2, text= "Show Unit:", font=('Arial',10, "bold"), command=showunit)
bt3.pack(side=tk.LEFT, padx=5)
#str var for combobox below
strvarcbt3=tk.StringVar()
strvarcbt3.set("Select Unit")
#combobox of the unit that had been selected
optionbt3 = ["Mass","Heat","△T", "Heat Capacity","Specific Heat"] 
combobt3 = ttk.Combobox(framebt2,values=optionbt3, width=10,textvariable=strvarcbt3, font=("Arial",10,"bold"))
combobt3.pack(side=tk.LEFT, padx=5)

#frame output heat----------------------------------------------------------
frameoutput2 = tk.Frame(window)
frameoutput2.pack(fill=tk.X, pady=7)
#textoutput tempt
txtoutput2 = tk.StringVar() #biartext "OUTPUT" Bisa berubah
txtoutput2.set(" ")
labeloutputtempt2 = tk.Label(frameoutput2, font=('Helvetica', 12, "bold"), textvariable=txtoutput2)
labeloutputtempt2.pack(side=tk.TOP, padx=10)

#RUNPROGRAMM
window.mainloop()