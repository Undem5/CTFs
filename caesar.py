SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

MAX_KEY_SIZE = len(SYMBOLS)
def getMode():
    while True:
        print("Encrypt or Decrypt?")
        mode = raw_input().lower()
        if mode in ['encrypt', 'e','decrypt','d']:
            return mode
        else:
            continue

def getMessage():
    print("Enter your message")
    message = raw_input()

    return message

def getKey():
    
    while True:
        print("Enter the key")
        key = raw_input()
        print type(key)
        val = int(key)
        if (val > 0  and val <= MAX_KEY_SIZE ) :
            return val
        else:
            print("the key must be btw 0 and 52")

def getTranslatedMessage(mode, message, key):

    translated = ''
    if mode[0] == 'd':
        key = -key


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
