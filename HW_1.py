plainT = [
        "1111 0100 0110 0110", 
        "0010 1001 1100 0010", 
        "0101 1100 1110 0010", 
        "1001 1100 0010 0111", 
        "1011 1101 1101 1111", 
        "0001 1101 0001 0011", 
        "1110 0001 1100 0011", 
        "0011 1110 0000 0010", 
        "0101 0011 1101 1011", 
        "1100 0010 0111 0100"] 

keys = [
    "1010 0010 1111 1010", 
    "1110 0000 0001 1000" 
]

def encrypt(plainText, initK):
    s1 = [[15, 10, 2, 5], [8, 4, 11, 6], [1, 0, 14, 7], [9, 3, 12, 13]]

    s2 = [[4, 0, 15, 10], [8, 9, 7, 13], [5, 1, 6, 11], [2, 3, 14, 12]]

    ctr = 0
    cipher = []
    p = plainText.split(" ")
    
    k = initK.split(" ")

    a = []
    a.append(int(p[0]))
    a.append(int(p[1]))
    a.append(int(p[2]))
    a.append(int(p[3]))

    kList = []
    kList.append(int(k[0]))
    kList.append(int(k[1]))
    kList.append(int(k[2]))
    kList.append(int(k[3]))

    mapping = [[1, 0], [3, 2], [0, 1], [2, 3]]

    for item in mapping:
        # firstMap and secondMap contains single number to be mapped
        firstMap = item[0]
        secondMap = item[1]
        
        decimalA = int(str(a[firstMap]), 2)
        decimalB = int(str(kList[secondMap]), 2)
        
        # Performing the XOR operation
        xored = decimalA^decimalB
        xoredBin = '{0:b}'.format(xored)

        # Padding the number with 0's.
        padXoredBin = xoredBin.rjust(4, '0')

        # Now we have to split the xored output

        firstHalfXored = padXoredBin[:2]
        secondHalfXored = padXoredBin[2:]


        firstRowNum = int(firstHalfXored, 2)
        secondRowNum = int(secondHalfXored, 2)

        # Taking number from S-boxes based on row and column value.
        if ctr % 2 == 0:
            matrixNum = s1[secondRowNum][firstRowNum]
        else:
            matrixNum = s2[secondRowNum][firstRowNum]
        ctr+=1
        # print(matrixNum)

        cipher.append("{0:b}".format(matrixNum).rjust(4, '0'))
    
    cipher = ' '.join(cipher)
    return cipher

for key in keys:
    for plaintext in plainT:
        print("Plaintext: ", plaintext, "Key: ", key)
        cipher = encrypt(plaintext, key)
        print("Resulting Cipher: ", cipher)
        print("------------------------------------------------------")

# Avalanche ------------------------------

def avalanche():
    diffBits = 0

    ctr = 0
    # For every 16 bit plaintext
    for plaintext in plainT:
        # For every key from above key
        for key in keys:
            # We are going to encrypt that one plaintext with that one key
            C = encrypt(plaintext , key)
           
            # C = "0111 0100 0110 0111"
            for i in range(len(plaintext)):
                    # We change 1 bit in plaintext and see how many bits are different in C and C_Dash.
                # Here we will change 1 bit each from plaintext 16 times
                
                plainTextList = list(plaintext)
                if(plaintext[i] == '0'):
                    plainTextList[i] = '1'
                elif(plaintext[i] == '1'):
                    plainTextList[i] = '0'
                else:
                    continue
                
                # Changing 1 bit in p
                pDash = ''.join(plainTextList)
               
                # Now we will calculate the new CipherText
                C_Dash = encrypt(pDash, key)
                
                # print(C, C_Dash)
                
                # Now we will compare C_Dash to C, we count how many bits are different.
                for j in range(len(C)):
                    if C[j] != C_Dash[j]:
                        diffBits += 1
                print("Plaintext : ", plaintext, " | ","Changed plaintext : ", pDash)
                print("Cipher text", C, " | ", "New cipher text: ", C_Dash)
                print("Total bits changed", diffBits)
                print("Avalanche: ", (diffBits / 5120) * 100, "%")
                print("-----------------------------------------------------------------")
                # if(diffBits == 9):
                #     exit()
    # print(diffBits)           
# avalanche() 

# Modification for improving avalance-----------------------------------------------------------------------------------------------------------



