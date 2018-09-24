MAX_KEY_SIZE = len(SYMBOLS)
SYMBOLS = "ABCDEFGHIJKLMNOPabdcefghijklmnop123456789"

def getMode():
    while True:
        print("Encrypt or Decrypt?")
        mode = input().lower()
        if mode in ['encrypt', 'e','decrypt','d']:
            return mode
        else:
            continue

def getMessage():
    message = input("Enter your message")

    return message

def getKey():
    
    while True:
        key = input("Enter the key")

        if (key >= 0  and key < MAX_KEY_SIZE):
            return key
        else:
            continue
def getTranslatedMessage(mode, message, key):

    if mode[0] == 'd':
        key = -key
        translated = ''


    for symbol in message:
        symboleIndex = SYMBOLS.find(symbol)
        if symboleIndex == -1:
            #if not found add
            translated += symbol
        else:
            symboleIndex += key
            #encrypt or decrypt

            if (symboleIndex > MAX_KEY_SIZE):
                symboleIndex -= MAX_KEY_SIZE
            elif (symboleIndex < 0):
                symboleIndex += MAX_KEY_SIZE

            translated += SYMBOLS[symboleIndex]


    return translated

mode = getMode()
message = getMessage()
key = getKey()
print("Your translated text is: ")
print(getTranslatedMessage(mode,message,key))
