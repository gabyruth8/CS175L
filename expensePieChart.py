#GabriellaVelasquez
#CS175L
#expensePieChart


import matplotlib.pyplot

def main():
    try:
        expenses_file = open('expenses.txt', 'r')
        return expenses_file
    except IOError:
        print('File not found - exiting')
        raise SystemExit

def pie_chart():
    expenses_file = main()
    labels = []
    values = []

    for row in expenses_file:
        row = row.rsrtip('\n')
        label, value = row.split('\t')
        try:
            value = int(values)
            label.append(labels)
            value.append(values)
        except ValueError:
            print('Error')
    plt.pie(values, labels = labels)
    plt.title('Expense Pie Chart')
    plt.show()

if __name__ == '__main__':
    main()
    
