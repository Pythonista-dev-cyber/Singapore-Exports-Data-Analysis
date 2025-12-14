import csv
import numpy
import matplotlib.pyplot as plt

#Sub_Function
def Display_Menu():
    print("Menu")
    print("1.the exports to Asia for the period from 1998 to 2009.")
    print("2.Average and Highest value of selected area.")
    print("3.Show the list which increase or decrease at least 15%")
    print("4.Drawing plot.")
    print("Exit")



def Option1():
    Data = Read_Csv_File("sgexports_dataset 2.csv")
    Year = Data[0][1:] #1998,1999,......2009
    Export_Value = Data[2][1:]  # 50197.3,56987.4,73466.9
    print("Export value for Asia from 1998 to 2009 is:")
    for i in range(len(Year)):
        print(f"{Year[i]} export value is {Export_Value[i]}")
        


def Option2():
    UserChoice = 0 
    Data  = Read_Csv_File("sgexports_dataset 2.csv")
    Year = Data[0]
    Export_Value = Data[1:]
    Set_Line()
    while UserChoice <=0 or UserChoice >len(Export_Value):
        UserChoice = Show_Region()
    Set_Line()

    Average_Export = 0
    Total_Export  = 0 
    Maximum_Export = 0 
    Maximum_Year   = ""

    #Search the average value of selected region
    for i in Export_Value[UserChoice-1][5:]:
        Total_Export += float(i)
    Average_Export = Total_Export / 8

    for i in range(len(Export_Value[UserChoice-1][5:])):
        if float(Export_Value[UserChoice-1][i+5]) > Maximum_Export:
            Maximum_Export = float(Export_Value[UserChoice-1][i+5])
            Maximum_Year = Year[i+5]
    

    print(f"Avearge value of {Export_Value[UserChoice-1][0]} for the period 2002 to 2009 is {round(Average_Export,3)}")
    print(f"Maximum expoort value is {Maximum_Export} at {Maximum_Year}")


        

    

    


def Option3():
    UserChoice = 0 
    Data  = Read_Csv_File("sgexports_dataset 2.csv")
    Year = Data[0]
    All_Export_Value = Data[1:]
    Set_Line()
    while UserChoice <=0 or UserChoice >len(All_Export_Value):
        UserChoice = Show_Region()
    Set_Line()

    Export_Value=[]
    for i in All_Export_Value[UserChoice-1][1:]:
        Export_Value.append(float(i))
    
    prev=0
    for i in range(len(Export_Value)):
        if Export_Value[i]>(1.15*prev) or Export_Value[i]<(0.85*prev):
            print(f'{Year[i+1]} : export value is {Export_Value[i]}')
        prev=Export_Value[i]



def Option4():
    Data = Read_Csv_File("sgexports_dataset 2.csv")
    Year = Data[0]
    Export_Value = Data[1:]


    #Draw the line plot for America and Europe
    America_Export= []
    Europe_Export = []

    for i in range(1,len(Year)):
        America_Export.append(float(Export_Value[0][i]))
        Europe_Export.append(float(Export_Value[2][i]))


    PointX = range(len(America_Export))
    plt.figure(figsize=(15,10))
    plt.subplot(2,1,1)
    plt.plot(PointX,America_Export,c='r',label="America")
    plt.plot(PointX,Europe_Export,c='b',label="Europe")
    plt.xticks(PointX,Year[1:])
    plt.xlabel("Year")
    plt.ylabel("Export value")
    plt.legend()


    TotalArray = []
    for i in range(1,len(Year)):
        TempTotal = 0 
        for y in range(len(Export_Value)):
            TempTotal += float(Export_Value[y][i])
        TotalArray.append(TempTotal)

    #Draw bar chart 
    plt.subplot(2,1,2)
    plt.xlabel("Year")
    plt.ylabel("Total export value")
    plt.xticks(PointX,Year[1:])
    plt.bar(PointX,TotalArray,color='r',label="Total value",width=0.5)
    


    plt.show()

def Exit():
    print("Calling Exit!")


def Set_Line():
    print("*"*40)
    print("*"*40)


def Read_Csv_File(FileName):
    Data = []
    File = open(FileName,"r")
    Read_Csv = csv.reader(File)
    for i in Read_Csv:
        Data.append(i)
    return Data


def Show_Region():
    print("Region name:")
    Data = Read_Csv_File("sgexports_dataset 2.csv")
    for i in range(len(Data[1:])):
        print(f"{i+1}.{Data[i+1][0]}")

    try:
        UserChoice = int(input("Selct the area(1 to 6):"))
    except TypeError:
        UserChoice = 0

    return UserChoice






    



#Identify Array
Year = []  #Single array to store the value of Year
Export_Value = [] #Double array to store the value of export depend on location


#Main program
while True:
    Read_Csv_File("sgexports_dataset 2.csv")
    Display_Menu() #Show menu
    Set_Line()
    UserChoice = input("Enter choice between 1 and 5:")
    if UserChoice == "1":
        Option1()
    elif UserChoice =="2":
        Option2()
    elif UserChoice =="3":
        Option3()
    elif UserChoice =="4":
        Option4()
    elif UserChoice =="5":
        Exit()
        break
    else:
        print("Invaild input!Please try again.")

    Set_Line()

print("End program")