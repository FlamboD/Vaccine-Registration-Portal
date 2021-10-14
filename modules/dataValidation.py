def validateChecksum(id_number):
    sum =0
    miniSum=0
    current_digit=0
    checksum= None
    if ((id_number.isdigit()) & (len(id_number)==13)):
        for i in range(0,12):
            current_digit = int(id_number[i])
            if not(i%2==0):
                product = current_digit*2
                if product>9:
                    miniSum = int(str(product)[0])+ int(str(product)[1]) 
                    sum +=miniSum
                else:
                    sum +=product
            else:
                sum += current_digit
    checksum = 10-(sum%10)
    
    if checksum>9:
        checksum = 0
    if checksum==int(id_number[12]):
        return True
    else:
        return False
def allData(id_number,confID,dob,name,surname,gender):
    valid_ID = validateChecksum(id_number)
    
        


