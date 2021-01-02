#TODO: DRY up the code
#TODO: Do time and space complexity analysis and fix issues
def addBigNumbers(a, b):
    longerNumber, shorterNumber = "0", "0"
    if len(a)> len(b):
        longerNumber = a
        shorterNumber = b
    else: 
        longerNumber = b
        shorterNumber = a
    shorterNumberLength = len(shorterNumber)
    total = ""
    carry = 0
    for i in range (1, shorterNumberLength+1):
        currentColumnSum = int(shorterNumber [-1*i]) + int(longerNumber[-1*i]) + carry
        carry = 0
        if currentColumnSum > 9:
            carry = currentColumnSum // 10
            total = str(currentColumnSum % 10) + total
        else:
            total = str(currentColumnSum) + total
    if carry != 0:
        ctr = 1
        while True:
            if shorterNumberLength + ctr <= len(longerNumber): 
                currentColumnSum = carry + int(longerNumber[-1*shorterNumberLength-ctr])
                carry = 0
                if currentColumnSum > 9:
                    carry = currentColumnSum // 10
                    total = str( currentColumnSum%10) + total
                else:
                    total = str(currentColumnSum) + total
                ctr+=1
                
            else:
                total = str(carry) + total
                carry = 0
            if carry == 0:
                    break
    if len(total) < len(longerNumber):
        total = longerNumber[0: len(longerNumber)- len(total)]+ total
    return total        
addBigNumbers ("999992399999992323999", "999993723187861023129")         
        
        