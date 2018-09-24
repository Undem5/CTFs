key = "!\"#$%&'-./0.123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


def decrypt(message):


    result = ''

    for n in range(1,len(key)+1):

        for l in message:
            try:
                i = (key.index(l) + n) % len(key)
                result += key[i]

            except ValueError:
                result += l

        print '|' + result + '|\n'
        message = ''

print("Enter your message:")
message = raw_input()
decrypt(message)
        
