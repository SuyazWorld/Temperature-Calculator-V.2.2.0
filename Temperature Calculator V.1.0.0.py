#TEMPREATURE CHANGER
class Tempt:
    def __init__(self, degree):
        self.degree = degree
class Celcius(Tempt):
    def __init__(self, degree):
        super().__init__(degree)
    def celtofah(self):
        return (9/5) * self.degree + 32
    def celtorea(self):
        return (4/5) * self.degree
    def celtokel(self):
        return 273 + self.degree
class Fahrenheit(Tempt):
    def __init__(self, degree):
        super().__init__(degree)
    def fahtocel(self):
        return (5/9) * (self.degree - 32)
    def fahtorea(self):
        return (4/9) * (self.degree - 32)
    def fahtokel(self):
        return (4/9) * (self.degree - 32) + 273
class Reamur(Tempt):
    def __init__(self, degree):
        super().__init__(degree)
    def reatocel(self):
        return (5/4) * self.degree
    def reatofah(self):
        return (9/4) * self.degree + 32
    def reatokel(self):
        return (5/4) * self.degree + 273
class Kelvin(Tempt):
    def __init__(self, degree):
        super().__init__(degree)
    def keltocel(self):
        return self.degree - 273
    def keltofah(self):
        return (9/5) * (self.degree - 273) + 32
    def keltorea(self):
        return (4/5) * (self.degree - 273)

#HEAT Calculator
class Calor:
    def __init__(self, mass, capacity, kalor, kalorjenis, initial, after):
        self.m1 = mass
        self.C1 = capacity
        self.Q = kalor
        self.C2 = kalorjenis
        self.T1 = initial
        self.T2 = after
    
    def cal_kalor(self):
        return self.m1 * self.C2 *(self.T2 - self.T1)
    def capacity1_calor(self):
        return self.m1*self.C2
    def capacity2_calor(self):
        return self.Q/(self.T2 - self.T1)
    def kalorjenis1(self):
        return self.Q / (self.m1 *(self.T2 - self.T1))
    def kalorjenis2(self):
        return self.C1 / self.m1
    def temperature_change(self):
        return self.T2 - self.T1
    def temperature_change2(self):
        return self.Q / (self.m1*self.C2)
    def temperature_change3(self):
        return self.Q/self.C1

class Runprogram:
    def runningprogram():
        #PROGRAM RUNNING
        selectproject = input("what calculator you want to use? (heat/tempt): ")
        #PROGRAM FOR HEAT CALCULATOR
        if selectproject == "heat":
            selectheat = input("choose (Q/c/C/m/Temperature Change(temptchange)):")
            if selectheat == "Q": #nyari kalor biasa Q
                #rumus kalor biasa mc△T
                selectQ = input("For the temperature you have to use celcius, do you already have celcius degree? (yes/no)")
                if selectQ == "yes":
                    kalorc = Calor(float(input("input mass (kg):")), 1, 1, float(input("input Specific Heat (J/kg°C):")), float(input("input initial temperature (°C):")), float(input("input after temperature (°C):")))
                    print("The Heat is ",kalorc.cal_kalor(), "Joule")
                #bisa buat rubah delta T / rumus kalor mcat tapi temperaturnya bisa dipilih untuk diubah
                elif selectQ == "no":
                    selectinputtemp = input("Do you want to change it from (r/f/k) to Celcius?")
                    if selectinputtemp == "r":
                        reamur = Reamur(float(input("input initial degree (Reamur to Celcius): ")))
                        reamur2 = Reamur(float(input("input after degree (Reamur to Celcius): ")))
                        kalor1 = Calor(float(input("input mass (kg):")), 1, 1, float(input("input Specific Heat (J/kg°C):")), reamur.reatocel(), reamur2.reatocel())
                        print("The Heat is ",kalor1.cal_kalor(), "Joule")
                    elif selectinputtemp == "f":
                        fahren1 = Fahrenheit(float(input("input initial degree (Fahrenheit to Celcius): ")))
                        fahren2 = Fahrenheit(float(input("input after degree (Fahrenheit to Celcius): ")))
                        kalor1 = Calor(float(input("input mass (kg):")), 1, 1, float(input("input Specific Heat (J/kg°C):")), fahren1.fahtocel(), fahren2.fahtocel())
                        print("The Heat is ",kalor1.cal_kalor(), "Joule")
                    elif selectinputtemp == "k":
                        kelvin1 = Kelvin(float(input("input initial degree (kelvin to Celcius): ")))
                        kelvin2 = Kelvin(float(input("input after degree (kelvin to Celcius): ")))
                        kalor3 = Calor(float(input("input mass (kg):")), 1, 1, float(input("input Specific Heat (J/kg°C):")), kelvin1.keltocel(), kelvin2.keltocel())
                        print("The Heat is ",kalor3.cal_kalor(), "Joule")
                    else:
                        print("please choose between (r/f/k)!")
                else:
                    print("please input between (yes/no)!")
            elif selectheat == "C":
                    rumus = input("pilih rumus 1/2 :")
                    if rumus == "1":
                        tanya1 = input("For the temperature you have to use celcius, do you already have celcius degree? (yes/no)")
                        if tanya1 == "yes":
                            kapacity1 = Calor(1, 1, float(input("input Heat (Joule):")), 1, float(input("input initial temperature (°C):")), float(input("input after temperature (°C):")))
                            print("The Heat Capacity is ", kapacity1.capacity2_calor(), "J/°C")
                        elif tanya1 == "no":
                            CCtempt = input("Do you want to change it from (r/f/k) to Celcius?")
                            if CCtempt == "r":
                                CCrea1 = Reamur(float(input("input initial degree (Reamur to Celcius): ")))
                                CCrea2 = Reamur(float(input("input after degree (Reamur to Celcius): ")))
                                kapacity2 = Calor(1, 1, float(input("input Heat (Joule):")), 1, CCrea1.reatocel(), CCrea2.reatocel())
                                print("The Heat Capacity is ", kapacity2.capacity2_calor(), "J/°C")
                            elif CCtempt == "f":
                                CCfah1 = Fahrenheit(float(input("input initial degree (Fahenheit to Celcius): ")))
                                CCfah2 = Fahrenheit(float(input("input after degree (Fahrenheit to Celcius): ")))
                                kapacity3 = Calor(1, 1, float(input("input Heat (Joule):")), 1, CCfah1.fahtocel(), CCfah2.fahtocel())
                                print("The Heat Capacity is ", kapacity3.capacity2_calor(), "J/°C")
                            elif CCtempt == "k":
                                CCkel1 = Kelvin(float(input("input initial degree (Kelvin to Celcius): ")))
                                CCkel2 = Kelvin(float(input("input after degree (Kelvin to Celcius): ")))
                                kapacity4 = Calor(1, 1, float(input("input Heat (Joule):")), 1, CCkel1.keltocel(), CCkel2.keltocel())
                                print("The Heat Capacity is ", kapacity4.capacity2_calor(), "J/°C")
                            else: 
                                print("please choose between (r/f/k)!") 
                        else:
                            print("please input between (yes/no)!")
                    elif rumus == "2":
                        kapacity5 = Calor(float(input("input mass (kg):")), 1, 1, float(input("input Specific Heat (J/kg°C):")), 1, 1)
                        print("The Heat Capacity is ", kapacity5.capacity1_calor(), "J/°C")
                    else:
                        print("please choose the formula that you want!")
            elif selectheat == "c": #nyari specific heat
                    rumus2 = input("pilih rumus 1/2 :")
                    if rumus2 == "1": #rumus 1 c = Q/m△t
                        #brtnaya apa udh celcius blm
                        selectc = input("For the temperature you have to use celcius, do you already have celcius degree? (yes/no)")
                        if selectc == "yes": #kalo udh celcius pake rumus 1 biasa
                            kalorjenis = Calor(float(input("input mass (kg):")), 1, float(input("input Heat (Joule):")), 1, float(input("input initial temperature (°C):")), float(input("input after temperature (°C):")))
                            print("The Specific Heat is ",kalorjenis.kalorjenis1(), "J/kg°C")
                        #rumus 1 dengan delta t tapi delta t bebas mau diubah dari apapun ke celcius
                        elif selectc == "no":
                            cjenis = input("Do you want to change it from (r/f/k) to Celcius?")
                            if cjenis == "r":
                                reac1 = Reamur(float(input("input initial degree (Reamur to Celcius): ")))
                                reac2 = Reamur(float(input("input after degree (Reamur to Celcius): ")))
                                kalorjenis2 = Calor(float(input("input mass (kg):")), 1, float(input("input Heat (Joule):")), 1, reac1.reatocel(), reac2.reatocel())
                                print("The Specific Heat is ",kalorjenis2.kalorjenis1(), "J/kg°C")
                            elif cjenis == "f":
                                fahc1 = Fahrenheit(float(input("input initial degree (Fahrenheit to Celcius): ")))
                                fahc2 = Fahrenheit(float(input("input after degree (Fahrenheit to Celcius): ")))
                                kalorjenis3 = Calor(float(input("input mass (kg):")), 1, float(input("input Heat (Joule):")), 1, fahc1.fahtocel(), fahc2.fahtocel())
                                print("The Specific Heat is ",kalorjenis3.kalorjenis1(), "J/kg°C")
                            elif cjenis == "k":
                                kelvinc1 = Kelvin(float(input("input initial degree (Kelvin to Celcius): ")))
                                kelvinc2 = Kelvin(float(input("input after degree (Kelvin to Celcius): ")))
                                kalorjenis4 = Calor(float(input("input mass (kg):")), 1, float(input("input Heat (Joule):")), 1, kelvinc1.keltocel(), kelvinc2.keltocel())
                                print("The Specific Heat is ",kalorjenis4.kalorjenis1(), "J/kg°C")
                            else:
                                print("please choose between (r/f/k)!")
                        else:
                            print("please input between (yes/no)!")
                    elif rumus2 == "2": #rumus2 c = C/m
                        kalorjenis2 = Calor(float(input("input mass (kg):")), float(input("input Heat Capacity (J/°C):")), 1, 1, 1, 1)
                        print("The Specific Heat is ",kalorjenis2.kalorjenis2(), "J/kg°C")
                    else:
                        print("please choose the formula that you want!")
            elif selectheat == "temptchange":#mencari delta T
                    temptchangesuper = input("pilih rumus 1/2/3 :")
                    if temptchangesuper == "1": #rumus biasa T2-T1
                        selectT = input("For the temperature you have to use celcius, do you already have celcius degree? (yes/no)")
                        if selectT == "yes": #kalo udah celcius
                            temptchange1 = Calor(1,1,1,1, float(input("input initial temperature (°C):")), float(input("input after temperature (°C):")))
                            print("The Temperature Change is ", temptchange1.temperature_change(), "°C")
                        elif selectT == "no" :#kalo blm celcius
                            tempted1 = input("Do you want to change it from (r/f/k) to Celcius?")
                            if tempted1 == "r":
                                temptedrea1 = Reamur(float(input("input initial degree (Reamur to Celcius): ")))
                                temptedrea2 = Reamur(float(input("input after degree (Reamur to Celcius): ")))
                                temptchange2 = Calor(1,1,1,1, temptedrea1.reatocel(), temptedrea2.reatocel())
                                print("The Temperature Change is ", temptchange2.temperature_change(), "°C")
                            elif tempted1 == "f":
                                temptedfah1= Fahrenheit(float(input("input initial degree (Fahrenheit to Celcius): ")))
                                temptedfah2 = Fahrenheit(float(input("input after degree (Fahrenheit to Celcius): ")))
                                temptchange3 = Calor(1,1,1,1, temptedfah1.fahtocel(), temptedfah2.fahtocel())
                                print("The Temperature Change is ", temptchange3.temperature_change(), "°C")
                            elif tempted1 == "k":
                                temptedkel1= Kelvin(float(input("input initial degree (Kelvin to Celcius): ")))
                                temptedkel2 = Kelvin(float(input("input after degree (Kelvin to Celcius): ")))
                                temptchange3 = Calor(1,1,1,1, temptedkel1.keltocel(), temptedkel2.keltocel())
                                print("The Temperature Change is ", temptchange3.temperature_change(), "°C")
                            else: 
                                print("please choose between (r/f/k)!")  
                        else:
                            print("please input between (yes/no)!") 
                    elif temptchangesuper == "2":
                        temptchange2 = Calor(float(input("input mass (kg):")), 1, float(input("input Heat (Joule):")), float(input("input Specific Heat (J/kg°C):")), 1, 1)
                        print("The Temperature Change is ", temptchange2.temperature_change2(), "°C")
                    elif temptchangesuper == "3":
                        temptchange2 = Calor(1, float(input("input Heat Capacity (J/°C):")), float(input("input Heat (Joule):")), 1, 1, 1)
                        print("The Temperature Change is ", temptchange2.temperature_change2(), "°C")    
                    else:
                        print("please choose the formula that you want!")
            else:
                print("pliss choose between Q/c/C/m/Temperature Change(temptchange))")      
        #PROGRAM FOR TEMPERATURE CALCULATOR
        elif selectproject == "tempt":   
            selecttempterature = input("select temperature (c/f/r/k):")
            if selecttempterature == "c":
                selectcelcius = input("turn in to (f/r/k/all)? :")
                celtempt = Celcius(float(input("input Celcius degree : ")))
                if selectcelcius == "f":
                    print("Change Celcius to Fahrenheit:", celtempt.celtofah(), "°F")
                elif selectcelcius == "r":
                    print("Change Celcius to Reamur:", celtempt.celtorea(), "°R")
                elif selectcelcius == "k":
                    print("Change Celcius to Kelvin:", celtempt.celtokel(), "°K")
                elif selectcelcius == "all":
                    print("change Celcius to:")
                    print("Fahrenheit:", celtempt.celtofah(), "°F")
                    print("Reamur:", celtempt.celtorea(), "°R")
                    print("Kelvin:", celtempt.celtokel(), "°K")
                else:
                    print("please choose between (f/r/k/all)!!!")
            elif selecttempterature == "r":
                selectcreamur = input("turn in to (c/f/k/all)? :")
                reatempt = Reamur(float(input("input Celcius degree : ")))
                if selectcreamur == "c":
                    print("Change Reamur to Celcius:", reatempt.reatocel(), "°C")
                elif selectcreamur == "f":
                    print("Change Reamur to Fahrenheit:", reatempt.reatofah(), "°F")
                elif selectcreamur == "k":
                    print("Change Reamur to Kelvin:", reatempt.reatokel(), "°K")
                elif selectcreamur == "all":
                    print("change Reamur to:")
                    print("Fahrenheit:", reatempt.reatofah(), "°F")
                    print("Celcius:", reatempt.reatocel(), "°C")
                    print("Kelvin:", reatempt.reatokel(), "°K")
                else:
                    print("please choose between (c/f/k/all)!!!")
            elif selecttempterature == "f":
                selectcfahren = input("turn in to (c/r/k/all)? :")
                fahtempt = Fahrenheit(float(input("input Celcius degree : ")))
                if selectcfahren == "c":
                    print("Change Fahrenheit to Celcius:", fahtempt.fahtocel(), "°C")
                elif selectcfahren == "r":
                    print("Change Fahrenheit to Reamur:", fahtempt.fahtorea(), "°R")
                elif selectcfahren == "k":
                    print("Change Fahrenheit to Kelvin:", fahtempt.fahtokel(), "°K")
                elif selectcfahren == "all":
                    print("change Fahrenheit to:")
                    print("Reamur:", fahtempt.fahtorea(), "°R")
                    print("Celcius:", fahtempt.fahtocel(), "°C")
                    print("Kelvin:", fahtempt.fahtokel(), "°K")
                else:
                    print("please choose between (c/r/k/all)!!!")
            elif selecttempterature == "k":
                selectckelvin= input("turn in to (c/r/f/all)? :")
                keltempt = Kelvin(float(input("input Celcius degree : ")))
                if selectckelvin == "c":
                    print("Change Kelvin to Celcius:", keltempt.keltocel(), "°C")
                elif selectckelvin == "r":
                    print("Change Kelvin to Reamur:", keltempt.keltorea(), "°R")
                elif selectckelvin == "f":
                    print("Change Kelvin to Fahrenheit:", keltempt.keltofah(), "°F")
                elif selectckelvin == "all":
                    print("change Kelvin to:")
                    print("Reamur:", keltempt.keltorea(), "°R")
                    print("Celcius:", keltempt.keltocel(), "°C")
                    print("Fahrenheit:", keltempt.keltofah(), "°F")
                else:
                    print("please choose between (c/r/f/all)!!!")
            else:
                print("please choose between (c/f/r/k)!!!")
        else:
            print("please choose between (heat/tempt)!")

runtheprogram = Runprogram.runningprogram()
print(runtheprogram)