#GabriellaVelasquez
#CS175L
#AvergaeFromInput

def read_numbers():
    try:
        numbers_file = open('numbers.txt', 'r')
        return numbers_file
    except IOError:
        print("SystemExit: File not found: numbers.txt - exiting")
        raise SystemExit

def get_numbers():
    numbers_file = read_numbers()
    total = 0
    count = 0
    numbers = []

    for line in numbers_file:
        try:
            amount = float(line.strip())
            numbers.append(amount)
            count += 1
            total += amount
            print(f'I read in {count} number(s) Current number is: {amount:.2f} Total is: {total:.2f}.')
        except ValueError:
            print("Bad data:", line.strip(), "skipping")

    numbers_file.close()
    return numbers

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    numbers = get_numbers()
    average = calculate_average(numbers)
    print(f'Average: {average:.1f}')

if __name__ == '__main__':
    main()
