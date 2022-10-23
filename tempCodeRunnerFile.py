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
                print(pDash)                
                C_Dash = encrypt(pDash, key)
                
                # print(C, C_Dash)
                
                # Now we will compare C_Dash to C, we count how many bits are different.
                for j in range(len(C)):
                    if C[j] != C_Dash[j]:
                        diffBits += 1
                print("Plaintext : ", plaintext, " | ","Changed plaintext : ", pDash)
                print("Cipher text", C, " | ", "New cipher text: ", C_Dash)
                print("Total bits changed", diffBits)
                print("Total avalanche: ", (diffBits / 5120) * 100, "%")
                # if diffBits == 20:
                #     exit()
    # print(diffBits)           
avalanche() 