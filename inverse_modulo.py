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
    if gcd != 1 or p > a:
        print("Inverse does not exist, please choose different values!")
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