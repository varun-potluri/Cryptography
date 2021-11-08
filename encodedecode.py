import math

def modulo_calc(x,y):
    m = x%y
    return(m)
def naive_rep(message):
    numbers = []
    for letter in message:
        number = ord(letter) - 97
        number_str = str(number)
        zero_filled_number = number_str.zfill(2)
        numbers.append(zero_filled_number)

    return numbers


def encoder(txt,blocksize):
    
    if len(txt)%blocksize != 0:
        while len(txt)%blocksize != 0:
            txt += 'x'
    
    plaintext = naive_rep(txt)
    temp  = 0
    i=0
    j=0
    while j != len(plaintext):
        block = plaintext[j:j+blocksize]
        k = 0
        compression = 0
        block = block[::-1]
        while k < len(block):
            temp = int(block[k])
            print(temp, k)
            compression = compression +  (temp * pow(26,k)) 
            k += 1  
        print(compression)
        print(str(block) + "   " +str(compression))
        j += blocksize

    return(compression)

def decoder(message):
    l = 26
    reverse = ''
    while message > 0:
        code = modulo_calc(message, l)
        reverse.append(code)

        message = message - code
        message /= l
    print(reverse)

print(encoder("njit",4))