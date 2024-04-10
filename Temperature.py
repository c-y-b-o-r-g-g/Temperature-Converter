def isfloat(x):
    try:
        float_n = float(x)
    except ValueError:
        return False
    else:
        return True

print("\n\n***Welcome to The Temperatrue Conversion Program***")
print("You will be prompted to Choose your input unit, then enter the temperature value")
print("After that you will have the entered temperature Converted to All units")
input("Press Enter to continue...")

choice_flag = False
while choice_flag == False:
        choice = (input("Choose Your Input Temperature:\n1.Celsius\n2.Fahrenheit\n3.Kelvin\n>:"))
        if choice.isdigit():
            choice = int(choice)
            if not 1<=choice<=3:
                print("Enter a valid Choice")
            else:
                choice_flag = True
                break
            


temp_flag = False
while temp_flag==False:
    temp = input("Enter the Temperature Value:\n>:")
    if temp.isdigit():
        temp = int(temp)
        temp_flag = True
    elif isfloat(temp):
        temp = float(temp)
        temp_flag = True
    else:
        print("Enter a Valid Temperature")


def celsius_calcs(celsius):
    fahrenheit = (celsius * (9/5)+32)
    kelvin = celsius + 273.15
    return (f"{fahrenheit:.2f} Fahrenheit\n{kelvin:.2f} Kelvin")
    
def fahrenheit_calcs(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    kelvin  = (fahrenheit - 32) * (5/9) +273.15
    return (f"{celsius:.2f} Celsius\n{kelvin:.2f} Kelvin")

def kelvin_calcs(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15)*(9/5) + 32
    return (f"{celsius:.2f} Celsius\n{fahrenheit:.2f} Fahrenheit")


choice_name = ''



if(choice ==1 ):
    printable = celsius_calcs(temp)
    choice_name = 'Celsius'
    
elif(choice ==2):
    printable = fahrenheit_calcs(temp)
    choice_name = 'Fahrenheit'
elif(choice ==3):
    printable = kelvin_calcs(temp)
    choice_name = 'kelvin'
    
    

print(f"Your Input temperature was {temp} {choice_name} which is equal to:")
print(printable)