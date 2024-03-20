#GabriellaVelasquez
#CS175L
#AvergaeFromInput

def main():
    numbers_file = open('numbers.txt', 'r')

    total = 0
    count = 0
    
    for line in numbers_file:
        amount = float(line)
        count += 1
        total += amount
        print(f'I read in {count} number(s) Current number is: {amount:.2f} Total is: {total:.2f}.')

    average = total / count
    print(f'Average: {average:.1f}')
      
if __name__ == '__main__':
    main()                
            
