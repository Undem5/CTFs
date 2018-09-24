import string

def getMessage():
    print("Enter your message")
    message = raw_input()
    return message

def getTranslatedMessage(message):

    translated = ''
    #max key len 52
    for key in range(1,256+1):

        for symbol in string.printable:
            
            symboleIndex = ord(symbol)
            
            if symboleIndex == -1:
                #if not found add
                translated += symbol
            else:
                symboleIndex += key
                #encrypt or decrypt

            if (symboleIndex > 256):
                symboleIndex -= 256
            elif (symboleIndex < 0):
                symboleIndex += 256

            translated += chr(symboleIndex)
            #chr inverse of ord


        print translated
        print "\n"

message = getMessage()
print(getTranslatedMessage(message))
