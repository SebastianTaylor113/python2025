"""
Python for a Year
Sebastian Taylor
2.TemperatureConverter.py
"""

import os

def ClearScreen():
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')

def TempConv(temp, forc):
    if forc == "1":
        temperature=((temp-32) * 0.55555555555)
        print(str(temp) + " Farenheit is " + str(temperature) + " in Celsius!")
        input("Press Enter to Continue")
    elif forc == "2":
        temperature=((temp * 1.8) + 32)
        print(str(temp) + " Celsius is " + str(temperature) + " in Farenheit!")
        input("Press Enter to Continue")
    elif forc == "3":
        return False
    else:
        print('error invalid range')

while True:
    forc=input(
    """
    Farenheit or Celsius?
        1.Farenheit
        2.Celsius
        3.Exit

    Input: """)
    if forc == "3":
        temp=int(0)
    else:
        temp=int(input("Input Temperature: "))
    ClearScreen()
    result = TempConv(temp, forc)
    ClearScreen()
    if result == False:
        break