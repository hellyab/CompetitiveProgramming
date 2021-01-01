import functools
from addBigNumbers import addBigNumbers
def multiplyBigNumbers(a,b):
    longerNumber, shorterNumber = "0", "0"
    if len(a) > len(b):
        longerNumber = a
        shorterNumber = b
    else: 
        longerNumber = b
        shorterNumber = a
    shorterNumberLength = len(shorterNumber)
    longerNumberLength = len(longerNumber)
    productRows = []
    carry = 0
    for i in range(shorterNumberLength):
        print(shorterNumberLength)
        currentNumber = int(shorterNumber[-1 * shorterNumberLength]) 
        currentProductRow = "0" * i
        for j in range (longerNumberLength):
            product = (currentNumber * int(longerNumber[-1 * longerNumberLength])) + carry
            carry = 0
            if product > 9:
                carry = product // 10
                currentProductRow = str(product % 10) + currentProductRow
            else:
                currentProductRow = str(product) + currentProductRow
        if carry > 0:
            currentProductRow = str(carry) + currentProductRow
            carry = 0
        productRows.append(currentProductRow)
    return functools.reduce(addBigNumbers,productRows)
    
multiplyBigNumbers("999999999", "99999999999")
        
  