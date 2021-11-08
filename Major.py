import math
import random

print("Choices:\n 1 - GCD\n 2 - Modulo Calculator\n 3 - Inverse Calculator\n 4 - Square & Multiply Calculator\n 5 - Generator\n 6 - Diffie-Hellman \n 7 - Encode \n 8 - Decoder")
c = input("Please enter your choice:\n")
 
c = int(c)
 
if c == 1:
    print('1. GCD')
elif c == 2:
    print('2. Modulo Calculator')
elif c == 3:
    print('3. Inverse Calculator')
elif c == 4:
    print('4. Square & Multiply')
elif c == 5:
    print('5. Generator')
elif c == 6:
    print('6. Diffie-Hellman')
elif c == 7:
    print('7. Encoder')
elif c == 8:
    print('8. Encoder')
else:
    print('wrong choice')

#----------------------------GCD Calculaotr--------------------------------
def gcd_calc(x,y):
    c = math.gcd(x, y)
    return(c)

#----------------------------Modulo Calculator--------------------------------
def modulo_calc(x,y):
    m = x%y
    return(m)

#----------------------------Check Prime--------------------------------
def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number%2 == 0:
        return False
    for i in range(3,int(math.sqrt(number))):
        if number%i == 0:
            return False
    return True

#----------------------------Check Fermat--------------------------------
def isFermat(u,p):
    if isPrime(p):
        if(u%p != 0):
            return True
    else:
        return False

#----------------------------Function to Display Inverse--------------------------------
def display_inverse(remainders, quotients, inverses):
    for i in range(0,len(remainders)):
        print("     " + str(i) + "    ")

    print("\n")
    print("\n")

    for i in range(0,len(remainders)):
        print("     " + str(remainders[i]) + "    ")

    print("\n")
    print("\n")

    for i in range(0,len(remainders)):
        if i == 0:
            print("     " + "Quotient" + "    ")
            continue
        if i == len(remainders) - 1:
            print("     " + "**" + "    ")
            continue
        print("     " + str(quotients[i]) + "    ")

    print("\n")
    print("\n")

    for i in range(0,len(inverses)-1):
        print("     " + str(inverses[i]) + "    ")

#----------------------------Inverse Mod Function--------------------------------
def inversemod(a,p):
    gcd = gcd_calc(a,p)
    if gcd != 1:
        print("Inverse does not exist, please choose different values!")
        return 0
    remainders = []
    quotients = []
    inverses = []

    remainders.insert(0,p)
    remainders.insert(1,a)
    quotients.insert(0,0)

    i = 2
    while True:
        print("P = "+ str(p) + "a = " + str(a))
        print("Remainders = "+str(remainders))
        print("Quotients = "+str(quotients))

        remainder = p%a
        quotient  = p/a
        quotient = int(quotient)

        remainders.insert(i, remainder)
        quotients.insert(i-1, quotient)

        if remainder == 1 or remainder == 0:
            break

        p = a
        a = remainders[i]
        i = i + 1
    
    inverses.insert(0, 0)
    inverses.insert(1, 1)

    j = len(quotients)

    while j > 1:
        x = (quotients[j-1] * inverses[len(inverses) - 1]) + inverses[len(inverses) - 2]
        inverses.append(x)
        j = j-1
    display_inverse(remainders,quotients,inverses)
    if len(remainders) % 2 == 0:
        return inverses[(len(inverses)-1)]
    else:
        return remainders[0] - inverses[(len(inverses)-1)]

#----------------------------Square & Multiply--------------------------------
def square_multiply(u, m ,p):
    if isFermat(u,p):
        m = modulo_calc(m,p-1)
        print("Using Fermat Theorem, m was reduced to" + str(m) + "." + "As," + str(u) + "^" + str(p-1)+" = 1 mod " + str(p) + ".\n")

        counter = 0
        b = 1
        A = 1
        multiply = ""
        print("   m:=(m-b)/2  " + "    b:=m mod 2  " + "  u:=u^2 mod p   " +  "   Squaring  " +  " A:=Au mod p " + "Comments")
        
        while(True):
            b = modulo_calc(m, 2)

            if b == 1:
                multiply = "Multiply"
            else:
                multiply = "Skip"        
        
            print("     " + str(m) + "       " + str(b) + "       " + str(u) + "       " + str(counter) + "       " + str(A) + "       "+ multiply)

            if b == 1:
                A = modulo_calc(A*u,p)
            
            m = (m-b)/2

            if m > 0:
                u = modulo_calc(u*u,p)
            else:
                return A
            counter = counter + 1

#----------------------------Generator--------------------------------
def LCMofArray(a):
    temp = []
    lcm = a[0]
    temp.append(lcm)
    for i in range(1, len(a)):
        value = a[i] // math.gcd(lcm, a[i])
        lcm = lcm * a[i] // math.gcd(lcm, a[i])
        if value not in temp and value != 1:
            temp.append(value)
    return temp

def generator(P):
    p_minus_1 = P - 1
    val = []
    for i in range(2, p_minus_1):
        if p_minus_1 % i == 0:
            val.append(i)
    if val:
        final_values = LCMofArray(val)
    else:
        final_values = [p_minus_1]
    print(f'{final_values} are prime factors of {p_minus_1}')

    for i in range(2, P):
        temp = []
        for val in final_values:
            final_value = int(pow(i, int(p_minus_1/val), P))
            temp.append(final_value)
        if 1 not in temp:
            print(f'{i} is a generator')
            break

#----------------------------Naive Representation of MSG--------------------------------
import math
def naive_rep(message):
    numbers = []
    for letter in message:
        number = ord(letter) - 97
        number_str = str(number)
        zero_filled_number = number_str.zfill(2)
        numbers.append(zero_filled_number)

    return numbers

#----------------------------Encoder for Compression--------------------------------
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

#----------------------------Decoder for Compression--------------------------------
def decoder(message):
    l = 26
    reverse = []
    while message > 0:
        code = modulo_calc(message, l)
        reverse.append(code)

        message = message - code
        message /= l
    reverse.reverse()    
    return reverse

#----------------------------Diffie-Hellman--------------------------------
def diffie(sharedPrime,sharedBase):
    
    aliceSecret =  random.randint(1,sharedPrime-1)   # a
    bobSecret =  random.randint(1,sharedPrime-1)      # b
    
    # Begin
    print( "Publicly Shared Variables:")
    print( "    Publicly Shared Prime: " , sharedPrime )
    print( "    Publicly Shared Base:  " , sharedBase )
    
    # Alice Sends Bob A = g^a mod p
    A = (sharedBase**aliceSecret) % sharedPrime
    print( "\n  Alice Sends Over Public Chanel: " , A )
    
    # Bob Sends Alice B = g^b mod p
    B = (sharedBase ** bobSecret) % sharedPrime
    print("\n  Bob Sends Over Public Chanel: ", B )
    print( "\n------------\n" )
    print( "Privately Calculated Shared Secret:" )
    # Alice Computes Shared Secret: s = B^a mod p
    aliceSharedSecret = (B ** aliceSecret) % sharedPrime
    print( "    Alice Shared Secret: ", aliceSharedSecret )
    
    # Bob Computes Shared Secret: s = A^b mod p
    bobSharedSecret = (A**bobSecret) % sharedPrime
    print( "    Bob Shared Secret: ", bobSharedSecret )




if c == 1:
    a = int(input("Enter value of 'a': "))
    b = int(input("Enter value of 'b': "))
    print(gcd_calc(a,b))

if c == 2:
   a = int(input("Enter the value of 'a': "))
   p = int(input("Enter the value of 'p': "))
   print(modulo_calc(a,p))

if c == 3:
    a = int(input("Enter the value of a: "))
    p = int(input("Enter the value of P: "))
    print(inversemod(a,p))

if c == 4:
    u = int(input("Enter the value of 'u': "))
    m = int(input("Enter the value of 'm': "))
    p = int(input("Enter the value of 'p': "))
    print(square_multiply(u,m,p))

if c == 5:
    p  = int(input("Enter the value of 'p': "))
    generator(p)

if c == 6:
    p = int(input("Enter the value of 'p': "))
    g = int(input("Enter the value of 'g':"))
    diffie(p,g)

if c == 7:
    t = input("Enter the text to Encode: ")
    b = int(input("Enter block Size: "))
    print(encoder(t,b))

if c == 8:
    t = int(input("Enter the text to Decode: "))
    print(decoder(t))