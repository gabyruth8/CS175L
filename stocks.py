

COMMISSION_RATE_p= float(input('Enter commission rate percentage (ex 0.03) on stock purchase: '))
COMMISSION_RATE_s= float(input('Enter commission rate precentage (ex 0.03) on stock sale: '))
NUM_SHARES_p= int(input('Enter number of shares purchsed: '))
NUM_SHARES_s= int(input('Enter number of shares sold: '))
PURCHASE_PRICE= int(input('Enter purchase price per share: '))
SELLING_PRICE= float(input('Enter sell price per share: '))
    
amountPaidForStock = NUM_SHARES_p * PURCHASE_PRICE

purchaseCommission = COMMISSION_RATE_p * amountPaidForStock

totalPaid = amountPaidForStock + purchaseCommission

stocksSoldFor = NUM_SHARES_s * SELLING_PRICE

sellingCommission= COMMISSION_RATE_s * stocksSoldFor

totalReceived = stocksSoldFor - sellingCommission

profitOrLoss= totalReceived - totalPaid

print('Amount paid for stock: $', (f'{amountPaidForStock:,.2f}'))
print('Commission Paid on the purchase: $', (f'{purchaseCommission:,.2f}'))
print('Amount the stock sold for: $', (f'{stocksSoldFor:,.2f}'))
print('Commssion paid on the sale: $', (f'{sellingCommission:,.2f}'))
print('Profit (or loss if negative): $', (f'{profitOrLoss:,.2f}'))
