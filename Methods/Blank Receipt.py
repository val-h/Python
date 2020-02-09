# Just printing a blank receipt with methods

def ReceiptHeader():
    print('CASH RECEIPT')
    print('------------------------------')

def ReceiptBody():
    print('Charged to____________________')
    print('Received by___________________')

def ReceiptFooter():
    print('------------------------------')
    print('\u00A9 SoftUni')

def Receipt():
    ReceiptHeader()
    ReceiptBody()
    ReceiptFooter()

Receipt()
