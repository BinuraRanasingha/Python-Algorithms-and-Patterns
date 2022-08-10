instring = input('Enter string...')


for index in range(0,len(instring),3):
    print(instring[index].lower(),end='')

    for index in range(1,len(instring),3):
        print(instring[index].upper(),end='')

        for index in range(2,len(instring),3):
            print('*',end='')
            break
        
