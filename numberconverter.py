print("\t\t\t>>>>>welcome to the converter<<<<<")
print("\t\t\t>>>>>Please select your operation<<<<<")
print("Please select your input base type: ")
print(" 1. Decimal\n 2. Binary\n 3. Ternary\n 4. Quaternary\n 5. Octal\n 6. Duodecimal\n 7. Hexadecimal\n")
a=int(input())
n=[]
b=0
def con(nmb,base):
    while nmb != 0:
        b=nmb%base
        n.append(b)
        #print(b)
        c=nmb//base
        nmb=c
        #print(c)
    #print(n)
    n.reverse()
    for i in n:
        print(i,end="")
    
if a==1:
    print("####################################################################################\n")
    print('''1. Decimal to Binary \t 2. Decimal to Ternary \t 3. Decimal to Quaternary  \t\t\t\n\t 4. Decimal to Octal \t\t5. Decimal to Duodecimal\t\n\t\t\t 6.Decimal to Hexadecimal\n''')
    print("####################################################################################\n")
    print("Please enter your choice: ")
    b=int(input())
    print("Please enter the Decimal number: ")
    nm=int(input())
    c=nm
    if b==1:
        print("Binary form is: ",bin(c))
    elif b==2:
        print("Ternary form is:  "), con(nmb=nm,base=3)
    elif b==3:
        print(" Quaternary form is: "),con(nmb=nm,base=4)
    elif b==4:
        print("Octal form is: ",oct(c))
    elif b==5:
        print("Duodecimalform is : "),con(nmb=nm,base=12)
    elif b==6:
        print("Hexadecimal form is: ",hex(c))
    else:
        print("error")
        
elif a==2:
    print("####################################################################################\n")
    print('''1. Binary to Decimal \t 2. Binary to Ternary" \t 3. Binary to Quaternary\t\t\t\n\t 4. Binary to Octal \t\t  5. Binary to Duodecimal \t\n\t\t 6.Binary to Hexadecimal\n''')
    print("####################################################################################\n")
    print("Please enter your choice: ")
    b=int(input())
    print("Please enter the Binary number: ")
    nm=str(input())
    c=(int(nm,2))
    if b==1:
        print("Decimal form is: ",c)
    elif b==2:
        print("Ternary form is: "), con(nmb=nm,base=3)
    elif b==3:
        print("Quaternary form is: "),con(nmb=c,base=4)
    elif b==4:
        print("Octal form is: ",oct(c))
    elif b==5:
        print("Duodecimal form is : "),con(nmb=c,base=12)
    elif b==6:
        print("Hexadecimal form is: ",hex(c))
    else:
        print("error")
elif a==3:
    print("####################################################################################\n")
    print('''1. Ternary to Decimal \t 2. Ternary to Binary" \t 3. Ternary to Quaternary\t\t\t 4. Ternary to Octal  \t\t 5. Ternary to Duodecimal \t\n\t\t\t  6.Ternary to Hexadecimal\n''')
    print("####################################################################################\n")
    print("Please enter your choice: ")
    b=int(input())
    print("Please enter the Ternary number: ")
    nm=str(input())
    c=(int(nm,3))
    if b==1:
       print("Decimal form is: ",c)
    elif b==2:
        print("Binary form is: ",bin(c))
    elif b==3:
        print("Quaternaty form is : "),con(nmb=c,base=4)
    elif b==4:
        print("Octal form is: ",oct(c))
    elif b==5:
        print("Duodecimal form is: "),con(nmb=c,base=12)
    elif b==6:
        print("Hexadecimal form is: ",hex(c))
    else:
        print("error")
        
elif a==4:
    print("####################################################################################\n")
    print('''1. Quaternary to Decimal \t 2. Quaternary to Binary \t 3. Quaternary to Ternary \t\t\t\n \t 4. Quaternary to Octal \t\t 5. Quaternary to Duodecimal \t\n\t\t\t 6. Quaternary to Hexadecimel \n''')
    print("####################################################################################\n")
    print("Please enter your choice: ")
    b=int(input())
    print("Please enter the Quaternary number: ")
    nm=str(input())
    c=(int(nm,4))
    if b==1:
        print("Decimal form is: ",c)
    elif b==2:
        print("Binary form is: ",bin(c))
    elif b==3:
        print("Ternary form is: "),con(nmb=c,base=3)
    elif b==4:
        print("Octal form is: ",oct(c))
    elif b==5:
        print("Duodecimal form is : "),con(nmb=c,base=12)
    elif b==6:
        print(" Hexadecimal form is: ",hex(c))
    else:
        print("error")
elif a==5:
    print("####################################################################################\n")
    print('''1. Octal to Decimal   \t 2. Octal to Binary  \t     3. Octal to Ternary \t\t\t\n \t 4. Octal to Quaternary \t\t 5. Octal to Duodecimal \t\n\t\t   6. Octal to Hexadecimal\n''')
    print("####################################################################################\n")
    print("Please enter your choice: ")
    b=int(input())
    print("Please enter the Octal number: ")
    nm=str(input())
    c=(int(nm,8))
    if b==1:
        print("Decimal form is: ",c)
    elif b==2:
        print("Binary form is: ",bin(c))
    elif b==3:
        print(" Ternaty form is: "),con(nmb=c,base=3)
    elif b==4:
        print("Quaternary form is: "),con(nmb=c,base=4)
    elif b==5:
        print("Duodecimal form is : "),con(nmb=c,base=12)
    elif b==6:
        print("Hexadecimal form is: ",hex(c))
    else:
        print("error")
elif a==6:
    print("####################################################################################\n")
    print('''1. Duodecimal to Decimal \t 2. Duodecimal to Binary" \t 3. Duodecimal to Ternary \t\t\t\n \t 4. Duodecimal to Quaternary \t\t 5. Duoecimal to Octal \t\n\t\t\t  6. Duodecimal to Hexadecimal\n''')
    print("####################################################################################\n")
    print("Please enter your choice: ")
    b=int(input())
    print("Please enter the Duodecimal number: ")
    nm=str(input())
    c=(int(nm,12))
    if b==1:
        print("Decimal form is: ",c)
    elif b==2:
        print("Binary form is: ",bin(c))
    elif b==3:
        print("Ternary form is: "),con(nmb=c,base=3)
    elif b==4:
        print(" Quaternaty form is: "),con(nmb=c,base=4)
    elif b==5:
        print(" Octal form is : ",oct(c))
    elif b==6:
        print("Hexadecimal form is: ",hex(c))
elif a==7:
    print("####################################################################################\n")
    print('''1. Hexadecimel to Decimal \t 2. Hexadecimel  to Binary " \t 3. Hexadecimel  to Ternary \t\t\t\n \t  4. Hexadecimel to  Quaternary \t\t 5. Hexadecimel  to Octal \t\n\t\t         6. Hexadecimel  to Duodecimal\n''')
    print("####################################################################################\n")
    print("Please enter your choice: ")
    b=int(input())
    print("Please enter the Hexadecimal number: ")
    nm=str(input())
    c=(int(nm,16))
    if b==1:
        print("Decimal form is: ",c)
    elif b==2:
        print("Binary form is: ",bin(c))
    elif b==3:
        print("Ternary form is: "),con(nmb=c,base=3)
    elif b==4:
        print("Quaternaty form is : "),con(nmb=c,base=4)
    elif b==5:
        print("Octal form is: ",oct(c))
    elif b==6:
        print("Duodecimal form is: "),con(nmb=c,base=12)
    else:
        print("error")
else:
    print("error")
