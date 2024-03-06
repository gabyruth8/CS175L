#GabriellaVelasquez
#CS175L
#TemperatureConversions

def main():
    controlLoop()

def convertToKelvin(fahrenheit):
    #Take in the fahrenheit temp as an argument
    #Convert Fahrenheit to Kelvin
    #return Kelvin
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin
    

def convertToCentigrade(fahrenheit):
    #Take in the fahrenheit temp as an argument
    #Convert Fahrenheit to Centigrade
    #return Centigrade
    centigrade = (fahrenheit - 32) * 5/9
    return centigrade
    

def doConversion(fahrenheit):
    #getFahrenheit(), get back Fahrenheit
    #convertToKelvin(), send Fahrenheit get back Kelvin
    #ConvertToCentigrade, sends Fahrenheit gets back Centigrade
    #prints for example: 'Fahrenheit: xx Kelvin xx Centigrade: xx'
    kelvin = convertToKelvin(fahrenheit)
    centigrade = convertToCentigrade(fahrenheit)
    print(f'Fahrenheit: {fahrenheit} Kelvin: {kelvin} Centigrade: {centigrade}')
    

def repeat():
    #Inputs How many conversions would you like to do this time?
    #for x in range how many
        #doConversion()
    conversions = int(input('How many conversions would you like to do at this time?: '))
    for _ in range(conversions):
        fahrenheit = getFahrenheit()
        doConversion(fahrenheit)
    

def controlLoop():
    #Inputs 'Do you want to do some conversions(Yes or No)?'
    #if 'yes' repeat()
    while True:
        user_input = input('Do you want to do some conversions(Yes or No)?: ')
        if user_input == 'yes' or 'Yes' :
            repeat()
        elif user_input == 'no' or "No" :
            break
        


def getFahrenheit():
    #Inputs 'Enter Fahrenheit temperature (must be -50 to 130):'
    #(validation loop)'Please re-enter'
    #return Fahrenheit
    fahrenheit = float(input('Enter Fahrenheit temperature (must be -50 to -130): '))
    if -50 <= fahrenheit <= 130:
        return fahrenheit
    else:
        print('Please re-enter')
    

# This code will call the 'main' function if the entire program was run.
if __name__ == '__main__':
    main()
